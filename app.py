from flask import Flask, render_template

app = Flask(__name__)

# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():

    return render_template('dashboard.html')

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