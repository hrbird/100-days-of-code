# Hacking game inspired by the computer-hacking minigames 
# in Fallout: New Vegas.
#
# The computer shows some memory banks filled with random
# characters and a few seven-letter words.
#
# The player must guess which word is the secret password.
# Each time they guess a word, the computer says how many 
# letters in the guessed word match the true password.
#
# A matching letter must also be in the same position in this
# word as in the password.
#
# FOR EXAMPLE:
# The secret password is MONITOR and the user guesses CONTAIN.
# MONITOR
# CONTAIN
#  XX
# The user is told that 2/7 letters are correct.
# The user then guesses the word CONQUER.
# MONITOR
# CONQUER
#  XX   X
# The user is told that 3/7 letters are correct.
# The user then guesses the word MONIKER.
# MONITOR
# MONIKER
# XXXX  X
# The user is told that 5/7 letters are correct.


import random, sys
from os.path import dirname, join

# Constants
GARBAGE_CHARS = "!@#$%^&*()_-+=~\{\}[]|;:,.<>?/"
WORDS_FILENAME = "./seven_letter_words.txt"

HACKER_ART = '''
88                                   88                              
88                                   88                              
88                                   88                              
88,dPPYba,   ,adPPYYba,   ,adPPYba,  88   ,d8   ,adPPYba,  8b,dPPYba,  
88P'    "8a  ""     `Y8  a8"     ""  88 ,a8"   a8P_____88  88P'   "Y8  
88       88  ,adPPPPP88  8b          8888[     8PP"""""""  88          
88       88  88,    ,88  "8a,   ,aa  88`"Yba,  "8b,   ,aa  88          
88       88  `"8bbdP"Y8   `"Ybbd8"'  88   `Y8a  `"Ybbd8"'  88          
'''

