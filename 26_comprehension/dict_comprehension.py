"""
new_dict = {new_key: new_value for item in list}                list
new_dict = {new_key: new_value for (key, value) in dict.items()}                    dictionary

"""
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {student: random.randint(30, 100) for student in names}
print(student_score)

passed_students = {stud: sco for (stud, sco) in student_score.items() if
                   sco > 75}


print(passed_students)
