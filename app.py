from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():

    return """
    <h1>🚀 Manjora AI</h1>

    <a href='/affairs'>
    Open Current Affairs
    </a>
    """

@app.route('/affairs')
def affairs():

    articles = [

        {
            "title": "India launches new education initiative",

            "description":
            "New reforms introduced for digital learning.",

            "url":
            "https://www.thehindu.com/news/national/",

            "image":
            "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
        }

    ]

    return render_template(
        'affairs.html',
        articles=articles
    )

if __name__ == '__main__':

    app.run(debug=True)
from flask import Flask, render_template

@app.route('/')
def home():

    return """
    <h1 style='font-family:Arial;'>
    🚀 Manjora AI Working
    </h1>

    <a href='/affairs'
    style='font-size:22px;'>
    Open Current Affairs
    </a>
    """

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
            "https://www.thehindu.com/news/national/",

            "image":
            "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
        },

        {
            "title":
            "UPSC aspirants adopting AI tools for preparation",

            "description":
            "Students increasingly use AI-based platforms for study planning and revision.",

            "url":
            "https://indianexpress.com/latest-news/",

            "image":
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
        },

        {
            "title":
            "Technology transforming competitive exam learning",

            "description":
            "AI and productivity platforms are reshaping online education systems.",

            "url":
            "https://www.hindustantimes.com/",

            "image":
            "https://images.unsplash.com/photo-1455390582262-044cdead277a"
        }

    ]

    return render_template(
        'affairs.html',
        articles=articles
    )

# =========================
# RUN APP
# =========================

if __name__ == '__main__':

    app.run(debug=True)