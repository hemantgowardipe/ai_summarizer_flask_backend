# 🧠 AI Document Summarizer – Advanced Backend (Flask, Transformers, PDF)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-API-orange?logo=flask"/>
  <img src="https://img.shields.io/badge/Transformers-HuggingFace-yellow?logo=python"/>
  <img src="https://img.shields.io/badge/Render.com-Deployed-success?logo=render"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
</p>

---

## ✨ Overview

**AI Document Summarizer** is a robust Flask-based backend for intelligent document and text summarization, tailored for seamless integration with modern web frontends (e.g., React). Using state-of-the-art NLP models, it can distill lengthy text passages or PDF documents into concise, human-readable summaries—ready for consumption in your apps, portals, or workflows.

**Live Demo (Render.com):**
```
https://your-app-name.onrender.com
```

---

## 🚀 Feature Highlights

- **AI-Powered Summarization:** Utilizes HuggingFace Transformers for superior extractive and abstractive summarization.
- **PDF Parsing:** Efficiently extracts and processes text from PDF files using PyMuPDF.
- **RESTful API:** Exposes a single `/api/summarize` endpoint for easy POST integration.
- **CORS Enabled:** Built-in support for cross-origin requests (frontend-backend separation).
- **Production Ready:** Deployed on Render, with simple environment configuration.
- **Modular Codebase:** Clean separation of concerns for maintainability and extensibility.

---

## 🏗️ Tech Stack

| Technology     | Role                                |
|----------------|-------------------------------------|
| **Flask**      | REST API server                     |
| **Flask-CORS** | Enables CORS for frontend access    |
| **Transformers** | State-of-the-art NLP summarization |
| **PyMuPDF**    | Fast and reliable PDF text parsing  |
| **Render**     | Cloud deployment platform           |

---

## 📂 Project Structure

```bash
backend/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── summarize.py           # Summarization logic (Transformers)
├── utils/
│   └── pdf_extractor.py   # PDF-to-text utility
```

---

## ⚡ Quickstart – Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-backend-repo.git
   cd your-backend-repo
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install All Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Server**
   ```bash
   python app.py
   ```
   The API will be live at: [http://localhost:5000](http://localhost:5000)

---

## 🧪 API Usage Guide

**Endpoint:** `POST /api/summarize`

- **Request Body (JSON):**
  ```json
  {
    "text": "Paste your long input text here..."
  }
  ```
- **Response (JSON):**
  ```json
  {
    "summary": "Generated summary goes here..."
  }
  ```

### 📝 Example with `curl`
```bash
curl -X POST http://localhost:5000/api/summarize \
     -H "Content-Type: application/json" \
     -d '{"text":"Your long text to summarize..."}'
```

---

## 🛰️ Zero-Hassle Deployment (Render.com)

1. **Push Your Code to GitHub**
2. **Sign in at [Render.com](https://render.com)**
3. **Create New Web Service**:
   - Connect your repo
   - Set **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Instance Type**: Free or Starter
   - **Environment Variable**:  
     - Key: `PORT`  
     - Value: `5000`
4. **Deploy & Go Live** 🚀

---

## 🔐 CORS Configuration

CORS is enabled by default in `app.py`:

```python
from flask_cors import CORS
CORS(app)
```
This allows your React (or any) frontend to interact with the backend securely across domains.

---

## 💡 Core Code Samples

### `app.py`
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from summarize import generate_summary
from utils.pdf_extractor import extract_text_from_pdf

app = Flask(__name__)
CORS(app)

@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    input_text = data.get('text', '')
    
    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400
    
    summary = generate_summary(input_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
```

### `summarize.py`
```python
from transformers import pipeline

summarizer = pipeline("summarization")

def generate_summary(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']
```

### `requirements.txt`
```
Flask
flask-cors
transformers
torch
PyMuPDF
```

---

## 🧙‍♂️ Pro Tips

- **Model Customization:** The summarizer pipeline can be swapped or fine-tuned for domain-specific summarization.
- **PDF Handling:** Use `utils/pdf_extractor.py` to preprocess and clean extracted PDF text before summarization.
- **Scaling:** For production, consider Gunicorn + Nginx and HuggingFace model caching.

---

## 👨‍💻 Author

**Hemant Gowaedipe**  
[LinkedIn](https://www.linkedin.com/in/hemantgowardipe)  

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---
