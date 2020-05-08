import sys

from flask import Flask, render_template, request, redirect
from library import Article, read_articles, add_article, change_article

app = Flask(__name__)

our_articles = []
read_articles(our_articles)


@app.route('/about')
def go_about():
    return render_template('about.html')


@app.route('/articles')
def go_articles():
    return render_template('articles.html', our_articles=our_articles)


@app.route('/article/', methods=['GET', 'POST'])
def go_article():
    if request.method == 'POST':
        change_article(our_articles, request.args['text'], request.args['id'], request.args['title'],
                       request.args['authors'])
        return render_template('article_data.html', id=request.args['id'], text=request.args['text'],
                               author=request.args['author'], title=request.args['title'])
    return render_template('article_data.html', id=request.args['v1'], text=request.args['v2'],
                           author=request.args['v3'], title=request.args['v4'])


@app.route('/new_article', methods=['GET', 'POST'])
def create_new_article():
    return render_template('article_page.html', id=request.args['id'], text=request.args['text'],
                           author=request.args['author'], title=request.args['title'])


@app.route('/edit_article', methods=['GET', 'POST'])
def edit_article():
    if request.method == 'POST':
        return render_template('article_edit_page', id=request.args['id'], text=request.args['text'],
                               author=request.args['author'], title=request.args['title'])


@app.route('/', methods=['POST'])
def start_menu():
    if request.method == 'POST':
        add_article(our_articles, request.form['article'], len(our_articles), request.form['ArticleName'],
                    request.form['AuthorName'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
