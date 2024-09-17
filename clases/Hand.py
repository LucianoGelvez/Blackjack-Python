# from .deck import Deck
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
            'Queen':10, 'King':10, 'Ace':11}
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # card passed in
        # from Deck.deal() --single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
            self.value += 1
    
    def adjust_for_ace(self):
        #IF TOTAL VALUE > 10 AND STILL HAVE AN ACE
        #THAN CHANGE MY ACE  TO BE 1 INSTED OF AN 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
        pass

