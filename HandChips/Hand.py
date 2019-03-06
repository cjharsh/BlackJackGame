from CardDeck.Deck import deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand:
    '''
    for holding Card objects dealt from the Deck,
    the Hand class may be used
    to calculate the value of those cards using the values dictionary defined above.
    It may also need to adjust for the value of Aces when appropriate.
    '''

    def __init__(self):
        self.cards = []  # to hold the cards from the deck
        self.value = 0
        self.aces = 0



    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def addjust_for_ace(self):
        # If total value > 21 and I still have an Ace
        # Than Change THe ace to be a 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1






