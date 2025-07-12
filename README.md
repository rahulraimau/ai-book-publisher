# 📚 AI Book Publisher

An **AI-powered publishing assistant** that helps transform classic texts into rewritten content using cutting-edge AI — with human input, voice support, and reinforcement learning-based feedback.

---

## 🎮 Demo Video

👉 [Watch the full demo on Loom](https://www.loom.com/share/your-loom-video-id)

---

## 🚀 Features Explained

### 🔍 1. Scraping from Wikisource

Fetches chapter content directly from public-domain books hosted on [Wikisource](https://en.wikisource.org/). Optionally captures screenshots with Playwright.

> Example URL:

```
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
```

---

### ✍️ 2. AI Writer (Gemini 1.5 Flash)

Uses Google’s **Gemini LLM** to rewrite chapters creatively with paraphrasing and simplification. Controlled via prompt instructions.

---

### 🧠 3. AI Reviewer (Reinforcement Learning Scoring)

Measures:

* **Semantic Similarity** using Sentence Transformers
* **Lexical Diversity** (Jaccard score)
* **Novelty** from embeddings

Reward formula:

```
Reward = 0.4 * Similarity + 0.4 * Novelty + 0.2 * Diversity
```

---

### 🔁 4. Human-in-the-Loop Workflow

Allows manual editing of AI output with reward scoring after every iteration. Saves each version to a vector database.

---

### 📃️ 5. Versioning via ChromaDB

All rewrites are versioned in **ChromaDB**. You can perform **semantic search** to find the most relevant version of rewritten content.

---

### 🔊 6. Text-to-Speech (TTS)

Uses Google’s `gTTS` to read AI-generated text aloud and save as `.mp3`.

---
Metric,Description,Range,Ideal Range,Interpretation
Semantic Similarity,Cosine similarity between original and spun embeddings,0.0 – 1.0,0.6 – 0.85,Closer to 1.0 = semantically similar
Novelty,1 - semantic similarity,0.0 – 1.0,0.4 – 0.6,Closer to 1.0 = more novel
Jaccard Diversity,Word-level difference using token overlap,0.0 – 1.0,0.3 – 0.7,Higher value = more lexical diversity
Final Reward Score,Combined reward: 0.4*sim + 0.4*novelty + 0.2*jaccard_diversity,0.0 – 1.0,0.6 – 0.9,Balanced indicator of rewrite quality
## 🖥️ Streamlit Web App (Optional)

To run a visual UI for the entire pipeline:

```bash
streamlit run app.py
```

To share it publicly:

```bash
ngrok http 8501
```

---

## 📁 Project Structure

```
ai-book-publisher/
├── app.py                  # Streamlit frontend
├── main.py                 # CLI runner
├── pipeline.py             # Scraper + Writer + Reviewer logic
├── chroma_utils.py         # Vector DB utilities
├── voice_utils.py          # Text-to-Speech functions
├── playwright_screenshot.py # (Optional) webpage screenshots
├── requirements.txt
├── .env.example            # Template for API keys
└── README.md
```

---

## 💠 Setup Instructions

```bash
git clone https://github.com/your-username/ai-book-publisher.git
cd ai-book-publisher

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add Gemini API key
cp .env.example .env
nano .env  # Paste your GEMINI_API_KEY
```

---

## 🔑 Required API Keys

| Name               | Source                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------ |
| GEMINI\_API\_KEY   | [Google AI Studio](https://makersuite.google.com/app)                                      |
| NGROK\_AUTH\_TOKEN | [ngrok.com](https://dashboard.ngrok.com/get-started/setup) (optional for public Streamlit) |

---

## 🧲 Example Code

```python
from pipeline import run_interactive_pipeline

chapter_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
final_version, reward_score = run_interactive_pipeline(chapter_url)
```

---

## 🧠 Tech Stack

| Component     | Tool Used                 |
| ------------- | ------------------------- |
| AI Writer     | Gemini 1.5 Flash          |
| Web Scraper   | BeautifulSoup, Playwright |
| Review System | Sentence Transformers     |
| Versioning    | ChromaDB                  |
| TTS           | gTTS                      |
| Frontend      | Streamlit                 |

---

## 🗾️ Submission Checklist

* [x] ✅ Code pushed to GitHub
* [x] ✅ Loom video recorded and linked
* [x] ✅ `.env.example` provided
* [x] ✅ `README.md` with setup + usage

---

## 👨‍💼 Author

Made by \[Your Name]
🔗 GitHub: [github.com/rahulraimau](https://github.com/rahulraimau)
✉️ Email: [rahulraimau5@@gmail.com](mailto:rahulraimau5@gmail.com)

---

## 📺 License

MIT License. Free to use with attribution.
