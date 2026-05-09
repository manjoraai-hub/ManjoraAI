from flask import Flask, render_template

app = Flask(__name__)

# Landing page first
@app.route('/')
def home():
    return render_template('index.html')

# Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Register page
@app.route('/register')
def register():
    return render_template('register.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Planner
@app.route('/planner')
def planner():
    return render_template('planner.html')

# Career Roadmaps
@app.route('/career')
def career():
    return render_template('career.html')

# Reminder Page
@app.route('/reminder')
def reminder():
    return render_template('reminder.html')

# Books & Lectures
@app.route('/books')
def books():
    return render_template('books.html')

# Current Affairs
@app.route('/affairs')
def affairs():
    return render_template('affairs.html')

if __name__ == '__main__':
    app.run(debug=True)