class WordManager:
    """The WordManager class handles getting the list of 
    words for each game."""
    def __init__(self, file_name):
        self.ALL_WORDS = []     # List to hold 7-letter words
        self.game_words = []    # List to hold the words for the game.
        self.password = ""      # The correct secret password to win the game.
        self.total_words = 12   # How many words to get.
        self.max_tries = 1000   # The number of times to try finding a word before giving up.
        self.file_name = file_name # Name of the text file with all the words.
        self.num_guesses = 4    # The number of password guesses the player can make.

        self.import_word_list()

    def import_word_list(self):
        """Read each 7-letter word from the given txt file into the WORDS list.
        Args:
            file_name (str): relative file path and name of txt file
        """

        # Get the file path of the list of 7-letter words.
        current_dir = dirname(__file__)
        file_path = join(current_dir, self.file_name)

        # Load the list of 7-letter words from a text file.
        with open(file_path, "r") as word_list_file:
            self.ALL_WORDS = word_list_file.readlines()

        # Clean each word in the list by removing whitespace/newlines
        # and converting them to all uppercase.
        for w in range(len(self.ALL_WORDS)):
            self.ALL_WORDS[w] = self.ALL_WORDS[w].strip().upper()

    def get_random_word_except(self, block_list = None):
        """Returns a random word from ALL_WORDS that isn't in the
        given block_list.

        Args:
            block_list (list of strings, optional): the words to exclude
        """
        if block_list == None:
            block_list = []

        # Get a random word.
        # If it's not in the block list, return it.
        # Otherwise, keep trying to get a word.
        for i in range(self.max_tries):
            random_word = random.choice(self.ALL_WORDS)
            if random_word not in block_list:
                return random_word

    def count_matching_letters(self, word1, word2):
        """Counts the number of letters that match in both words.
        The letter must be in the same position in both words to count.

        Args:
            word1 (string): the first word to check
            word2 (string): the second word to check

        Returns the int number of letters that match.
        """
        num_matches = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                num_matches += 1
        return num_matches

    def get_match(self, num_matches):
        """Get a random word that has a given number of letters that
        match the current secret password (and is not already in game_words).

        Args:
            num_matches (int): the number of letters to match the password

        Returns the matching word, or an empty string if none was found.
        """

        # Look for a random word that meets the given conditions in ALL_WORDS.
        # Give up after 1000 tries.
        for i in range(self.max_tries):
            random_word = self.get_random_word_except(self.game_words)
            if self.count_matching_letters(self.password, random_word) == num_matches:
                return random_word

        return ""

    def get_match_list(self, num_matches, num_words):
        """Get a list of random words that have a given number of letters that
        match the given secret password (and are not already in game_words).

        Args:
            num_matches (int): the number of letters to match the password
            num_words (int): the number of words of this criteria to get
        """
        words = []
        for w in range(num_words):
            new_word = self.get_match(num_matches)
            if len(new_word) > 0:
                words.append(new_word)

        #print(f"{len(words)} words with {num_matches} matches: {words}")

        return words

    def get_game_words(self):
        """Fill game_words with a list of random words from the ALL_WORDS list."""

        # The secret password will be the first word in the list.
        self.password = random.choice(self.ALL_WORDS)
        self.game_words = [self.password]
        #print(f"The secret password is: {self.password}")

        # To make the game fair, we need to ensure that there are words 
        # with a range of matching numbers of letters as the secret word.
        fairness_matrix = [
            [0, 2], # Find 2 words with zero letters that match the password
            [1, 2], # Find 2 words with 1 letter that matches the password
            [2, 3], # Find 3 words with 2 letters that match the password
            [3, 2], # Find 2 words with 3 letters that match the password
            [4, 1], # Find 1 word with 4 letters that match the password
            [5, 1]  # Find 1 word with 5 letters that match the password
        ]

        # Get the new words that match the criteria and add them to the game_words list.
        for f in fairness_matrix:
            new_words = self.get_match_list(f[0], f[1])
            self.game_words.extend(new_words)

        # Fill out the rest of the list with random words, if needed.
        num_words_left = self.total_words - len(self.game_words)
        for w in range(num_words_left):
            new_word = self.get_random_word_except(self.game_words)
            self.game_words.append(new_word)

        #print(f"game words: {self.game_words}")
        #print(f"length: {len(self.game_words)}")
    
    def get_memory_bank_string(self, num_chars, word=""):
        """Returns a line of the given number of random garbage characters.
        If a word is given, it is inserted at random inside the string.

        Args:
            word (str, optional): String word to hide in the memory bank,
            if any. Defaults to an empty string.
        """

        line_str = ""
        for c in range(num_chars):
            line_str += random.choice(GARBAGE_CHARS)

        if len(word) > 0:
            # If a word is given, insert it at a random index in the line.
            i = random.randint(0, num_chars - len(word))

            # Insert the word.
            line_str = (line_str[:i] + word + line_str[i + 7:])

        return line_str

    def get_hex_address_string(self, memory_address):
        """Returns a formatted string similar to a hex memory bank address.

        Args:
            memory_address (int): the memory address, as an integer
        """
        hex_address = hex(memory_address)[2:].zfill(4)
        return f"0x{hex_address}"

    def get_memory_banks_string(self):
        """Return a string representing the "computer memory banks".
        The possible passwords are hidden in the data."""

        # If the game_words haven't been created yet, return an empty string.
        if len(self.game_words) != self.total_words:
            return ""

        # Shuffle the possible passwords.
        shuffled_words = self.game_words
        random.shuffle(shuffled_words)
        
        # 16 is a reoccuring number in this code, since old computers
        # had 16-bit (2-byte) memory banks (link MS-DOS).
        # There will be 16 lines in total, split into two half-lines (32 total).
        # There will be 16 characters per half-line, representing each memory address.

        # Choose which lines will contain a word.
        lines_with_words = random.sample(range(16 * 2), len(self.game_words))
        
        # Get a random starting "memory address" number, for flavor text.
        # Make it a multiple of 16, to seem more hex.
        memory_address = 16 * random.randint(1, 4000)

        # Create the "computer memory" text.
        # Start with a list of 16 strings, one for each line.
        computer_memory = []

        cur_word_index = 0 # Track where we are in shuffled_words list

        for line_num in range(16):
            # Create two half-lines of garbage characters.
            left_half = ""
            right_half = ""
            
            # If this half-line should have a word in it, 
            # add the next word from the shuffled_words list at a random place.
            # Else, fill the entire half-line with garbage characters.
            if line_num in lines_with_words:
                left_half = self.get_memory_bank_string(16, shuffled_words[cur_word_index])
                cur_word_index += 1
            else:
                left_half = self.get_memory_bank_string(16)

            # Do the same with the right half-line.
            if (line_num + 16) in lines_with_words:
                right_half = self.get_memory_bank_string(16, shuffled_words[cur_word_index])
                cur_word_index += 1
            else:
                right_half = self.get_memory_bank_string(16)

            # Add the whole line to the computer_memory list.
            hex_address_a = self.get_hex_address_string(memory_address)
            hex_address_b = self.get_hex_address_string(memory_address + (16*16))
            
            line_str = f"{hex_address_a}  {left_half}    {hex_address_b}  {right_half}"
            computer_memory.append(line_str)

            # Go to the next "computer memory" address.
            memory_address += 16

        # Join all the strings into one string with newlines.
        return "\n".join(computer_memory)

    def get_guess(self):
        """Asks user to guess one of the passwords.
        Keeps looping until the user enters an acceptable word in game_words.
        Returns a string."""
        ans = ""
        while True:
            ans = input("> ").upper().replace(" ", "")

            if ans not in self.game_words:
                print(f"Sorry, '{ans}' is not an acceptable answer.")
                print("Please enter one of the passwords listed above.")
            else:
                return ans

    def play_game(self):
        """Play a single game of Hacking."""

        print(HACKER_ART)

        print("Find the correct password hidden in the computer's memory.")
        print("After each guess, you will be told how many letters you got right.")
        print(f"You get {self.num_guesses} attempts before you are locked out.\n")

        self.get_game_words()

        print(self.get_memory_banks_string())
        print()

        num_tries_left = self.num_guesses
        is_game_over = False
        while not is_game_over:

            # Ask the user for their guess.
            print(f"Enter the password ({num_tries_left} tries remaining):")
            guess = self.get_guess()

            # Check if it's the correct password.
            if guess == self.password:
                print("\nA C C E S S   G R A N T E D\n")
                is_game_over = True
            else:
                # Get the number of matching letters.
                num_matches = self.count_matching_letters(self.password, guess)
                print(f"Access Denied ({num_matches}/7 correct)\n")
                num_tries_left -= 1

            # If user runs out of guesses, end the game.
            if num_tries_left <= 0:
                print(f"Out of tries. The secret password was {self.password}.\n")
                is_game_over = True


def main():
    word_manager = WordManager(WORDS_FILENAME)
    
    # Run a single game.
    word_manager.play_game()

if __name__ == "__main__":
    main()
