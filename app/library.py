# /usr/bin/env python
# -*- coding: utf-8 -*-
class Article():
    def __init__(self):
        self.id = None
        self.title = ""
        self.generate_data = ""
        self.text = ""
        self.authors = ""


def return_Articles():
    articles = []
    for i in range(1, 4):
        article = Article()
        article.id = i
        article.title = "Статья " + str(i)
        article.text = 'Article'
        article.generate_data = "28.04.2020"
        article.authors = "Alex"
        articles.append(article)
    return articles
