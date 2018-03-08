from flask import request, render_template
from index import app, db
from models import Post


@app.route('/')
def hello_world():
    return 'Flask is working'


@app.route('/hello')
def new_route():
    return 'Routes are working too '


@app.route('/posts', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
