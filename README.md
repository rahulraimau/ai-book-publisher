# 📚 AI Book Publisher

An **AI-powered publishing assistant** that:
- 📖 Scrapes public-domain books from [Wikisource](https://en.wikisource.org/)
- ✍️ Rewrites content using **Gemini** (Google's LLM)
- 🧠 Reviews AI output using **Reinforcement Learning (RL)** reward scoring
- 🔁 Supports **Human-in-the-Loop (HITL)** editing iterations
- 🗃️ Stores versioned chapters using **ChromaDB**
- 🔊 Reads rewritten content aloud via **Text-to-Speech (TTS)**

---

## 🎬 Demo Video

👉 [Watch the full demo on Loom](https://www.loom.com/share/your-loom-video-id)

---

## 🚀 Features Explained

### 🔍 1. Scraping + Screenshot
Fetches chapter content directly from a given **Wikisource URL**, parses HTML using BeautifulSoup, and optionally captures the web page with Playwright (screenshot).

> _Example:_
```txt
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
✍️ 2. AI Writer (Gemini API)
Uses Gemini 1.5 Flash via Google's Generative AI API to paraphrase and creatively rewrite the chapter text.

Prompted with:

pgsql
Copy
Edit
Paraphrase and creatively rewrite the following chapter text:
🧠 3. AI Reviewer (RL Reward System)
Calculates a reward score for rewritten chapters using:

✅ Semantic Similarity (Cosine Distance using Sentence Transformers)

✅ Lexical Diversity (Jaccard Distance of tokens)

✅ Novelty Score

Reward formula:

Copy
Edit
0.4 * Similarity + 0.4 * Novelty + 0.2 * Jaccard Diversity
🔁 4. Human-in-the-Loop Workflow
Allows human editors to:

View AI-spun content

Modify or accept AI output

Track revisions across 3 iterations

Get reward score feedback after each edit

🗃️ 5. Versioning with ChromaDB
Each rewrite is saved to a vector database (ChromaDB) for:

Easy history tracking

Fast semantic search among previous versions

🔊 6. Voice Output (TTS)
Uses gTTS (Google Text-to-Speech) to speak AI-rewritten content aloud and saves audio as .mp3.

🖥️ Streamlit App (Optional)
You can run this as a Streamlit web app:

bash
Copy
Edit
streamlit run app.py
📡 Use ngrok for public sharing:

bash
Copy
Edit
ngrok http 8501
📦 Folder Structure
bash
Copy
Edit
ai-book-publisher/
├── app.py                  # Streamlit UI
├── main.py                 # CLI entry point
├── pipeline.py             # Core scraping/writing/review logic
├── chroma_utils.py         # Version storage & semantic search
├── voice_utils.py          # TTS functions
├── playwright_screenshot.py # Optional: take screenshot of page
├── requirements.txt
├── .env.example            # API keys template
└── README.md
🛠️ Setup Instructions
bash
Copy
Edit
git clone https://github.com/your-username/ai-book-publisher.git
cd ai-book-publisher

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key in .env
cp .env.example .env
nano .env  # Or open in any editor
📡 Required API Keys
GEMINI_API_KEY from Google AI Studio

(Optional) NGROK_AUTH_TOKEN for live Streamlit demo

🧪 Example Usage
python
Copy
Edit
from pipeline import run_interactive_pipeline

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
final_version, final_score = run_interactive_pipeline(url)
🧠 Tech Stack
Component	Tool Used
AI Writing	Gemini 1.5 Flash (Google LLM)
Scraping	BeautifulSoup, Requests
Voice TTS	gTTS
RL Review	Sentence Transformers
Versioning	ChromaDB
UI (Optional)	Streamlit

🏁 Submission Checklist
✅ Code pushed to GitHub
✅ .env.example file provided
✅ Loom video recorded and linked
✅ README.md with usage and demo

📩 Contact / Help
For issues or feature requests, create a GitHub issue or email at your@email.com.

markdown
Copy
Edit

Would you like me to:

- Fill in your **real Loom link and GitHub URL**?
- Add **badges** (like `Made with Gemini`, `MIT License`, etc.)?
- Generate a **PDF version** of this README for submission?

Let me know, and I’ll finalize everything.






You said:
write in copy paste format


ChatGPT said:
Absolutely! Below is a copy-paste ready README.md for your AI Book Publisher project. Just replace placeholders like your-username and your-loom-link before publishing:

markdown
Copy
Edit
# 📚 AI Book Publisher

An **AI-powered publishing assistant** that helps transform classic texts into rewritten content using cutting-edge AI — with human input, voice support, and reinforcement learning-based feedback.

---

## 🎬 Demo Video

👉 [Watch the full demo on Loom](https://www.loom.com/share/your-loom-video-id)

---

## 🚀 Features Explained

### 🔍 1. Scraping from Wikisource
Fetches chapter content directly from public-domain books hosted on [Wikisource](https://en.wikisource.org/). Optionally captures screenshots with Playwright.

> Example URL:
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1

yaml
Copy
Edit

---

### ✍️ 2. AI Writer (Gemini 1.5 Flash)
Uses Google’s **Gemini LLM** to rewrite chapters creatively with paraphrasing and simplification. Controlled via prompt instructions.

---

### 🧠 3. AI Reviewer (Reinforcement Learning Scoring)
Measures:
- **Semantic Similarity** using Sentence Transformers
- **Lexical Diversity** (Jaccard score)
- **Novelty** from embeddings

Reward formula:
Reward = 0.4 * Similarity + 0.4 * Novelty + 0.2 * Diversity

yaml
Copy
Edit

---

### 🔁 4. Human-in-the-Loop Workflow
Allows manual editing of AI output with reward scoring after every iteration. Saves each version to a vector database.

---

### 🗃️ 5. Versioning via ChromaDB
All rewrites are versioned in **ChromaDB**. You can perform **semantic search** to find the most relevant version of rewritten content.

---

### 🔊 6. Text-to-Speech (TTS)
Uses Google’s `gTTS` to read AI-generated text aloud and save as `.mp3`.

---

## 🖥️ Streamlit Web App (Optional)

To run a visual UI for the entire pipeline:

```bash
streamlit run app.py
To share it publicly:

bash
Copy
Edit
ngrok http 8501
📁 Project Structure
graphql
Copy
Edit
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
🛠️ Setup Instructions
bash
Copy
Edit
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
🔑 Required API Keys
Name	Source
GEMINI_API_KEY	Google AI Studio
NGROK_AUTH_TOKEN	ngrok.com (optional for public Streamlit)

🧪 Example Code
python
Copy
Edit
from pipeline import run_interactive_pipeline

chapter_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
final_version, reward_score = run_interactive_pipeline(chapter_url)
🧠 Tech Stack
Component	Tool Used
AI Writer	Gemini 1.5 Flash
Web Scraper	BeautifulSoup, Playwright
Review System	Sentence Transformers
Versioning	ChromaDB
TTS	gTTS
Frontend	Streamlit

🧾 Submission Checklist
 ✅ Code pushed to GitHub

 ✅ Loom video recorded and linked

 ✅ .env.example provided

 ✅ README.md with setup + usage

👨‍💻 Author
Made by [Your Name]
🔗 GitHub: github.com/your-username
✉️ Email: your@email.com

🪪 License
MIT License. Free to use with attribution.

yaml
Copy
Edit
