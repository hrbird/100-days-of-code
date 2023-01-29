# NATO Alphabet Program
# Converts a given word or message in English to the NATO alphabet.

from os.path import dirname, join
import pandas

def convert_nato(input_str, nato_dict):
    """Convert a given string into the NATO alphabet."""
    input_str = input_str.strip().upper()

    # For each alphabetic character in the input string, 
    # get its NATO code and add that to a new list.
    nato_letters = ""
    for letter in input_str:
        if letter.isalpha():
            try:
                # Add the NATO code.
                nato_letters += " " + nato_dict[letter]
            except KeyError:
                # If the user entered letters that are not found in the NATO dictionary,
                # print an error message and return an empty string.
                print(f"Sorry, the letter {letter} was not found in the NATO dictionary.\n")
                return ""
        else:
            # If the user sent in a non-alphabetic character (like numbers or punctuation),
            # simply add it to the new list.
            nato_letters += letter

    # Return the string.
    return nato_letters.lstrip()

def main():

    # Get the file path of the NATO alphabet CSV file.
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./nato_alphabet.csv")

    # Load the contents of the file into a panda DataFrame.
    try:
        nato_df = pandas.read_csv(file_path)
    except FileNotFoundError:
        print("Error: Could not find file at: {file_path}")
    else:
        # Create a NATO dictionary from the dataframe.
        # Keys = english letters, Values = NATO codes
        nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

        # Get input from user to convert into the NATO alphabet.
        print("\nWelcome to the English to NATO Alphabet Converter.")

        quit_program = False
        while not quit_program:

            input_str = input("\nEnter a message to convert (or Q to quit):\n> ").strip().upper()

            if input_str == "Q":
                print("\nGoodbye!\n")
                quit_program = True
            else:
                nato_str = convert_nato(input_str, nato_dict)
                
                if len(nato_str) > 0:
                    print(f"\nYour message spelled out in the NATO alphabet is:\n{nato_str}\n")

            print("-" * 50)

if __name__ == "__main__":
    main()