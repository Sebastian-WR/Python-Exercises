class Person:
   # pass #lader en lave en tom class ellers ville den komme med fejl

    species = 'Mammel' # class variable
    # self skal altid være først i metode header, sådan er det bare når det er OOP i guess
    def __init__(self, name): # hvis man laver en metode nedunder denne med samme navn så overider den bare den øverste
        self.name = name # 'Sebastian' # instance variable

    #def __init1__(self, *args): # *args er tuple så her kan man skrive så meget man vil i parametre og så skriver den dem ud i tuple
       # self.arguments = args
        

    def name_age(self):
        return self.name + " " + str(self.age)

p = Person('Christopher')
#p1 = Person('Christopher', 12, 1234) her for eksempel virker det med tuple

#print(p1.arguments)
print(p.name)
print(p.species)
print(p.__dict__) # dictionary
p.name = 'Tykke-Lars'
print(p.name)
p.age = 12 # man kan bare smide flere ting på objectet bare sån
print(p.__dict__)
Person.species = 'Retard' # ændre class variable 
print(p.species)
print(p.name_age())
print(ord('*')) #værdi af *
print(chr(42)) # teg tilhørende værdien 42 i ASCII måske eller hex eller hvad det hedder :O

class Instructor:
    def __init__(self, course):
        self.course = course

class Student(Person, Instructor): # tager fra superklassen som nu er person i tilfældet af to superklasser, så er super metoden i student den sidste klasse

    def __init__(self, name, course):
        # super().__init__(name) # kalder super init metode som er constructor med variable name som den skal bruge en 
        Person.__init__(self, name) # når to implementeres i calss header så skal man kalde dem som disse to 
        Instructor.__init__(self, course)

student = Student('Lars', 'ITP')
print(student.name + " " + student.course)

def __repr__(self): #formal representation
    return f'{self.name}'

def __str__(self): #informal representation lav disse som toStrings 
    return f'{self.name}'
