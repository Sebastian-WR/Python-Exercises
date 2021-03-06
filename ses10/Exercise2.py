""" 
In this exercise you start out by having a list of names, and a list of majors.

Your job is to create:

A list of dictionaries of students (ie: students = [{‘id’: 1,’name’: ‘Claus’, ‘major’: ‘Math’}]), cretated in a normal function that returns the resul.

A Generator that “returns” a generator object. So the student is yield instead of returned.

Both functions should do the same, but one returns a list and one a generator object.

students = [{‘id’: 1,’name’: ‘Clasu’, ‘major’: ‘Math’}]
The id could be generated by a counter or like in a loop.
The Name should be found by randomly chosing a name from the names list
The Major should be found by randomly chosing a major from the major list """
import random


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    id = 0
    stud_list = []
    while(id <= num_students):
        rname = random.randint(0, 5)
        rmajor = random.randint(0, 4)
        stud = { 'id': id + 1, 'name': names[rname], 'major': majors[rmajor] }
        stud_list.append(stud)
        id += 1
    return stud_list
        

def students_generator(num_students):
    id = 0
    while(id <= num_students):
        rname = random.randint(0, 5)
        rmajor = random.randint(0, 4)
        stud = { 'id': id + 1, 'name': names[rname], 'major': majors[rmajor] }
        id += 1
        yield stud

people = students_list(10)
for stu in people:
    print(stu)
people1 = students_generator(10)
for stu in people:
    print(stu)