
import db.noun_db as db
import db.schema as sc

import unittest


def fake_loader():
    return [
        {
            "english_word": "hi",
            "german_word": "hallo",
            "plural_word": "hallos",
            "article": "das"
        }, 
        {
            "english_word": "bye",
            "german_word": "tchüss",
            "plural_word": "tchüsses",
            "article": "die"
        }
    ]


class NounDBTestCase(unittest.TestCase):
    def setUp(self):
        self.config = db.ConfigNounDB()
        self.config.loader = fake_loader
        self.db = db.NounDB(self.config)

    def test_len(self) -> None:
        self.assertEqual(len(self.db), 2)

    def test_idx(self) -> None:
        self.assertEqual(self.db[0].article, "das")
        self.assertEqual(self.db[0].english_word, "hi")
        self.assertEqual(self.db[0].plural_word, "hallos")
        self.assertEqual(self.db[0].german_word, "hallo")

        self.assertEqual(self.db[1].article, "die")
        self.assertEqual(self.db[1].english_word, "bye")
        self.assertEqual(self.db[1].plural_word, "tchüsses")
        self.assertEqual(self.db[1].german_word, "tchüss")

    def test_sample(self) -> None:
        data = self.db.sample(1, seed=0)

        elem = next(data)
        self.assertEqual(elem.article, "die")
        self.assertEqual(elem.english_word, "bye")
        self.assertEqual(elem.plural_word, "tchüsses")
        self.assertEqual(elem.german_word, "tchüss")

        data = self.db.sample(2, seed=10)

        elem = next(data)
        self.assertEqual(elem.article, "das")
        self.assertEqual(elem.english_word, "hi")
        self.assertEqual(elem.plural_word, "hallos")
        self.assertEqual(elem.german_word, "hallo")

        elem = next(data)
        self.assertEqual(elem.article, "die")
        self.assertEqual(elem.english_word, "bye")
        self.assertEqual(elem.plural_word, "tchüsses")
        self.assertEqual(elem.german_word, "tchüss")