
import db_op.schema as sc
import typing as t
import random

import yaml


def load_yaml(self, path: str) -> t.Dict[str, str]:
    with open(path, 'r') as file:
        data = yaml.safe_load(file)["words"]

    fields = sc.FileFields()
    return [{
        fields.out_english: elem[fields.in_english],
        fields.out_article: elem[fields.in_article],
        fields.out_german: elem[fields.in_german],
        fields.out_plural: elem[fields.in_plural],
    } for elem in data]
 

class ConfigNounDB:
    loader = load_yaml
    path = "databases/noun.yaml"


class NounDB:
    def __init__(self, config: ConfigNounDB = ConfigNounDB()) -> None:
        self.config = config
        self.__load_data()
    
    def __load_data(self) -> None:
        self.__list = []
        for elem in self.config.loader(self.config.path):
            self.__list.append(sc.NounSchema(**elem))

    def __len__(self) -> int:
        return len(self.__list)
    
    def __getitem__(self, idx: int) -> sc.NounSchema:
        return self.__list[idx]

    def sample(self, n: int, seed: int = 0) -> t.Iterator[sc.NounSchema]:
        indices = list(range(len(self)))
        for i in range(n):
            random.seed(seed + i)
            idx = random.randint(0, len(indices) - 1) 
            position = indices[idx]
            indices.remove(position)            
            yield self[position]