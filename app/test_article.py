import library as lib
import json
import unittest

file_ = "test_data.json"


class TestArticleMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.articles = []
        article = [{'id': 0, 'title': 'prog', 'authors': 'sanches', 'text': 'Genius'}]
        with open(file_, 'w') as f:
            json.dump(article, f)

    def tearDown(self) -> None:
        with open(file_, 'w') as f:
            json.dump('', f)

    def test_read(self):
        lib.read_articles(file_, self.articles)
        self.assertEqual(1, len(self.articles))
        self.assertEqual('prog', self.articles[0].title)
        self.assertEqual(0, int(self.articles[0].id))
        self.assertEqual('Genius', self.articles[0].text)

    def test_add(self):
        lib.read_articles(file_, self.articles)
        lib.add_article(file_, self.articles, "new_txt", 1, "second article", "alex")
        self.assertEqual(2, len(self.articles))
        self.assertEqual('new_txt', self.articles[1].text)
        copy_articles = []
        lib.read_articles(file_, copy_articles)
        self.assertEqual(2, len(self.articles))

    def test_change(self):
        lib.add_article(file_, self.articles, "new_txt", 0, "article", "alex")
        self.assertEqual("article", self.articles[0].title)
        lib.change_article(file_, self.articles, "change_txt", 0, "new title", "Sasha")
        self.assertEqual("change_txt", self.articles[0].text)
        self.assertEqual("new title", self.articles[0].title)
        self.assertEqual("Sasha", self.articles[0].authors)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
