from data_patient import *
from data_validation import *
import logging

logging.basicConfig(
    filename='app.log', 
    filemode='a', 
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


test_pdq8 = {
    "pid": 1, 
    "ass_num": 0,
    "ass_date": "01/01/2021",
    "PDQ1": 0,
    "PDQ2": 1,
    "PDQ3": 2,
    "PDQ4": 3,
    "PDQ5": 4,
    "PDQ6": 5,
    "PDQ7": None,
    "PDQ8": 0,
}

bad_pdq8 = {
    "pid": 2, 
    "ass_num": 0,
    "ass_date": "01/01/2021",
    "PDQ1": 0,
    "PDQ2": 1,
    "PDQ33": 2,
    "PDQ4": 3,
    "PDQ5": 4,
    "PDQ6": 5,
    "PDQ7": None,
    "PDQ8": 0
}

p1 = Patient(1,"bloke", 1999, 2)

p1.add_pdq8(test_pdq8)
print('...')
p1.add_pdq8(bad_pdq8)

print(p1.pdq8_scores)
print(len(p1.pdq8_scores))
x = validate_pdq8(test_pdq8)
y = validate_pdq8(bad_pdq8)
print(x)
print(y)