import random
class Cards:


    def __init__(self, letter, number):
        self.letter = letter
        self.number = number

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
oneDigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

card = Cards('A', 4)
card2 = Cards('I', 4)
card3 = Cards('C', 5)
card4 = Cards('E', 4)



cardList = [card, card2, card3, card4]

def cardCheck(list, vowels):
    for i in list:
        if i.letter in vowels and (i.number % 2 != 0):
            return False
    return True

def cardGen(number):
    for i in range(number):
        randLet = random.choice(alphabet)
        randNum = random.choice(oneDigits)
        newCard = Cards(randLet, randNum)
        yield newCard

cardList2 = [i for i in cardGen(4)]

# cardList2 = cardGen(4)

for i in cardList2:
    print(i.letter, i.number)

print(cardCheck(cardList2, vowels))
