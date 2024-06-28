def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Procesamiento del texto (por ejemplo, convertir a mayúsculas)
    return text.upper()

def save_processed_text(filename, processed_text):
    from app import db  # Importar aquí para evitar importación circular
    from app.models import Document  # Importar aquí para evitar importación circular
    document = Document(filename=filename, processed_text=processed_text)
    db.session.add(document)
    db.session.commit()
