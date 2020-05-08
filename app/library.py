# /usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any
import json


class Article():
    def __init__(self):
        self.id = None
        self.title = ""
        self.text = ""
        self.authors = ""


articles = []


def read_articles(articles):
    with open('data.json', 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        article = Article()
        article.id = data[i]['id']
        article.title = data[i]['title']
        article.text = data[i]['text']
        article.authors = data[i]['authors']
        articles.append(article)


def add_article(articles, text: str, id: int, title: str, authors: str) -> None:
    article = Article()
    article.id = id
    article.title = title
    article.text = text
    article.authors = authors
    articles.append(article)
    data = []
    for i in range(len(articles)):
        data.append({'id': articles[i].id, 'title': articles[i].title, 'authors': articles[i].authors, 'text':
            articles[i].text})
        with open('data.json', 'w') as f:
            json.dump(data, f)


def change_article(articles, new_text: str, id: int, new_title: str, new_authors: str) -> None:
    articles[id].text = new_text
    articles[id].authors = new_authors
    articles[id].title = new_title
