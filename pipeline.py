import os, requests, nltk, uuid
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
import google.generativeai as genai
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from gtts import gTTS

# Download required NLTK data
nltk.download('punkt')

# Gemini API setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
reward_model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB setup
chroma_client = chromadb.Client()
embedding_fn = SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")
collection = chroma_client.create_collection("chapters", embedding_function=embedding_fn)

# Step 1: Scrape chapter
def fetch_chapter(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    paragraphs = soup.select("div#mw-content-text p")
    return "\n\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 50])

# Step 2: Use Gemini to rewrite chapter
def ai_writer(text):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    prompt = f"Paraphrase and creatively rewrite the following chapter text:\n\n{text[:2000]}"
    response = model.generate_content(prompt)
    return response.text.strip()

# Step 3: RL-style reviewer
def ai_reviewer(original, spun):
    orig_tokens = set(nltk.word_tokenize(original.lower()))
    spun_tokens = set(nltk.word_tokenize(spun.lower()))
    jaccard_sim = len(orig_tokens & spun_tokens) / len(orig_tokens | spun_tokens)
    orig_emb = reward_model.encode(original, convert_to_tensor=True)
    spun_emb = reward_model.encode(spun, convert_to_tensor=True)
    sim = util.pytorch_cos_sim(orig_emb, spun_emb).item()
    novelty = 1 - sim
    reward = 0.4 * sim + 0.4 * novelty + 0.2 * (1 - jaccard_sim)
    return {
        "semantic_similarity": round(sim, 3),
        "novelty": round(novelty, 3),
        "jaccard_diversity": round(1 - jaccard_sim, 3),
        "final_reward_score": round(reward, 3)
    }

# Step 4: TTS feedback
def speak(text, filename="tts_output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename

# Step 5: Save version to ChromaDB
def save_version(text, meta):
    version_id = str(uuid.uuid4())
    collection.add(documents=[text], metadatas=[meta], ids=[version_id])
    return version_id

# Step 6: Semantic search among versions
def semantic_search(query_text):
    result = collection.query(query_texts=[query_text], n_results=1)
    return result['documents'][0] if result['documents'] else "No match found."

# Full human-in-the-loop workflow
def run_interactive_pipeline(url):
    original = fetch_chapter(url)
    current = ai_writer(original)
    print("\n🌀 AI-Spun Version (excerpt):\n", current[:400])

    for i in range(3):
        print(f"\n✍️ Iteration {i+1}: You may refine the text manually below")
        current = input("\nYour rewrite (or press Enter to keep AI version):\n") or current
        reward = ai_reviewer(original[:512], current)
        version_id = save_version(current, {"iteration": i + 1, "reward": reward})
        print("✅ Reward:", reward)
        print("💾 Saved as version:", version_id)
        speak(current[:300], f"readout_{i+1}.mp3")

    return current, reward
