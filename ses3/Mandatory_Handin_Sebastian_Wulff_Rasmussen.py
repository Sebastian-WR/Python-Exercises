# 1: Model an organisation of employees, management and board of directors in 3 sets.

board = ['Benny','Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren']
management = ['Tine', 'Trunte', 'Rane']
employees = ['Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars']

# who in the board of directors is not an employee?
# who in the board of directors is also an employee?

def notEmployee(list1, list2):
    notIn = []
    totsIn = []
    for person in list1:
        if person in list2:
            totsIn.append(person)
        else:
            notIn.append(person)
    print("Theese people are only board and not employees: " + str(notIn))
    print("Theese people are also an employee: " + str(totsIn))

notEmployee(board, employees)

# how many of the management is also member of the board?

def alsoInTheBoard(list1, list2):
    notIn = []
    totsIn = []
    for person in list1:
        if person in list2:
            totsIn.append(person)
        else:
            notIn.append(person)
    return print(str(len(totsIn)) + ": " + totsIn[0])

alsoInTheBoard(management, board)

# All members of the managent also an employee

def alsoEmployee(list1, list2):
    result = all(person in list1 for person in list2)
    if result:
        print("Yes! all the people from management is also an employee!")
    else:
        print("No... sadly they're to fancy to also be an employee all of them")

alsoEmployee(employees, management)

# All members of the management also in the board?

def alsoBoardMember(list1, list2):
    result = all(person in list1 for person in list2)
    if result:
        print("Yes! all the people from management is also part of the board!")
    else:
        print("No... sadly they're not all good enough to be part of the board..")

alsoBoardMember(management, board)

# Who is an employee, member of the management, and a member of the board?

def alsoInTheBoard(list1, list2, list3):
    notIn = []
    totsIn = []
    for person in list1:
        if person in list2 and list3:
            totsIn.append(person)
        else:
            notIn.append(person)
    return print("Yes!: " + totsIn[0] + " is part of all the departments!")

alsoInTheBoard(employees, management, board)

# Who of the employee is neither a memeber or the board or management?

def notPartOfAll(list1, list2, list3):
    notIn = []
    totsIn = []
    for person in list1:
        if person in list2 and list3:
            totsIn.append(person)
        else:
            notIn.append(person)
    return print("Theese employees are not part of all departments" + str(notIn))

notPartOfAll(employees, management, board)

# 2: Using a list comprehension create a list of tuples from the folowing datastructure

oldList = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
tupList = [item for item in oldList.items()]
print(tupList)

# 3: From theese 2 sets:

list1 = {'a', 'e', 'i', 'o', 'u', 'y'}
list2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

Union = list1.union(list2)
print(Union)

symmetricDiff = list1.symmetric_difference(list2)
print(symmetricDiff)

diff = list1.difference(list2)
print(diff)

disJoint = list1.isdisjoint(list2)
print(disJoint)

# 4: Date Decoder 

dateDecoder = {
    "JAN": 1, 
    "FEB": 2, 
    "MAR": 3, 
    "APR": 4, 
    "MAJ": 5, 
    "JUN": 6, 
    "JUL": 7, 
    "AUG": 8, 
    "SEP": 9, 
    "OKT": 10, 
    "NOV": 11, 
    "DEC": 12       
}
strD = "8-MAR-85"

def dateDec(str, dateDecoders):
    splitTup = str.split("-")
    if int(splitTup[2]) > 21:
        splitTup[2] = 1900 + int(splitTup[2])
    else:
        splitTup[2] = 2000 + int(splitTup[2])
    tupTup = (splitTup[2], dateDecoders[splitTup[1]], int(splitTup[0]))
    return tupTup

print(dateDec(strD, dateDecoder))