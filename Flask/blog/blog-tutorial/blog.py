from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from .db import get_db
from .auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute('SELECT p.id, title, body, created, author_id, username'
                       ' FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC').fetchall()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        print("estamos por aqui")
        print(title)
        print(body)
        if not title:
            error = 'title is required'
        if error is not None:
            flash(error)
        else:
            print('-- SALVANDO NO BANCO --')
            db = get_db()
            db.execute('INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)', (title, body, g.user['id']))
            db.commit()

            print("-- salvo com sucesso --")
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


def get_post(id, check_author=True):
    print("chamando get_post com id ", id)
    post = (
        get_db()
        .execute(
            'SELECT p.id, title, body, created, author_id, username'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' WHERE p.id = ?',
            (id,),
        )
        .fetchone()
    )
    print("finalizando a consulta no banco com o post", post["title"])
    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    post = get_post(id)
    print("post retornado")
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if not title:
            error = 'Title is required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('UPDATE post SET title = ?, body = ? WHERE id = ?', (title, body, id))
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)


@bp.route('/<int:id_post>/delete', methods=['POST'])
@login_required
def delete_post(id_post):
    get_post(id_post)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id_post,))
    db.commit()
    return redirect(url_for('blog.index'))
