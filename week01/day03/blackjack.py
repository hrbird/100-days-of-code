# Blackjack Project

import random

LOGO_ART = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


############### Our Blackjack House Rules #####################

## Each game begins with a full, shuffled deck.
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1 (however best benefits the player).
## Cards are removed from the deck as they are drawn.
## The computer is the dealer.
## There is no betting or tracking multiple games.

# Card class to represent each playing card.
class Card:
    def __init__(self, suit, symbol, rank, rank_short, value):
        self.suit = suit
        self.symbol = symbol
        self.rank = rank
        self.rank_short = rank_short
        self.value = value
        self.is_ace = (rank_short == "A")

    # What to print if a Card object is treated as a string. EG "Queen of Hearts"
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # Get the short representation of the card as a string. EG "Q ♥"
    def getShortName(self):
        return f"{self.rank_short} {self.symbol}"


# Deck class to create and hold 52 playing cards.
class Deck:
    def __init__(self):
        self.cards = []
        self.create_new_deck()
        self.shuffle_deck()

    # Creates a new deck of Cards.
    def create_new_deck(self):

        suits = {
            "Hearts": "♥", 
            "Diamonds": "♦", 
            "Clubs": "♣", 
            "Spades": "♠"
        }

        ranks = {
            "1": ["One", 1], 
            "2": ["Two", 2], 
            "3": ["Three", 3], 
            "4": ["Four", 4], 
            "5": ["Five", 5], 
            "6": ["Six", 6], 
            "7": ["Seven", 7], 
            "8": ["Eight", 8], 
            "9": ["Nine", 9], 
            "10": ["Ten", 10], 
            "J": ["Jack", 10], 
            "Q": ["Queen", 10], 
            "K": ["King", 10], 
            "A": ["Ace", 1]
        }

        self.cards = []

        # Generate each card and add it to the deck.
        for s in suits:
            for r in ranks:
                c = Card(suit=s, symbol=suits[s], rank=ranks[r][0], rank_short=r, value=ranks[r][1])
                self.cards.append(c)

    # Shuffle the cards.
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    # Draw a card and remove it from the deck.
    def draw_card(self):
        return self.cards.pop()
        
class Hand:
    def __init__(self):
        self.cards = []

    # Add a Card object to the hand.
    def add_card(self, card):
        self.cards.append(card)

    # Return the hand of cards as a string.
    def __str__(self):
        
        hand_str = ""

        for c in self.cards:
            hand_str += c.getShortName()
            hand_str += "   "

        return hand_str

    # Show initial dealer's hand, which only reveals the first of two cards.
    def show_init_dealer_hand(self):
        
        if len(self.cards) > 0:
            return f"{self.cards[0].getShortName()}   ??"
        else:
            return ""

    # Get total value of the cards.
    # Returns an int total of the cards' value.
    def get_value(self):
        
        total_value = 0
        num_aces = 0

        for c in self.cards:
            if c.is_ace:
                # Aces can either be considered 1 or 11, so handle them last.
                num_aces += 1

            else:
                total_value += c.value
            
        # Aces have a value of either 11 or 1 as needed to reach 21 without busting.
        # Therefore, only count an ace as an 11 if it does not bring the total over 21.
        # (You would never count two aces as an 11, since that would be 22.)
        # Possible ace values:
        #   - 1 ace: either 11 or 1
        #   - 2 aces: either 12 (11 + 1) or 2
        #   - 3 aces: either 13 (11 + 2) or 3
        #   - 4 aces: either 14 (11 + 3) or 4
        if num_aces > 0:
            if (total_value + 10 + num_aces) <= 21:
                total_value += 10 + num_aces
            else:
                total_value += num_aces
            
        return total_value

    # Get value as a formatted string.
    def get_value_str(self):
        return f"(Current value: {self.get_value()})"

# Gets either "H" or "S" from the user and validates the answer.
# Returns either "H" for Hit or "S" for Stand.
def get_hit_or_stand():
    while True:

        # Get input from user.
        # Strip it of whitespace and grab the first character.
        ans = input(f"\n> ").strip()

        if len(ans) == 0:
           print(f"Oops, you did not enter a letter. Please enter H or S..")

        elif ans[0].upper() == "H":
            return "H"

        elif ans[0].upper() == "S":
            return "S"

        else:
            print(f"Oops, I can't accept {ans}. Please enter H or S...")

