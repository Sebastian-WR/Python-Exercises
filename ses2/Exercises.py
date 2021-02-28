#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
#'Hello World Huston we are here' -> 'World Huston we'

# opgave 1 Slicing
s = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
s2 = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
print(s)
print(s[1:])
print(s[:2])
print(s[4:])
print(s[4:5])
print(s[::2])
print(s[::-1])
print(s[1:4])

#opgave 2 Sort a text
str = 'abcdefghijklmnopqrstuvxyz'
str1 = 'Christoffer har meget lange løg altså hans klunker'

def removeVowelAndSort(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', ' ')
    for i in s:
        if i in vowels:
            s = s.replace(i, "")
    print(sorted(s))

removeVowelAndSort(str)
removeVowelAndSort(str1)

#opgave 3 Sort a list
str3 = ['Adolf', 'Askepot', 'Snehvide', 'Balbot', 'Christopher', 'Dværge', 'Heks']

def sortLast(s):
    return s[-1]

def sortA(s):
    noA = []
    lotsOfA = []
    for i in s:
        if 'a' in i:
            lotsOfA.append(i)
            lotsOfA = sorted(lotsOfA)
        elif 'A' in i:
            lotsOfA.append(i)
            lotsOfA = sorted(lotsOfA)
        else:
            noA.append(i)
            noA = sorted(noA)
    fullList = lotsOfA + noA
    print(fullList)


print(sorted(str3))
print(sorted(str3, reverse=True))
print(sorted(str3, key=len))
print(sorted(str3, key=sortLast))
sortA(str3)

#opgave 4 Files read write
f = open('lyrics.txt', 'w')
s = open('songs.docx', 'w')
s.write('Op med håret\nAaa aaa aaa aaa\nVi siger op med håret')
s = open('songs.docx')
print(s.read())
s = open('songs.docx')
print(s.readline())
s = open('songs.docx')
print(s.readlines())

#Opgave 5 Sort a list of tuples

tuplesUnsorted = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
print(sorted(tuplesUnsorted))
tuplesSorted = sorted(tuplesUnsorted, key=lambda tup: (tup[1], tup[0]))
print(tuplesSorted)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[4::-2])