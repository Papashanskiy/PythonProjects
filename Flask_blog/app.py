from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import os, datetime


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'post.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):                               # DB model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    sub_title = db.Column(db.String(128))
    author = db.Column(db.String(64), index=True)
    date_post = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Author: {self.author}, post title: {self.title}>'


@app.route('/')                                     # View functions
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/addpost', methods=['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']

        post = Post(title=title, sub_title=subtitle, author=author, content=content, date_post=datetime.datetime.now())

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        flash('<h1>Something came wrong</h1>')
        return redirect(url_for('index'))


@app.errorhandler(404)                             # Error handlers
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
