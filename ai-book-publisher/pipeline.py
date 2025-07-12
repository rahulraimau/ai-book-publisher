import os, requests, nltk
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

nltk.download('punkt')
reward_model = SentenceTransformer('all-MiniLM-L6-v2')

def fetch_wikisource_chapter(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    paragraphs = soup.select('div#mw-content-text p')
    return "\n\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 50])

def ai_writer(text):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Paraphrase and creatively rewrite the following chapter text:\n\n{text[:2000]}"
    response = model.generate_content(prompt)
    return response.text.strip()

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

def run_pipeline(url):
    original = fetch_wikisource_chapter(url)
    spun = ai_writer(original)
    reward = ai_reviewer(original[:512], spun)
    return original, spun, reward