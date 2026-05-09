from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

        # Simple demo login
        if username and password:

            return redirect(url_for('dashboard'))

    return render_template('login.html')


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
# RUN APP
# =========================

if __name__ == '__main__':

    app.run(debug=True)