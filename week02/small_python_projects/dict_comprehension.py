# Demonstrates dictionary comprehension syntax:
# new_dict = {new_key:new_value for (key, value) in dict.items()}

import random

# Create a dictionary of the given students and random test scores.
names_list = ["alex", "beth", "charlie", "dan", "eleanor", "freddy", "gwen", "heather"]
student_scores = {student.title():random.randint(50, 100) for student in names_list}
print(f"\nStudent test scores:\n{student_scores}\n")

# Now get a dictionary of the students with passing scores.
passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}
print(f"Students who passed the test:\n{passed_students}\n")

# Another example: creates a dictionary from a list of words.
# Each word is a key and its value is the number of characters it has.
words = "What is the Airspeed Velocity of an Unladen Swallow?".split()
result = {word:len(word) for word in words}
print(f"===============================================\n")
print(f"Number of letters in each word:\n{result}\n")

# Another example: creates a new dictionary of temperatures in Fahrenheit,
# given a dictionary of temperatures in Celsius.
# Keys: weekdays, Values: the temperatures.
temps_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

temps_f = {weekday:(temp_c * 9/5 + 32) for (weekday, temp_c) in temps_c.items()}

print(f"===============================================\n")
print(f"Temperatures (C):\n{temps_c}\n")
print(f"Temperatures (F):\n{temps_f}\n")