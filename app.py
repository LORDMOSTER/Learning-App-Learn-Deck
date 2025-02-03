from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'  # Use your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Flashcard model
class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=True)

# Create the database and add sample flashcards
with app.app_context():
    db.create_all()  # Create tables if they don't exist

    # Sample flashcards
    flashcards = [
        Flashcard(subject='Mathematics', text='What is the Pythagorean theorem?', image='path/to/image1.jpg'),
        Flashcard(subject='Science', text='What is the chemical symbol for water?', image='path/to/image2.jpg'),
        Flashcard(subject='History', text='Who was the first president of the United States?', image='path/to/image3.jpg'),
        Flashcard(subject='Language Arts', text='What is a synonym for "happy"?', image='path/to/image4.jpg'),
        Flashcard(subject='Geography', text='What is the capital of France?', image='path/to/image5.jpg'),
    ]

    # Add flashcards to the session and commit
    db.session.add_all(flashcards)
    db.session.commit()

    print("Sample flashcards added successfully!")