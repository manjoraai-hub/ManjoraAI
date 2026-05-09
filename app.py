from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/ask_ai', methods=['POST'])
def ask_ai():

    data = request.get_json()

    user_message = data.get('message')

    try:

        response = client.chat.completions.create(

            model="gpt-3.5-turbo",

            messages=[
                {
                    "role": "system",
                    "content": "You are Manjora AI, an AI mentor for students, UPSC aspirants and programmers."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]

        )

        ai_reply = response.choices[0].message.content

        return jsonify({
            "reply": ai_reply
        })

    except Exception as e:

        return jsonify({
            "reply": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)