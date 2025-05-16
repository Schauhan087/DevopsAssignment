import random
import flask
from flask import Flask, request, render_template

app = Flask(__name__)

# List of fun Instagram captions
captions = [
    "Living my best life one photo at a time ✨",
    "Less Monday, more sunshine ☀️",
    "Adventure awaits, go find it 🌍",
    "Making memories, one picture at a time 📸",
    "Good vibes only 🌈",
    "Keeping it real since [birth year] 💯",
    "Life is short, make every picture count 📷",
    "Just another day in paradise 🏝️",
    "Not all who wander are lost 🧭",
    "Crazy hair, don't care 💁‍♀️",
    "Coffee in one hand, confidence in the other ☕",
    "Too glam to give a damn ✨",
    "Sunshine mixed with a little hurricane 🌪️",
    "Messy hair, messy life, beautiful chaos 💫",
    "Friday state of mind 🙌"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    mood = request.form.get('mood', 'happy')
    filtered_captions = captions  # In a real app, we would filter by mood
    caption = random.choice(filtered_captions)
    return render_template('index.html', caption=caption)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)