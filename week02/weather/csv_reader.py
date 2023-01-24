# Opens the weather.csv file and reads the data 
# into the program using the csv library. 
# Specifically, this program gets the average 
# temperature for each day in the file and 
# calculates the overall average temperature.

from os.path import dirname, join
import csv

# Get the file path of the weather csv file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./weather.csv")

# Load the contents of the file into DATA.
with open(file_path, "r") as data_file:
    DATA = csv.reader(data_file)

    # Store all data for the average daily temps in this list.
    avg_temps = []

    # Get the data from column 4, excluding the header row.
    avg_temp_index = 2
    for row in DATA:
        if row[avg_temp_index] != "avg_temp":
            avg_temps.append(float(row[avg_temp_index]))

    # Calculate the overall average temperature.
    overall_avg_temp = sum(avg_temps) / len(avg_temps)
    print(f"The overall average temperature was {overall_avg_temp:.2f} degrees F.")

