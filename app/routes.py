import os
from flask import Flask, request
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load the model and tokenizer
model_name = "mistralai/Mistral-7B-Instruct-v0.3"  
generator = pipeline('text-generation', model=model_name, token='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')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {"error": "No file part"}, 400
    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400
    content = file.read().decode('utf-8')
    prompt = f"haz un resumen de este texto {content}"
    response = query_local_model(prompt)
    return {"message": response}, 200

def query_local_model(prompt):
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text'] if response else "No se pudo generar una respuesta."

@app.route('/prompt', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return "No prompt provided", 400

    response = query_local_model(prompt)
    return response, 200

def query_local_model(prompt):
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text'] if response else "No se pudo generar una respuesta."

if __name__ == '__main__':
    app.run(debug=True)
