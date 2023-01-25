# NATO Alphabet Program
# Converts a given word or message in English to the NATO alphabet.

from os.path import dirname, join
import pandas

# Get the file path of the NATO alphabet CSV file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./nato_alphabet.csv")

# Load the contents of the file into a panda DataFrame.
nato_df = pandas.read_csv(file_path)

# Create a NATO dictionary from the dataframe.
# Keys = english letters, Values = NATO codes
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Get input from user to convert into the NATO alphabet.
print("\nWelcome to the English to NATO Alphabet Converter.")
input_str = input("\nEnter a message to convert: ").strip().upper()

# For each alphabetic character in the input string, 
# get its NATO code and add that to a new list.
nato_letters = [nato_dict[l] for l in input_str if l.isalpha()]

# Convert the list into a string with codes separated by spaces.
nato_str = " ".join(nato_letters)
print(f"\nYour message spelled out in the NATO alphabet is:\n{nato_str}")