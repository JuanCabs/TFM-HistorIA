from app import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    processed_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Document {self.filename}>'
