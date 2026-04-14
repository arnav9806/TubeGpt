#  TubeGPT – AI-Powered YouTube Assistant

TubeGPT is an AI-powered system that transforms YouTube videos into an interactive learning experience.

Instead of passively watching videos, users can:

*  Get summaries
*  Ask questions
*  Search concepts
*  Generate notes
*  Learn in a structured way
 Built using **RAG (Retrieval-Augmented Generation)** architecture.

---

#  Features

##  Core Features

* YouTube video processing (URL input)
* Transcript extraction
* AI-based summaries (short + detailed)
* Chatbot (ask questions about video)

##  Advanced Features

* Multi-level summaries (TL;DR, detailed, bullet points)
* Semantic search
* Timestamp-based answers
* Notes generator (study notes, flashcards)
* Learning modes (Beginner / Intermediate / Advanced)
* Multi-language support
* Important segment detection

---

#  Tech Stack

## Backend

* FastAPI
* PostgreSQL
* Redis
* Celery

## AI / ML

* OpenAI / Gemini
* LangChain / LlamaIndex
* FAISS (Vector DB)

## Frontend

* Streamlit (initial UI)

## DevOps

* Docker
* Docker Compose

---

#  Project Structure

```
tubegpt/
│
├── app/                # Backend (FastAPI)
├── streamlit_app/      # Frontend (Streamlit)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```
git clone https://github.com/arnav9806/TubeGpt.git
cd TubeGpt
```

---

## 2️⃣ Create Virtual Environment

### Windows:

```
py -3.8 -m venv venv
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pip install -r requirements.txt


```

---

## 4️⃣ Setup Environment Variables

Create a `.env` file in root:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/tubegpt
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_api_key
REDIS_URL=redis://localhost:6379
```

---

# 🚀 Running the Project

## ▶️ Run Backend (FastAPI)

```
uvicorn app.main:app --reload
```

Open:
👉 http://localhost:8000/docs

---

## 🖥️ Run Frontend (Streamlit)

```
streamlit run streamlit_app/app.py
```

---

## 🐳 Run with Docker (Recommended)

```
docker-compose up --build
```

---

# 🔄 Workflow

1. User inputs YouTube URL
2. Transcript extracted
3. Text chunked
4. Embeddings generated
5. Stored in vector DB
6. User asks question
7. Relevant chunks retrieved
8. LLM generates answer

---

# 👥 Collaboration Guide

* Create a new branch:

  ```
  git checkout -b feature/your-feature
  ```
* Push changes:

  ```
  git push origin feature/your-feature
  ```
* Create a Pull Request

 Direct push to `main` is restricted.

---

#  Future Enhancements

* React/Next.js frontend
* Knowledge graph visualization
* Real-time video summarization
* Notion integration
* Voice-based interaction

---

#  Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---

#  License

This project is for learning and development purposes.

---

#  Support

If you like this project, give it a ⭐ on GitHub!


