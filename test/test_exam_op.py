
import db_op.schema as sc
import exam_op as exam

import unittest


class ExamTestCase(unittest.TestCase):
    def setUp(self):
        self.noun = sc.NounSchema(
            english_word="hi",
            german_word="hallo",
            plural_word="hallos",
            article="das",
        )
        self.no_plural = sc.NounSchema(
            english_word="hi",
            german_word="hallo",
            plural_word="<None>",
            article="das",
        )
        
    def test_noun_question(self) -> None:
        question = exam.noun_question(self.noun)

        self.assertEqual(question.title, f"Translate the word: hi")
        self.assertListEqual(
            question.parts, ["word", "article", "plural"]
        )

    def test_noun_no_plural_question(self) -> None:
        question = exam.noun_question(self.no_plural)

        self.assertEqual(question.title, f"Translate the word: hi")
        self.assertListEqual(
            question.parts, ["word", "article"]
        )

    def test_one_answer_incorrect(self) -> None:
        result = exam.noun_check_answer(
            self.noun, {
                "word": "hallo", "plural": "hallos", "article": "die"
            }
        )

        self.assertTrue(result.german_is_correct)
        self.assertTrue(result.plural_is_correct)
        self.assertFalse(result.article_is_correct)
        self.assertEqual(result.points, 2)
        self.assertEqual(result.noun, self.noun)
        self.assertFalse(result.all_correct())

    def test_two_answer_incorrect(self) -> None:
        result = exam.noun_check_answer(
            self.noun, {
                "word": "hallos", "plural": "hallos", "article": "die"
            }
        )

        self.assertFalse(result.german_is_correct)
        self.assertTrue(result.plural_is_correct)
        self.assertFalse(result.article_is_correct)
        self.assertEqual(result.points, 1)
        self.assertEqual(result.noun, self.noun)
        self.assertFalse(result.all_correct())

    def test_all_answer_correct(self) -> None:
        result = exam.noun_check_answer(
            self.noun, {
                "word": "hallo", "plural": "hallos", "article": "das"
            }
        )

        self.assertTrue(result.german_is_correct)
        self.assertTrue(result.plural_is_correct)
        self.assertTrue(result.article_is_correct)
        self.assertEqual(result.points, 3)
        self.assertEqual(result.noun, self.noun)
        self.assertTrue(result.all_correct())

    def test_all_answer_correct_no_plural(self) -> None:
        result = exam.noun_check_answer(
            self.no_plural, {
                "word": "hallo", "article": "das"
            }
        )

        self.assertTrue(result.german_is_correct)
        self.assertTrue(result.plural_is_correct)
        self.assertTrue(result.article_is_correct)
        self.assertEqual(result.points, 3)
        self.assertEqual(result.noun, self.no_plural)
        self.assertTrue(result.all_correct())