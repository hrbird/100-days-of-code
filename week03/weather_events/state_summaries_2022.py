# Displays storm event data for the US in 2022 using the pandas library.

from os.path import dirname, join
import pandas

# Get the file path of the StormEvents_2022 CSV file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./StormEvents_2022.csv")

# Load the contents of the file into a panda DataFrame.
DATA = pandas.read_csv(file_path)

# ===========================================================================
# List of States
# ===================================================================================

# First group the data by state
grouped_states = DATA.groupby(by=["STATE"])

# Count the number of total tornado events per state.
total_storm_counts = grouped_states["EVENT_ID"].count().to_dict()

# Get a list of all of the state names, ordered by the number of storms, from highest to lowest.
all_states_list = list(total_storm_counts.keys())

# ===================================================================================
# Get Storm Event Summary Data by State
# ===================================================================================

# Create a main dictionary to store the summary data.
state_summaries = {}

# For each state, get the summary data and add it to the main dict.
for s in all_states_list:

    # Make a nested dictionary for the state.
    state_summaries[s] = {}

    # Get the data for the state.
    df = DATA[DATA["STATE"] == s]

    # List to store the EVENT_TYPE values and the key names I'd like to use in the state summaries.
    EVENT_TYPES = [
        "Astronomical Low Tide", "Avalanche", "Blizzard", "Coastal Flood", "Cold/Wind Chill", 
        "Debris Flow", "Dense Fog", "Dense Smoke", "Drought", "Dust Devil", "Dust Storm", 
        "Excessive Heat", "Extreme Cold/Wind Chill", "Flash Flood", "Flood", "Freezing Fog", 
        "Frost/Freeze", "Funnel Cloud", "Hail", "Heat", "Heavy Rain", "Heavy Snow", "High Surf", 
        "High Wind", "Hurricane", "Ice Storm", "Lake-Effect Snow", "Lightning", "Marine Dense Fog", 
        "Marine Hail", "Marine High Wind", "Marine Hurricane/Typhoon", "Marine Strong Wind", 
        "Marine Thunderstorm Wind", "Marine Tropical Depression", "Marine Tropical Storm", 
        "Rip Current", "Seiche", "Sleet", "Storm Surge/Tide", "Strong Wind", "Thunderstorm Wind", 
        "Tornado", "Tropical Depression", "Tropical Storm", "Tsunami", "Waterspout", "Wildfire", 
        "Winter Storm", "Winter Weather"
    ]

    # Count the total number of each type of storm event in the state.
    for e in EVENT_TYPES:
        state_summaries[s][e + " Events"] = df[df["EVENT_TYPE"] == e]["EVENT_ID"].count()

    # Get the sums of total injuries and deaths.
    state_summaries[s]["Direct Injuries"] = df["INJURIES_DIRECT"].sum()
    state_summaries[s]["Indirect Injuries"] = df["INJURIES_INDIRECT"].sum()
    state_summaries[s]["Direct Deaths"] = df["DEATHS_DIRECT"].sum()
    state_summaries[s]["Indirect Deaths"] = df["DEATHS_INDIRECT"].sum()

    

# ===================================================================================
# Show Data by State
# ===================================================================================

print("="*75)
print(f"*{'STORM EVENT DATA FOR THE UNITED STATES IN 2022':^73}*")
print("="*75)

for s in state_summaries:
    print("-"*75)
    print(f"{s} COUNTS:")
    print("-"*75)

    for (key, val) in state_summaries[s].items():
        if int(val) > 0:
            print(f"    {key}: {val}")
