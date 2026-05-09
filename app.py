import os

from openai import OpenAI

from flask import jsonify, request

client = OpenAI(

    api_key=os.getenv("OPENAI_API_KEY")

)

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
                    "content": "You are Manjora AI, an advanced AI mentor for education, productivity, coding, UPSC preparation and career guidance."
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