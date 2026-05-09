from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/affairs')
def affairs():
    return render_template('affairs.html')

if __name__ == '__main__':
    app.run(debug=True)