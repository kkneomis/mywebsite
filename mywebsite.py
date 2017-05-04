import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('index.html', posts=get_posts()[-3:])

@app.route("/404/")
def not_found():
    return render_template('error.html')

def get_posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=False)
    return posts

@app.route("/posts/")
def posts():
    return render_template('posts.html', posts=get_posts())

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)

    # getting the next and previous posts
    links = {}
    posts = get_posts()
    index = posts.index(post)
    next = index + 1
    previous = index - 1
    if next < len(posts):
        links['next'] = posts[next]
    if previous >= 0:
        links['previous'] = posts[previous]

    return render_template('post.html', post=post, links=links)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)