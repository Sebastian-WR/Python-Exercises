### Exercise 1 ###
# Model an organisation of employees, management and board of directors in 3 sets.
#
# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
#
# Management: Tine, Trunte, Rane
#
# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

# who in the board of directors is not an employee?
print ("who in the board of directors is not an employee?")
directorButNotEmployeeSet = directors.difference(employees)
print(directorButNotEmployeeSet)

# who in the board of directors is also an employee?
print("who in the board of directors is also an employee?")
directorAndEmployeeSet = directors.intersection(employees)
print(directorAndEmployeeSet)

# how many of the management is also member of the board?
#                                                    ^ assuming this means a director
print("how many of the management is also member of the board?")
managementAndDirectorSet = management.intersection(directors)
print(managementAndDirectorSet)

# (are) All members of the managent also an employee?
# not exactly sure that the exercise is but I think he wants me to use "issubset"
print("# (are) All members of the managent also an employee?")
print(management.issubset(employees))

# All members of the management also in the board?
# same as above
print("# All members of the management also in the board?")
print(management.issubset(directors))

# Who is an employee, member of the management, and a member of the board?
print("# Who is an employee, member of the management, and a member of the board?")
tineSet = directors.intersection(management,employees)
print(tineSet)

# Who of the employee is neither a memeber or the board or management?
print("# Who of the employee is neither a memeber or the board or management?")
onlyEmployeeSet = employees.difference(directors, management)
print(onlyEmployeeSet)

### Exercise 2 ###
# Using a list comprehension create a list of tuples from the folowing datastructure
print("# Using a list comprehension create a list of tuples from the folowing datastructure")
letterDict = { 
    "a": "Alpha", 
    "b" : "Beta", 
    "g": "Gamma"
}

listOfTuples = [(k, v) for k, v in letterDict.items()] 
print(listOfTuples)

### Exercise 3 ###
# From these 2 sets:
englishSet = {'a', 'e', 'i', 'o', 'u', 'y'}
danishSet = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Of the 2 sets create a:
# Union
print("# Union")
print(englishSet.union(danishSet))

# Symmetric difference
print("#Symmetric difference")
print(englishSet.symmetric_difference(danishSet))

# Difference
print("#Difference")
print(danishSet.difference(englishSet))

# disjoint
print("# disjoint")
print(englishSet.intersection(danishSet))

### Exercise 4 ###
# date decoder
# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
# Create a dict suitable for decoding month names to numbers.

monthDict = { 
    "JAN" : 1,
    "FEB" : 2,
    "MAR" : 3,
    "APR" : 4,
    "MAY" : 5,
    "JUN" : 6,
    "JUL" : 7,
    "AUG" : 8,
    "SEP" : 9,
    "OCT" : 10,
    "NOV" : 11,
    "DEC" : 12
}

# Create a function which uses string operations to split the date into 3 items using the "-" character.
def splitStringfunc (date) :
    return date.split("-")

# Translate the month, correct the year to include all of the digits.
# The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
print("# Translate the month, correct the year to include all of the digits.")

def translateDate(date) :
    dateTuple = splitStringfunc(date)

    # adding year first
    # as we dont know if date is before or after year 2000 I assume we should just add "19" before the year
    dateList = ["19" + dateTuple[2]] 

    #append month number from dict
    dateList.append(monthDict[dateTuple[1]])

    #add date number
    dateList.append(dateTuple[0])

    return tuple(dateList)

print(translateDate("8-MAR-85"))
print(translateDate("25-DEC-96"))