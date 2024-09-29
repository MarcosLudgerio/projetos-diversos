from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from urllib.parse import urlparse


@app.route("/")
@app.route("/index")
@login_required
def index():
    posts = [
        {"author": {"name": "Luiza"}, "title": "How to read a book in english",
         "body": "Reading a book in english is better than reading a book in english.",
         "created": "12/06/2024"},
        {"author": {"name": "Marcos"}, "title": "How can i say this sentences in english?",
         "body": "Reading a book in english is better than reading a book in english.", "created": "12/06/2024"},
        {"author": {"name": "Antonio"}, "title": "How to make new friends?",
         "body": "Reading a book in english is better than reading a book in english.", "created": "08/09/2024"}
    ]
    return render_template("index.html", title="Home", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        print('--- VERIFICANDO USER AUTHENTICADO ---')
        return redirect(url_for('index'))

    form = LoginForm()
    print('--- gerando o form login ---')
    print(form.username.data)
    print(form.password.data)
    print(form.validate_on_submit())
    print('---------------------')
    if form.validate_on_submit():
        print("---- CONSULTANDO DADOS NO BANCO ----")
        user = User.query.filter_by(username=form.username.data).first()
        print(f'--- usuario validado {user} ---')
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    print("--- finalizando o processo ---")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
