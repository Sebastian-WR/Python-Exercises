#Exercise 1
#Create a list of capital letters in the english alphabet
#Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O 70 - 79 -- mangler at løse --

APLHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

numAplha = [chr(x) for x in range(65, 91)] # laver liste af chars fra unixcode værdi 65 - 90 som er A-Z store bogstaver
numaplha2 = [chr(x) for x in range(ord('A'), ord('Z') + 1)] # 2 måder at lave på
print(numAplha)
print(numaplha2)

withoutThe4 = [chr(x)for x in range(65, 91) if x != [70, 75, 80, 85]] # virker umiddelbart ikke
try2 = [chr(x)for x in range(65, 91) if x not in [70, 75, 80, 85]] # virker
print(withoutThe4)
print(try2)

try3 = [chr(x)for x in range(65, 91) if x not in [71, 73, 75, 77]] # det er hardcoded men måske bedre måde at gøre det på
try4 = [chr(x) if x%2 == 0 not in [70, 80] else '' for x in range(65, 91)] # ved ikke hvordan man kommer videre med en smart måde
print(try3)
print(try4)

#Exercise 2
#From 2 lists, using a list comprehension, create a list containing:
#[(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothes = [(i, j) for i in colors for j in sizes]
print(clothes)
sold_out = [('Black', 'm'), ('White', 's')]
clothes2 = [(i, j) for i in colors for j in sizes if (i,j) not in sold_out]
print(clothes2)

