from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/planner')
def planner():
    return render_template('planner.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/reminder')
def reminder():
    return render_template('reminder.html')

@app.route('/ask_ai', methods=['POST'])
def ask_ai():

    data = request.get_json()

    user_message = data.get('message')

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are Manjora AI, an advanced AI mentor."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        ai_reply = response.choices[0].message.content

        return jsonify({
            'reply': ai_reply
        })

    except Exception as e:

        return jsonify({
            'reply': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)