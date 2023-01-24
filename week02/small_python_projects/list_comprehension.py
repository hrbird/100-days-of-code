# Demonstrates list comprehension syntax for lists, strings, ranges, and dictionaries

# Take a list of numbers and create a new list of each of those numbers + 1.
old_list = [1, 5, 3, 8, 6, 2, 4, 9, 7, 0, -5]
new_list = [(n + 1) for n in old_list]
print(f"\nNumbers: {old_list}")
print(f"Numbers + 1: {new_list}\n")

# Create a list of even numbers using list comprehension.
evens_list = [n * 2 for n in range(1,21)]
print(f"Evens: {evens_list}\n")

# Get only the alphabetic characters from a string and add them to a letter,
# using list comprehension and a conditional statement.
name = "H1ea5ther7"
letters_list = [letter for letter in name if letter.isalpha()]
print(f"Original: {name}")
print(f"Letters only: {letters_list}\n")

# Get only the names in a list that have 4 or less characters and convert them to title case.
names_list = ["alex", "beth", "charlie", "dan", "eleanor", "freddy", "gwen", "heather"]
short_names = [name.title() for name in names_list if len(name) <= 4]
print(f"All names: {names_list}")
print(f"Short names: {short_names}\n")

# Square each number in a list.
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [n**2 for n in nums]
print(f"Numbers: {nums}")
print(f"Numbers squared: {squared_nums}\n")

# Get only the odd numbers in a list.
nums_mixed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums_odd = [n for n in nums_mixed if n % 2 != 0]
print(f"Mixed numbers: {nums_mixed}")
print(f"Odd numbers only: {nums_odd}\n")

# Get only the numbers that are in both lists.
list_a = [1, 2, 4, 6, 10, 12]
list_b = [0, 2, 5, 6, 7, 10, 15]
list_both = [n for n in list_a if n in list_b]
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Numbers in both: {list_both}\n")