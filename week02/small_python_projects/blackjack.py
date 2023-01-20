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

class Card:
    """Card class to represent each playing card."""
    def __init__(self, suit, symbol, rank, rank_short, value):
        self.suit = suit
        self.symbol = symbol
        self.rank = rank
        self.rank_short = rank_short
        self.value = value
        self.is_ace = (rank_short == "A")

    
    def __str__(self):
        """What to print if a Card object is treated as a string. EG 'Queen of Hearts'"""
        return f"{self.rank} of {self.suit}"

    def get_short_name(self):
        """Get the short representation of the card as a string. EG 'Q ♥'"""
        return f"{self.rank_short} {self.symbol}"

    def get_card_art(self):
        """Get ASCII art representation of the card.
        Returns a list of 4 strings for each row of the card."""
        rows = []

        rows.append(" ___ ")                    # Top line
        rows.append(f"|{self.rank_short:<3}|")  # Left-aligned rank
        rows.append(f"| {self.symbol} |")       # Suit symbol

        # Add right-aligned rank and bottom line.
        # All ranks have 1 character, except "10".
        if self.rank_short == "10":
            rows.append(f"|_{self.rank_short}|")
        else:
            rows.append(f"|__{self.rank_short}|")  

        return rows

    def get_card_art_mystery(self):
        """Get ASCII art representation of a mystery card,
        with ? replacing the rank and suit.
        Returns a list of 4 strings for each row of the card."""
        rows = []

        rows.append(" ___ ")    # Top line
        rows.append(f"|?  |")   # Left-aligned rank
        rows.append(f"| ? |")   # Suit symbol
        rows.append(f"|__?|")   # Left-aligned rank and bottom line

        return rows

class Deck:
    """Deck class to create and hold 52 playing cards."""
    def __init__(self):
        self.cards = []
        self.create_new_deck()
        self.shuffle_deck()

    def create_new_deck(self):
        """Creates a new deck of Cards."""

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

    def shuffle_deck(self):
        """Shuffle the cards."""
        random.shuffle(self.cards)
    
    def draw_card(self):
        """Draw a card and remove it from the deck."""
        return self.cards.pop()
        
class Hand:
    """Class to handle a hand of cards."""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a Card object to the hand."""
        self.cards.append(card)

    def __str__(self):
        """Return the hand of cards as a string."""
        
        hand_str = ""

        for c in self.cards:
            hand_str += c.get_short_name()
            hand_str += "   "

        return hand_str

    def show_hand(self):
        """Show the hand of cards as ASCII art."""
        lines = ["", "", "", ""]

        for c in self.cards:
            card_art = c.get_card_art()
            
            for a in range(len(card_art)):
                lines[a] += card_art[a] + "  "

        print(self.get_value_str())
        for l in lines:
            print(l)

    def show_init_dealer_hand(self):
        """Show initial dealer's hand, which only reveals the first of two cards."""
        lines = ["", "", "", ""]

        if len(self.cards) < 2:
            print("")
        else:
            # Get the first card art.
            card_art = self.cards[0].get_card_art()
            for a in range(len(card_art)):
                lines[a] += card_art[a] + "  "

            # Add the mystery card art.
            mystery_art = self.cards[1].get_card_art_mystery()
            for m in range(len(mystery_art)):
                lines[m] += mystery_art[m] + "  "

        print("(Current value: ??)")
        for l in lines:
            print(l)        

    def get_value(self):
        """Get total value of the cards.
        Returns an int total of the cards' value."""
        
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

    def get_value_str(self):
        """Get value as a formatted string."""
        return f"(Current value: {self.get_value()})"

def get_hit_or_stand():
    """Gets either "H" or "S" from the user and validates the answer.
    Returns either "H" for Hit or "S" for Stand."""
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

def getYN():
    """Gets either "Y" or "N" from the user and validates the answer.
    Returns either True for Y or False for N."""
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

def play_game():
    """Play a new game of blackjack."""

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
    dealer_hand.show_init_dealer_hand()

    # Show the player's cards to the player.
    print("\nYour starting hand:")
    player_hand.show_hand()

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
                player_hand.show_hand()

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
                dealer_hand.show_hand()

                # The dealer is obligated to keep Hitting until their cards value >= 17.
                while dealer_hand.get_value() < 17:
                    print("\nThe dealer Hits.")
                    dealer_hand.add_card(deck.draw_card())
                    dealer_hand.show_hand()

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


# Dealer's starting hand:
# (Current value: ??)
#  ___    ___
# |J  |  |?  |
# | ♦ |  | ? |
# |__J|  |__?|

# Your starting hand:
# (Current value: 13)
#  ___    ___
# |7  |  |6  |
# | ♣ |  | ♠ |
# |__7|  |__6|

# Enter either 'H' to Hit or 'S' to Stand.

# > h
# Hit

# Your current hand:
# (Current value: 14)
#  ___    ___    ___
# |7  |  |6  |  |A  |
# | ♣ |  | ♠ |  | ♦ |
# |__7|  |__6|  |__A|

# Enter either 'H' to Hit or 'S' to Stand.

# > s
# You choose to Stand.

# The dealer reveals their hand:
# (Current value: 14)
#  ___    ___
# |J  |  |4  |
# | ♦ |  | ♦ |
# |__J|  |__4|

# The dealer Hits.
# (Current value: 22)
#  ___    ___    ___
# |J  |  |4  |  |8  |
# | ♦ |  | ♦ |  | ♠ |
# |__J|  |__4|  |__8|

# The dealer Busts.
# You win!


# ==============================

# Would you like to play again? [Y/N]

# > n

# Goodbye!