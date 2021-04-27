""" Based on the Student class below, create a PythonStudents class that acts as a collection of students. 
The class should implement the iterations functionality (iter() and next()) and be able to return an iter object.
When iterated the Pythod_students object should return the name of each student in the list. """

class PythonStudents:

    def __init__(self, *args):
        self.last = 0
        self.students = list(args)

    def __iter__(self): # always self in class method
        return self

    def __next__(self):
        if self.last >= len(self.students):
            raise StopIteration
        stud = self.students[self.last]
        self.last += 1
        return stud.name



class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
        return f'{self.__dict__}'

Lotte = Student('Lise', 9090900090)
Peter = Student('Paul', 8080080808)
Connie = Student('Egon', 9090)

listen = PythonStudents(Lotte, Peter, Connie)

test = iter(listen)

for stud in listen: 
    print(stud)
    print(next(test))