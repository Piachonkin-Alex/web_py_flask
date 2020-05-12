import sys
import test_article
from flask import Flask, render_template, request, redirect
from library import Article, read_articles, add_article, change_article

app = Flask(__name__)

data_file = 'data.json'
our_articles = []
read_articles(data_file, our_articles)


@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def start_page():
    if request.method == 'POST':
        args = [data_file, our_articles, request.form['article']]
        args += [len(our_articles), request.form['ArticleName']]
        args += [request.form['AuthorName']]
        add_article(*args)
    return render_template('index.html')


@app.route('/about')
def go_about():  ## страничка о нас для красоты
    return render_template('about.html')


@app.route('/articles')
def go_articles():  ## страница сообственно созданных статей, они все выложены в список
    return render_template('articles.html', our_articles=our_articles)


@app.route('/article', methods=['GET', 'POST'])
def go_article():  ## при клике на статью мы видим все содержимое
    if request.method == 'POST':
        args = [data_file, our_articles, request.form['article']]
        args += [int(request.args['id']), request.form['ArticleName']]
        args += [request.form['AuthorName']]
        change_article(*args)
        ## еще мы можем сюда попасть при изменении статьи. поэтому тут и меняем ее
        kwargs = {'id': int(request.args['id']), 'text': request.form['article']}
        kwargs.update({'author': request.form['AuthorName']})
        kwargs.update({'title': request.form['ArticleName']})
        return render_template('article_data.html', **kwargs)
    kwargs = {'id': request.args['v1'], 'text': request.args['v2']}
    kwargs.update({'author': request.args['v3'], 'title': request.args['v4']})
    return render_template('article_data.html', **kwargs)


@app.route('/new_article', methods=['GET', 'POST'])
def create_new_article():  ## страничка новой статьи
    return render_template('article_new.html')


@app.route('/edit_article', methods=['GET', 'POST'])
def edit_article():
    if request.method == 'GET':
        ## страничка редактирования. в принципе, почти тоже самое, что и новое, но с заполненными полями
        kwargs = {'id': request.args['id'], 'text': request.args['text']}
        kwargs.update({'authors': request.args['authors'], 'title': request.args['title']})
        return render_template('article_edit.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True)
