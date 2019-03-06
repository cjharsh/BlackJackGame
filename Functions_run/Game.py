from HandChips.Chips import Chips
from HandChips.Hand import Hand
from CardDeck.Deck import deck,Card
playing = True
def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry please provide an integer<100 ')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cant exceed',chips.total)
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.addjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print('Sorry I didnt understand that, enter h or s only')
            continue
        break


def player_busts(player,dealer,chips):
    print('Bust Player')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print('Player Wins')
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print('Player wins, dealer busted')
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()


def tie():
    print('Dealer and player tie! Push')


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

while True:
    # print an opening msg
    print("Lets play BlackJack Game")
    deck = deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips() #set the chip for the player
    take_bet(player_chips) #sets the bet

    #see some of the cards
    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value> 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            tie()
    print("\nPlayer's total is: {0} ".format(player_chips.total))

    # Lets play again
    new_game = input('Would you like to play again')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break











