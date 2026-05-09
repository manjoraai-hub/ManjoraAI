import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'manjora_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'


# =========================
# DATABASE MODEL
# =========================

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(100))

    progress = db.Column(db.Integer, default=0)


# =========================
# LOAD USER
# =========================

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():

    return render_template('index.html')


# =========================
# REGISTER
# =========================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')

        password = request.form.get('password')

        user = User(
            username=username,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


# =========================
# LOGIN
# =========================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')

        password = request.form.get('password')

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:

            login_user(user)

            return redirect(url_for('dashboard'))

    return render_template('login.html')


# =========================
# LOGOUT
# =========================

@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('login'))


# =========================
# DASHBOARD
# =========================

@app.route('/dashboard')
@login_required
def dashboard():

    return render_template(
        'dashboard.html',
        username=current_user.username,
        progress=current_user.progress
    )


# =========================
# UPDATE PROGRESS
# =========================

@app.route('/update_progress/<int:value>')
@login_required
def update_progress(value):

    current_user.progress = value

    db.session.commit()

    return redirect(url_for('dashboard'))


# =========================
# PLANNER
# =========================

@app.route('/planner')
@login_required
def planner():

    return render_template('planner.html')


# =========================
# CAREER
# =========================

@app.route('/career')
@login_required
def career():

    return render_template('career.html')


# =========================
# BOOKS
# =========================

@app.route('/books')
@login_required
def books():

    return render_template('books.html')


# =========================
# LIVE CURRENT AFFAIRS
# =========================

@app.route('/affairs')
@login_required
def affairs():

    api_key = "6e564400a1884b29933d7db73feaa739"

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])

    return render_template(
        'affairs.html',
        articles=articles
    )


# =========================
# CREATE DATABASE
# =========================

with app.app_context():

    db.create_all()


# =========================
# RUN APP
# =========================

if __name__ == '__main__':

    app.run(debug=True)import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'manjora_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'


# =========================
# DATABASE MODEL
# =========================

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(100))

    progress = db.Column(db.Integer, default=0)


# =========================
# LOAD USER
# =========================

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():

    return render_template('index.html')


# =========================
# REGISTER
# =========================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')

        password = request.form.get('password')

        user = User(
            username=username,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


# =========================
# LOGIN
# =========================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')

        password = request.form.get('password')

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:

            login_user(user)

            return redirect(url_for('dashboard'))

    return render_template('login.html')


# =========================
# LOGOUT
# =========================

@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('login'))


# =========================
# DASHBOARD
# =========================

@app.route('/dashboard')
@login_required
def dashboard():

    return render_template(
        'dashboard.html',
        username=current_user.username,
        progress=current_user.progress
    )


# =========================
# UPDATE PROGRESS
# =========================

@app.route('/update_progress/<int:value>')
@login_required
def update_progress(value):

    current_user.progress = value

    db.session.commit()

    return redirect(url_for('dashboard'))


# =========================
# PLANNER
# =========================

@app.route('/planner')
@login_required
def planner():

    return render_template('planner.html')


# =========================
# CAREER
# =========================

@app.route('/career')
@login_required
def career():

    return render_template('career.html')


# =========================
# BOOKS
# =========================

@app.route('/books')
@login_required
def books():

    return render_template('books.html')


# =========================
# LIVE CURRENT AFFAIRS
# =========================

@app.route('/affairs')
@login_required
def affairs():

    api_key = "6e564400a1884b29933d7db73feaa739"

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])

    return render_template(
        'affairs.html',
        articles=articles
    )


# =========================
# CREATE DATABASE
# =========================

with app.app_context():

    db.create_all()


# =========================
# RUN APP
# =========================

if __name__ == '__main__':

    app.run(debug=True)