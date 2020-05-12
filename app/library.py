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
        article.fill_fields(data[i]['id'], data[i]['title'], data[i]['text'], data[i]['authors'])
        articles.append(article)


def add_article(file, articles: List, text: str, id: int, title: str, authors: str) -> None:
    article = Article()  ## добавление статьи в список
    article.fill_fields(id, title, text, authors)
    articles.append(article)
    data = []
    for i in range(len(articles)):
        data.append({'id': articles[i].id, 'title': articles[i].title, 'authors': articles[i].authors, 'text':
            articles[i].text})  ## запись в файл
        with open(file, 'w') as f:
            json.dump(data, f)


def change_article(file_, articles: List, new_text: str, id: int, new_title: str, new_authors: str) -> None:
    articles[int(id)].text = new_text  ## изменение статьи
    articles[id].authors = new_authors
    articles[id].title = new_title
    data = []
    for i in range(len(articles)):
        data.append({'id': articles[i].id, 'title': articles[i].title, 'authors': articles[i].authors, 'text':
            articles[i].text})  ## запись в файл
        with open(file_, 'w') as f:
            json.dump(data, f)
