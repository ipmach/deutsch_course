from dataclasses import dataclass


class FileFields:
    in_english: str = "english"
    in_german: str = "german"
    in_plural: str = "plural"
    in_article: str = "article"

    out_english: str = "english_word"
    out_german: str = "german_word"
    out_plural: str = "plural_word"
    out_article: str = "article"


@dataclass
class NounSchema:
    english_word: str
    german_word: str
    plural_word: str
    article: str