from dataclasses import dataclass

import db_op.schema as sc
import typing as t


@dataclass
class NounResults:
    article_is_correct: bool = False
    german_is_correct: bool = False
    plural_is_correct: bool = False

    points: int = 0
    max_points: int = 3


@dataclass
class ExamQuestion:
    title: str
    parts: t.List[str]


def noun_question(elem: sc.NounSchema) -> ExamQuestion:
    return ExamQuestion(
        title=f"Translate the word: {elem.english_word}",
        parts=["word", "article", "plural"]
    )


def noun_check_answer(
    elem: sc.NounSchema, answer: t.Dict[str, str]
) -> NounResults:
    return NounResults(
        article_is_correct=(a := answer["article"] == elem.article),
        german_is_correct=(b := answer["word"] == elem.german_word),
        plural_is_correct=(c := answer["plural"] == elem.plural_word),
        points=int(a) + int(b) + int(c)
    )
    


