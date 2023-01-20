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

class WordManager:
    """The WordManager class handles getting the list of 
    words for each game."""
    def __init__(self, file_name):
        self.ALL_WORDS = []     # List to hold 7-letter words
        self.game_words = []    # List to hold the words for the game.
        self.total_words = 12   # How many words to get.
        self.max_tries = 1000   # The number of times to try finding a word before giving up.
        self.file_name = file_name # Name of the text file with all the words.

        self.get_word_list()


    def get_word_list(self):
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

    def get_match(self, secret_password, num_matches):
        """Get a random word that has a given number of letters that
        match the given secret password (and is not already in game_words).

        Args:
            secret_password (string): the secret password for the game
            num_matches (int): the number of letters to match the password

        Returns the matching word, or an empty string if none was found.
        """

        # Look for a random word that meets the given conditions in ALL_WORDS.
        # Give up after 1000 tries.
        for i in range(self.max_tries):
            random_word = self.get_random_word_except(self.game_words)
            if self.count_matching_letters(secret_password, random_word) == num_matches:
                return random_word

        return ""

    def get_match_list(self, secret_password, num_matches, num_words):
        """Get a list of random words that have a given number of letters that
        match the given secret password (and are not already in game_words).

        Args:
            secret_password (string): the secret password for the game
            num_matches (int): the number of letters to match the password
            num_words (int): the number of words of this criteria to get
        """
        words = []
        for w in range(num_words):
            new_word = self.get_match(secret_password, num_matches)
            if len(new_word) > 0:
                words.append(new_word)

        print(f"{len(words)} words with {num_matches} matches: {words}")

        return words

    def get_game_words(self):
        """Fill game_words with a list of random words from the ALL_WORDS list."""

        # The secret password will be the first word in the list.
        secret_password = random.choice(self.ALL_WORDS)
        print(f"The secret password is: {secret_password}")
        self.game_words = [secret_password]

        # First, find 2 words with zero letters that match the password.
        self.game_words.extend(self.get_match_list(secret_password, 0, 2))

        # Find 2 words with 1 matching letter.
        self.game_words.extend(self.get_match_list(secret_password, 1, 2))

        # Find 3 words with 2 matching letters.
        self.game_words.extend(self.get_match_list(secret_password, 2, 3))

        # Find 2 words with 3 matching letters.
        self.game_words.extend(self.get_match_list(secret_password, 3, 2))

        # Try to find 1 word with 4 matching letters.
        self.game_words.extend(self.get_match_list(secret_password, 4, 1))

        # Try to find 1 word with 5 matching letters.
        self.game_words.extend(self.get_match_list(secret_password, 5, 1))

        # Fill out the rest of the list with random words.
        num_words_left = self.total_words - len(self.game_words)
        for w in range(num_words_left):
            new_word = self.get_random_word_except(self.game_words)
            self.game_words.append(new_word)

        print(f"game words: {self.game_words}")
        print(f"length: {len(self.game_words)}")
    
    def play_game(self):
        self.get_game_words()

def start_game():
    """Run a single game of Hacking."""
    word_manager = WordManager(WORDS_FILENAME)
    word_manager.play_game()

def main():
    
    start_game()

if __name__ == "__main__":
    main()
