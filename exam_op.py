from dataclasses import dataclass

import db_op.schema as sc
import typing as t


@dataclass
class NounResults:
    article_is_correct: bool = False
    german_is_correct: bool = False
    plural_is_correct: bool = False
    noun: sc.NounSchema =  None

    points: int = 0
    max_points: int = 3

    def __str__(self) -> str:
        msg = f"Result: {self.points}/{self.max_points}"
        if not self.article_is_correct:
            msg += f"\n Correct article -> {self.noun.article}"
        if not self.german_is_correct:
            msg += f"\n Correct word -> {self.noun.german_word}"
        if not self.plural_is_correct:
            msg += f"\n Correct plural -> {self.noun.plural_word}"

        return msg
    
    def all_correct(self) -> bool:
        return self.points == self.max_points
        

@dataclass
class ExamQuestion:
    title: str
    parts: t.List[str]


def noun_question(elem: sc.NounSchema) -> ExamQuestion:
    if elem.plural_word == "<None>":
        return ExamQuestion(
        title=f"Translate the word: {elem.english_word}",
        parts=["word", "article"]
    )

    return ExamQuestion(
        title=f"Translate the word: {elem.english_word}",
        parts=["word", "article", "plural"]
    )


def noun_check_answer(
    elem: sc.NounSchema, answer: t.Dict[str, str]
) -> NounResults:
    if elem.plural_word == "<None>":
        plural_correct = True
    else:
        plural_correct = answer["plural"] == elem.plural_word

    return NounResults(
        article_is_correct=(a := answer["article"] == elem.article),
        german_is_correct=(b := answer["word"] == elem.german_word),
        plural_is_correct=(plural_correct),
        points=int(a) + int(b) + int(plural_correct),
        noun=elem,
    )
    


