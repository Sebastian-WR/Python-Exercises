class P:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self) -> str:
        return self.name

    def __len__(self):
        return

    def __add__(self, other):
        return P(self.name + ' ' + other.name)

class Deck:

    def __init__(self):
        self.cards = ['A', 'K', 4, 7]
    
    def __repr__(self) -> str:
        return f'{self.__dict__}'
    
    def __str__(self) -> str:
        return str(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __add__(self, other):
        return self.cards.append(other)

    def __setitem__(self, key, val):
        self.cards[key] = val
        return self.cards
    
    def __delitem__(self, key):
        del self.cards[key]
        return  self.cards
    
    def __len__(self):
        return len(self.cards)

deck = Deck()
deck1 = Deck()
print(len(deck))
deck.__add__(7)
print(deck)
deck + 1
print(deck)
deck.__setitem__(2, 5)
print(deck)
deck[2] = 11
print(deck)
deck.__delitem__(-1)
print(deck)
deck + deck1
print(deck)
