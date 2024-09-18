
from clases.card import Card
from clases.chip import Chips
from clases.hand import Hand
from clases.deck import Deck


playing = True
player_chips = None
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s: ")
        if x[0].lower() == "h":
            hit(deck, hand)
        elif x[0].lower() == "s":
            print("Player Stand Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s")
            continue
        break

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

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and player tie! Push")

player_chips = Chips()
while True:

    if player_chips is None or player_chips.total <= 0:
        player_chips = Chips()
        print(f"Starting with {player_chips.total} chips.")

    else:
        print(f"Welcome to the Blackjack Python")
        print(f"You have {player_chips.total} chips.")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    take_bet(player_chips)
    
    show_some(player_hand, dealer_hand)
    
    while playing:
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand, dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
    
        show_all(player_hand, dealer_hand)
    
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    
    print("\nPlayer total chips are at: {}".format(player_chips.total))
    
    
    new_game = input("Would you like to play another hand? (y/n): ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break

# if __name__ == "__main__"
    