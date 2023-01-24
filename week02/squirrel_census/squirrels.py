# Opens the squirrel_data.csv file and reads the data into the program using the pandas library. 
# Specifically, this program counts the number of squirrels for each primary fur color.

from os.path import dirname, join
import pandas

# Get the file path of the weather csv file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./squirrel_data.csv")

# Load the contents of the file into a panda DataFrame.
data = pandas.read_csv(file_path)

# ===================================================================================
# Group by Primary Fur Color
# ===================================================================================

# Group the data by Primary Fur Color.
grouped_primary_fur = data.groupby(by=["Primary Fur Color"])

# Count the number of squirrels in each Primary and Highlight Fur Color category.
primary_fur_counts = grouped_primary_fur['Unique Squirrel ID'].count()

print("\nNumber of Squirrels per Primary Fur Color:\n")
print(f"{primary_fur_counts.sort_values(ascending=False, ).to_string()}\n")

# ===================================================================================
# Group by Primary Fur Color and Highlight Fur Color
# ===================================================================================

# Group the data by Primary Fur Color.
grouped_highlight_fur = data.groupby(by=["Primary Fur Color", "Highlight Fur Color"])

# Count the number of squirrels in each Primary and Highlight Fur Color category.
highlight_fur_counts = grouped_highlight_fur['Unique Squirrel ID'].count()

print("\nNumber of Squirrels per Primary and Highlight Fur Color:\n")
print(f"{highlight_fur_counts.sort_values(ascending=False).to_string()}\n")

# ===================================================================================
# Alternatively...
# ===================================================================================

# Get the count of squirrels for each fur color.
num_gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
num_cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

# Create a new dictionary (keys are header names, values are lists with an element for each row).
fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray_squirrels, num_cinnamon_squirrels, num_black_squirrels]
}

# Convert the dictionary into a DataFrame.
df = pandas.DataFrame(fur_dict)
print(df)
