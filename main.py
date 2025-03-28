
from db_op.noun_db import NounDB
import exam_op as exam

import random

seed = random.randint(0, 1000)

db = NounDB()

try:
    print(f"Start with seed {seed}")
    for j, elem in enumerate(db.sample(len(db), seed=seed)):

        is_correct = False 
        while not is_correct:
            print("#######################################")
            print(f"[{j + 1}/{len(db)}] ", end="")
            question = exam.noun_question(elem) 
            print(question.title)

            answer = {}
            skip = False
            for task in question.parts:
                input_ = "" if skip else input(f"  - {task}: ") 
                if input_ == "nächste":
                    skip = True
                answer[task] = input_ 
                
            print("")
            print(results := exam.noun_check_answer(elem, answer=answer))
            print("#######################################")
            is_correct = results.all_correct()

except KeyboardInterrupt:
    print("Test interrupt")
finally:
    print("Finish")