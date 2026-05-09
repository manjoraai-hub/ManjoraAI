from flask import Flask, render_template

app = Flask(__name__)

# =========================
# DASHBOARD
# =========================
# =========================
# LOGIN
# =========================

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


# =========================
# PLANNER
# =========================

@app.route('/planner')
def planner():

    return render_template('planner.html')


# =========================
# CAREER
# =========================

@app.route('/career')
def career():

    return render_template('career.html')


# =========================
# BOOKS
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
# RUN APP
# =========================

if __name__ == '__main__':

    app.run(debug=True)