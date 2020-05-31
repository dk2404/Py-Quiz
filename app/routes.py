from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User,Question
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
# @login_required
def index():
    user = {'username': 'Sonali'}
    posts = [
        {
            'author': {'username': 'Sonali'},
            'body': 'Currently socially iselated'
        },
        {
            'author': {'username': 'Dilip'},
            'body': 'Six seasons and a Netflix special'
        }
    ]
    return render_template('intro.html', title = 'Home', posts = posts,question_level=question_level, Question=Question)


@app.route('/login',methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:

        return redirect(url_for('login'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username = form.username.data).first()

        if user is None or not user.check_password(form.password.data):

            flash("Incorrect password")

            return redirect(url_for('login'))

        login_user(user, remember = form.remember_me.data)

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            
            return redirect(url_for('index'))

        return redirect(next_page)

    return render_template('login.html', title = "Sign in", form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:

        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("You've registered! Please Sign In")

        return redirect(url_for('login'))

    return render_template('register.html', title = "Register", form = form)

@app.route('/about')
def about():
    return render_template('about.html', title = "about")

@app.route('/dilip')
def dilip():
    return render_template('dilip.html', title ="dilip")

@app.route('/add_question')
def add_question():
    print("USER NAME: " + current_user.username)
    if current_user.is_authenticated and current_user.username == 'admin':
        return render_template('add_question.html')
    return render_template("restricted.html")

@app.route('/sonali')
def sonali():
    return render_template('sonali.html',title ="dilip")

@app.route('/test')
def test():
    return render_template('test.html',title="test")

@app.route('/feedback')
def feedback():
    return render_template('feedback.html',title="test")
