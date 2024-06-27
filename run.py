import os
from flask import Flask, request, Response
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para todas las rutas

# Cargar el modelo localmente
model_name = "PlanTL-GOB-ES/gpt2-large-bne"

try:
    generator = pipeline('text-generation', model=model_name)
except Exception as e:
    print(f"Error loading model: {e}")

# Función para consultar el modelo localmente
def query_local_model(prompt):
    response = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)
    return response[0]['generated_text'] if response else "No se pudo generar una respuesta."

# Ruta para subir archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return Response("No file part", status=400)
    file = request.files['file']
    if file.filename == '':
        return Response("No selected file", status=400)
    content = file.read().decode('utf-8')
    prompt = f"Haz un resumen de este texto: {content}"
    response = query_local_model(prompt)
    return Response(response, status=200, mimetype='text/plain')

# Ruta para manejar prompts
@app.route('/prompt', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return Response("No prompt provided", status=400)

    response = query_local_model(prompt)
    return Response(response, status=200, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
