import os
from openai import OpenAI
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

client = OpenAI(

    api_key="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"

)

# =========================
# HOME PAGE
# =========================

@app.route('/')
def index():

    return render_template('index.html')


# =========================
# LOGIN
# =========================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        # Demo Login

        if username and password:

            return redirect(url_for('dashboard'))

    return render_template('login.html')


# =========================
# REGISTER
# =========================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        return redirect(url_for('login'))

    return render_template('register.html')


# =========================
# DASHBOARD
# =========================

@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


# =========================
# STUDY PLANNER
# =========================

@app.route('/planner')
def planner():

    return render_template('planner.html')


# =========================
# CAREER ROADMAP
# =========================

@app.route('/career')
def career():

    return render_template('career.html')


# =========================
# BOOKS & LECTURES
# =========================

@app.route('/books')
def books():

    return render_template('books.html')


# =========================
# CURRENT AFFAIRS
# =========================

@app.route('/affairs')
def affairs():

    articles = [

        {
            "title":
            "India launches AI-powered education reforms",

            "description":
            "Government introduces smart classrooms and digital learning initiatives.",

            "url":
            "https://www.thehindu.com/",

            "image":
            "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
        },

        {
            "title":
            "UPSC aspirants adopting AI tools for preparation",

            "description":
            "Students increasingly use AI-based platforms for study planning and revision.",

            "url":
            "https://indianexpress.com/",

            "image":
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
        }

    ]

    return render_template(
        'affairs.html',
        articles=articles
    )


# =========================
# SOFTWARE JOBS
# =========================

@app.route('/software')
def software():

    return render_template('software.html')


# =========================
# UPSC
# =========================

@app.route('/upsc')
def upsc():

    return render_template('upsc.html')


# =========================
# BANKING
# =========================

@app.route('/banking')
def banking():

    return render_template('banking.html')


# =========================
# GATE
# =========================

@app.route('/gate')
def gate():

    return render_template('gate.html')


# =========================
# AI CHATBOT
# =========================

@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()

    user_message = data.get("message")

    try:

        response = client.chat.completions.create(

            model="gpt-3.5-turbo",

            messages=[

                {
                    "role": "system",
                    "content":
                    "You are Manjora AI, a smart educational assistant for students, UPSC aspirants, coders and productivity learners."
                },

                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({

            "reply": reply

        })

    except Exception as e:

        return jsonify({

            "reply":
            f"Error: {str(e)}"

        })


# =========================
# RUN APP
# =========================

if __name__ == '__main__':

    app.run(debug=True)