import os
from flask import Flask, render_template, request, redirect, url_for, flash
import pdfplumber
from PIL import Image
import pytesseract

# Set Tesseract path for Windows
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
except:
    pass  # Tesseract not installed, will handle in error

app = Flask(__name__)
app.secret_key = 'supersecret'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except pytesseract.pytesseract.TesseractNotFoundError:
        raise Exception("Tesseract OCR is not installed. Please install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki")
    except Exception as e:
        raise Exception(f"Error extracting text from image: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    extracted_text = None
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            flash('No file selected!')
            return redirect(request.url)
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        try:
            if file.filename.lower().endswith('.pdf'):
                extracted_text = extract_text_from_pdf(filename)
            elif file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                extracted_text = extract_text_from_image(filename)
            else:
                flash('Unsupported file type!')
        except Exception as e:
            flash(f'Error processing file: {str(e)}')
        os.remove(filename)
    return render_template('index.html', extracted_text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
