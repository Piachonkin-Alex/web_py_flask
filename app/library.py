# /usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
import json


class Article():  ## класс статьи
    def __init__(self):
        self.id = None
        self.title = ""
        self.text = ""
        self.authors = ""

    def fill_fields(self, id, title, text, authors):
        self.id = id  ## заполнение полей
        self.title = title
        self.text = text
        self.authors = authors


def read_articles(file_: str, articles):  ## считывание с файла
    with open(file_, 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        article = Article()
        args = [data[i]['id'], data[i]['title']]
        args += [data[i]['text'], data[i]['authors']]
        article.fill_fields(*args)
        articles.append(article)


def add_article(file, articles, text, id, title, authors) -> None:
    article = Article()  ## добавление статьи в список
    article.fill_fields(id, title, text, authors)
    articles.append(article)
    data = []
    for i in range(len(articles)):
        dict_ = {'id': articles[i].id, 'title': articles[i].title}
        dict_.update({'authors': articles[i].authors, 'text': articles[i].text})
        data.append(dict_)  ## запись в файл
        with open(file, 'w') as f:
            json.dump(data, f)


def change_article(file_, articles, new_text, id: int, new_title, new_authors) -> None:
    articles[int(id)].text = new_text  ## изменение статьи
    articles[id].authors = new_authors
    articles[id].title = new_title
    data = []
    for i in range(len(articles)):
        dict_ = {'id': articles[i].id, 'title': articles[i].title}
        dict_.update({'authors': articles[i].authors, 'text': articles[i].text})
        data.append(dict_)  ## запись в файл
        with open(file_, 'w') as f:
            json.dump(data, f)
