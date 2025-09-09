import os
import logging
import uuid
from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
from gemini_service import generate_mandala_description, generate_mandala_image
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Ensure static/images directory exists
os.makedirs('static/images', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_mandala', methods=['POST'])
def generate_mandala():
    try:
        data = request.get_json()
        user_thought = data.get('thought', '').strip()
        
        if not user_thought:
            return jsonify({'error': 'Por favor, digite um pensamento ou ideia'}), 400
        
        logging.info(f"Generating mandala for thought: {user_thought}")
        
        # Step 1: Generate artistic description using free APIs
        description = generate_mandala_description(user_thought)
        if not description:
            return jsonify({'error': 'Falha ao gerar a descrição da mandala'}), 500
        
        logging.info(f"Generated description: {description}")
        
        # Step 2: Generate mandala image using Lorem Picsum
        image_filename = f"mandala_{uuid.uuid4().hex}.png"
        image_path = os.path.join('static/images', image_filename)
        
        success = generate_mandala_image(description, image_path)
        if not success:
            return jsonify({'error': 'Falha ao gerar a imagem da mandala'}), 500
        
        logging.info(f"Generated image saved to: {image_path}")
        
        # Step 3: Generate QR code for the image
        image_url = url_for('serve_image', filename=image_filename, _external=True)
        qr_code_data = generate_qr_code(image_url)
        
        return jsonify({
            'description': description,
            'image_url': image_url,
            'qr_code': qr_code_data,
            'success': True
        })
        
    except Exception as e:
        logging.error(f"Error generating mandala: {str(e)}")
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

def generate_qr_code(url):
    """Generate QR code using external API and return the image URL"""
    try:
        # Use goqr.me API to generate QR code
        qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={url}"
        return qr_api_url
        
    except Exception as e:
        logging.error(f"Error generating QR code: {str(e)}")
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