# Gets either "Y" or "N" from the user and validates the answer.
# Returns either True for Y or False for N.
def getYN():
    while True:

        # Get input from user.
        # Strip it of whitespace and grab the first character.
        ans = input(f"\n> ").strip()

        if len(ans) == 0:
           print(f"Oops, you did not enter a letter. Please enter Y or N...")

        elif ans[0].upper() == "Y":
            return True

        elif ans[0].upper() == "N":
            return False

        else:
            # If the input is not acceptable, tell the player and keep looping.
            print(f"Oops, I can't accept {ans}. Please enter Y or N...")

# Play a new game of blackjack.
def play_game():

    print(LOGO_ART)

    # Create a shuffled deck.
    deck = Deck()

    # Deal two cards to the dealer.
    dealer_hand = Hand()
    dealer_hand.add_card(deck.draw_card())
    dealer_hand.add_card(deck.draw_card())

    # Deal two cards to the player.
    player_hand = Hand()
    player_hand.add_card(deck.draw_card())
    player_hand.add_card(deck.draw_card())

    # Show only one of the dealer's cards to the player.
    print("\nDealer's starting hand:")
    print(dealer_hand.show_init_dealer_hand())
    print(f"(Current value: ??)")

    # Show the player's cards to the player.
    print("\nYour starting hand:")
    print(player_hand)
    print(player_hand.get_value_str())

    # If the player gets 21 in their first two cards, they automatically win.
    if player_hand.get_value() == 21:
        print("\Blackjack!\nYou win!")

    else:

        # Loop until the player's turn is over.
        is_game_over = False
        while not is_game_over:

            # Ask the player if they wish to Hit or Stand.
            print("\nEnter either 'H' to Hit or 'S' to Stand.")

            ans = get_hit_or_stand()

            if ans == "H":
                print("Hit")

                # Give another card to the player.
                player_hand.add_card(deck.draw_card())

                # Show the player's cards to the player.
                print("\nYour current hand:")
                print(player_hand)
                print(player_hand.get_value_str())

                # Check if the player has Busted (gone over 21).
                # If so, the player automatically loses.
                if player_hand.get_value() > 21:
                    print("\nBust!\nSorry, you lose.")
                    is_game_over = True

            elif ans == "S":
                print("You choose to Stand.")

                # Now it's the dealer's turn.
                # Get the value of the dealer's hand.
                print("\nThe dealer reveals their hand:")
                print(dealer_hand)
                print(dealer_hand.get_value_str())

                # The dealer is obligated to keep Hitting until their cards value >= 17.
                while dealer_hand.get_value() < 17:
                    print("\nThe dealer Hits.")
                    dealer_hand.add_card(deck.draw_card())
                    print(dealer_hand)
                    print(dealer_hand.get_value_str())

                # If the dealer's hand is above 21, they lose.
                # Otherwise, whoever has the highest hand wins.
                player_value = player_hand.get_value()
                dealer_value = dealer_hand.get_value()
                if dealer_value > 21:
                    print("\nThe dealer Busts.\nYou win!")
                elif player_value == dealer_value:
                    print("\nPush!\nYou tie with the dealer.")
                elif player_value > dealer_value:
                    print("\nYou are closer to 21.\nYou win!")
                else:
                    print("\nThe dealer is closer to 21.\nSorry, you lose.")

                is_game_over = True

            else:
                print(f"Error: Cannot parse {ans}.")
                is_game_over = True


    print("\n")

def main():
    quit_game = False
    while not quit_game:

        play_game()

        print("==============================")

        print("\nWould you like to play again? [Y/N]")

        if not getYN():
            print("\nGoodbye!\n")
            quit_game = True

main()

#################
# SAMPLE OUTPUT #
#################
#
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
#       |  \/ K|                            _/ |
#       `------'                           |__/
#
#
# Dealer's starting hand:
# 9 ♠   ??
# (Current value: ??)
#
# Your starting hand:
# K ♦   7 ♠
# (Current value: 17)
#
# Enter either 'H' to Hit or 'S' to Stand.
#
# > s
# You choose to Stand.
#
# The dealer reveals their hand:
# 9 ♠   6 ♣
# (Current value: 15)
#
# The dealer Hits.
# 9 ♠   6 ♣   Q ♠
# (Current value: 25)
#
# The dealer Busts.
# You win!
#
# ==============================
#
# Would you like to play again?
# > n
#
# Goodbye!