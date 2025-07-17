from flask import Flask, request, jsonify
from flask_cors import CORS
from summarize import generate_summary
from utils.pdf_extractor import extract_text_from_pdf
import os

app = Flask(__name__)
CORS(app)

# ✅ Root route to confirm server is live
@app.route('/')
def home():
    return jsonify({'message': 'Flask backend is running!'})

# ✅ Your API route
@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    input_text = data.get('text', '')

    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400

    summary = generate_summary(input_text)
    return jsonify({'summary': summary})

# ✅ Ensure compatibility with Render (uses dynamic port)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render will set PORT env variable
    app.run(host='0.0.0.0', port=port)
