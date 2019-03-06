class Chips():
    '''
    we need to keep track of a Player's starting chips, bets, and ongoing winnings.
    This could be done using global variables,
    but in the spirit of object oriented programming, let's make a Chips class instead!
    '''

    def __init__(self,total=100):
        self.total = total
        # this can also be given by the user
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


