# 📚 AI Book Publisher

End-to-end system to scrape, rewrite, review, narrate, and semantically track book content using Gemini API, RL reward logic, and ChromaDB.

## Features
- Gemini-based creative AI Writer
- RL-based reviewer with reward scoring
- Screenshot capture with Playwright
- Voice narration (pyttsx3)
- Versioning & semantic search (ChromaDB)
- Streamlit interface

## Setup
1. Install:
```bash
pip install -r requirements.txt
playwright install
```

2. Create `.env`:
```env
GEMINI_API_KEY=your_actual_key
```

3. Run:
```bash
streamlit run app.py
```