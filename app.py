from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/ask_ai', methods=['POST'])
def ask_ai():

    data = request.get_json()

    user_message = data.get('message')

    return jsonify({
        "reply": f"You said: {user_message}"
    })

if __name__ == '__main__':
    app.run(debug=True)