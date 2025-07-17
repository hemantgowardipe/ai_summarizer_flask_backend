from flask import Flask, request, jsonify
from flask_cors import CORS
from summarize import generate_summary
from utils.pdf_extractor import extract_text_from_pdf
import os

web: gunicorn app:app
CORS(app)

@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json()

    # Get text from request
    input_text = data.get('text', '')

    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400

    summary = generate_summary(input_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
