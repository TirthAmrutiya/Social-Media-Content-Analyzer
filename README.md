# Social Media Content Analyzer

A minimal Flask-based web application for extracting text from PDF and image files (JPG/PNG) using PDF parsing and OCR technology.

## Features

- Upload PDF files and extract formatted text using `pdfplumber`.
- Upload image files (JPG, PNG) and extract text using OCR with `pytesseract`.
- Simple web interface with Bootstrap styling.
- Error handling for unsupported file types and processing errors.
- Temporary file storage for security.

## Requirements

- Python 3.7+
- Tesseract OCR engine installed on the system (for image text extraction)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd social-media-content-analyzer
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - On Windows: Download and install from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - On macOS: `brew install tesseract`
   - On Linux: `sudo apt-get install tesseract-ocr`

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Upload a PDF or image file using the form.

4. View the extracted text displayed on the page.

## Deployment

This app can be deployed to platforms like Streamlit Cloud, Vercel, or Render for easy hosting.

## Brief Write-up

The Social Media Content Analyzer allows users to effortlessly upload PDF and image files, extracting text through PDF parsing (using pdfplumber) and image OCR (using pytesseract). The simple Flask-based interface supports drag-and-drop or file picker uploads. Error-handling ensures users only process supported files, and temporary storage is used for security. Documented, clean code ensures production-readiness, while modular functions allow easy extension for further features like engagement suggestions, all deliverable within a short 3-hour window.
