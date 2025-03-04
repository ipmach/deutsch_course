
from db_op.noun_db import NounDB
import exam_op as exam

import random

seed = random.randint(0, 1000)

db = NounDB()
print(f"Start with seed {seed}")
for elem in db.sample(len(db), seed=seed):

    print("#######################################")
    question = exam.noun_question(elem) 
    print(question.title)

    answer = {}
    for task in question.parts:
        answer[task] = input(f"  - {task}: ")

    print("")
    print(exam.noun_check_answer(elem, answer=answer))
    print("#######################################")

    
