from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Marcos", "email": "teste@teste.com"}
    posts = [
        {"author": {"name": "Luiza"}, "title": "How to read a book in english",
         "body": "Reading a book in english is better than reading a book in english.",
         "created": "12/06/2024"},
        {"author": {"name": "Marcos"}, "title": "How can i say this sentences in english?",
         "body": "Reading a book in english is better than reading a book in english.", "created": "12/06/2024"},
        {"author": {"name": "Antonio"}, "title": "How to make new friends?",
         "body": "Reading a book in english is better than reading a book in english.", "created": "08/09/2024"}
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    print(form.errors)
    print(form.data)
    print(form.remember_me)
    if form.validate_on_submit():
        print("is login successful?")
        flash(f"Login requested for {form.username} remember_me={form.remember_me.data}")
        return redirect("/index")
    return render_template("login.html", title="Login", form=form)
