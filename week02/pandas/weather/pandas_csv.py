# Opens the weather.csv file and reads the data into the program using the pandas library.

from os.path import dirname, join
import pandas

# Get the file path of the weather csv file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./weather.csv")

# Load the contents of the file into a panda DataFrame.
data = pandas.read_csv(file_path)
print(data)

# Get the overall average temp.
if len(data) > 0:
    dates = data["date"].to_list()
    overall_avg_temp = data["avg_temp"].mean()

    print(f"\nThe overall average temperature from {dates[0]} to {dates[-1]} was {overall_avg_temp:.2f} degrees F.\n")


# Play around with Pandas DataFrame methods...

# DataFrame.head() shows a given number of rows at the top.
print(f"Head (5 rows):\n{data.head(5)}\n")

# DataFrame.tail() shows a given number of rows at the bottom.
print(f"Tail (3 rows):\n{data.tail(3)}\n")

# DataFrame.index shows the range index (start, stop, and step).
print(f"Index:\n{data.index}\n")

# DataFrame.columns shows the column names.
print(f"Columns:\n{data.columns}\n")

# DataFrame.describe() shows a quick statistic summary of any numerical data.
# This includes the count, mean, std (standard deviation), min, 25%, 50%, 75%, and max.
print(f"Describe:\n{data.describe()}\n")

# DataFrame.T shows the data transposed so the rows and columns are switched.
print(f"Transposed:\n{data.T}\n")

# DataFrame.sort_values()) sorts the data by the given column.
print(f"Sorted:\n{data.sort_values(by='avg_temp')}\n")

# DataFrame["column_x"] gets the data series for the column named "column_x".
print(f"Average Temps Series:\n{data['avg_temp']}\n")

# DataFrame[a:b] selects a slice of rows from a:b (including a, excluding b).
print(f"Slice Rows:\n{data[10:15]}\n")

# DataFrame[DataFrame['A'] > 0] selects rows that meet a certain condition 
# (EG the values in column A are more than 0.)
# Here's an example of how to show all of the days with average temps below 30.
cold_bools = data['avg_temp'] < 30
print(f"Rows where average temp < 30:\n{data[cold_bools]}\n")

# Here's another example that shows the day that had the hottest average temperature.
max_temp = data['avg_temp'].max()
print(f"Day with the maximum average temp:\n{data[data['avg_temp'] == max_temp]}\n")

# DataFrame[DataFrame['A'].isin(my_list)] selects rows that have a value in a given list
# (EG the values in column A are in my_list.)
bad_weather = ['Snow', 'Foggy']
bad_weather_bools = data['condition'].isin(bad_weather)
print(f"Rows Where Weather Condition is Bad (Snow or Foggy):")
print(f"{data[bad_weather_bools]}\n")

# DataFrame.groupby() allows you to group by a given column (or columns).
# Here's an example using groupby() on condition, then count() on date.
grouped_weather = data.groupby(by='condition')
print(f"Number of days, grouped by weather condition:")
print(f"{grouped_weather['date'].count()}\n")

# Here's an example using groupby() on condition, then mean() on avg_temp.
grouped_weather = data.groupby(by='condition')
print(f"Average temp, grouped by weather condition:")
print(f"{grouped_weather['avg_temp'].mean()}\n")

# You can also iterate through groups.
# Here's an example using groupby() on condition, then showing each row.
grouped_weather = data.groupby(by='condition')
print(f"Each day's data, grouped by weather condition:")
for name, group in grouped_weather:
    print(name)
    print(group)
    print()

# DataFrame.to_dict() converts the DataFrame object into a regular Python dictionary.
# Each column is a key that contains a nested dictionary of the values in each row.
data_dict = data.to_dict()
print(f"Dictionary:\n{data_dict}\n")
d = 14
print(f"On {data_dict['date'][d]}, the average temperature was {data_dict['avg_temp'][d]} degrees, and it was {data_dict['condition'][d]}.\n")

# DataFrame['a'].to_list() converts a column/series of data into a regular Python list.
avg_temps = data['avg_temp'].to_list()
print(f"List of average temps:\n{avg_temps}\n")

# Parse dates when reading a CSV file into a DataFrame.
data_with_dates = pandas.read_csv(file_path, index_col=0, parse_dates=True)
print(data_with_dates)
print(data_with_dates.index)