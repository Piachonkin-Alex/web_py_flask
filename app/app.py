import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, render_template
from library import return_Articles

app = Flask(__name__)

our_articles = return_Articles()


@app.route('/')
def start_page():
    return render_template('index.html')


@app.route('/about')
def go_about():
    return render_template('about.html')


@app.route('/articles')
def go_articles():
    return render_template('articles.html', our_articles=our_articles)


@app.route('/article/<string:id>/')
def go_article(id):
    return render_template('article_data.html', id=str(id))


if __name__ == '__main__':
    app.run(debug=True)
