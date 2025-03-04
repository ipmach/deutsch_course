from dataclasses import dataclass


@dataclass
class NounSchema:
    english_word: str
    german_word: str
    plural_word: str
    article: str