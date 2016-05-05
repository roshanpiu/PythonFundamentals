import random

class Die(object):

    def __init__(self, sides):
        self.sides = sides
    
    def roll(self): 
        return random.randint(1, self.sides)
        
class Deck(object):
    
    def shuffle(self):  
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(suit+ " of "+ rank) 
                
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

class Greeter(object):
    
    def __init__(self, name):
        self.name = name
    
    #self is a pointer to the class
    def greet(self):
        print("Hello" + self.name)
    
    def goodBye(self):
        print("Goodbye" + self.name)

g = Greeter("Roshan")
g.greet()
g.goodBye()

g2 = Greeter("Piumal")
g2.greet()
g2.goodBye()

d = Die(6)
print(d.roll())
print(d.roll())

d = Die(20)
print(d.roll())
print(d.roll())

d = Deck()
d.shuffle()
print(d.deal())
print(d.deal() )