
import db_op.schema as sc
import typing as t
import random


class ConfigNounDB:
    loader = None


class NounDB:
    def __init__(self, config: ConfigNounDB = ConfigNounDB()) -> None:
        self.config = config
        self.__load_data()
    
    def __load_data(self) -> None:
        self.__list = []
        for elem in self.config.loader():
            self.__list.append(sc.NounSchema(**elem))

    def __len__(self) -> int:
        return len(self.__list)
    
    def __getitem__(self, idx: int) -> sc.NounSchema:
        return self.__list[idx]

    def sample(self, n: int, seed: int = 0) -> t.Iterator[sc.NounSchema]:
        for i in range(n):
            random.seed(seed + i)
            yield self[random.randint(0, len(self) - 1)]