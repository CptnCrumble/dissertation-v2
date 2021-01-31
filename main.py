from data import *
import validation

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
    "PDQ3": 2,
    "PDQ4": 3,
    "PDQ5": 4,
    "PDQ6": 5,
    "PDQ7": None,
    "PDQ8": 0,
    "bad key": 234
}

p1 = Patient(1,"bloke", 1999, 2)

p1.add_pdq8(test_pdq8)
p1.add_pdq8(bad_pdq8)

print(p1.pdq8_scores)
print(len(p1.pdq8_scores))
x = validation.pdq8(test_pdq8)
y = validation.pdq8(bad_pdq8)
print(x)
print(y)