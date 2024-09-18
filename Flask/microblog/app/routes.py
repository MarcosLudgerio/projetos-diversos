from flask import render_template
from app import app


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
    return render_template("indexw.html", title="Home", user=user, posts=posts)
