# Displays storm event data for the US in 2022 using the pandas library.

from os.path import dirname, join
import pandas

# Get the file path of the StormEvents_2022 CSV file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./StormEvents_2022.csv")

# Load the contents of the file into a panda DataFrame.
DATA = pandas.read_csv(file_path)

# List to store the EVENT_TYPE values and the key names I'd like to use in the state summaries.
ALL_EVENT_TYPES = [
    "Astronomical Low Tide", "Avalanche", "Blizzard", "Coastal Flood", "Cold/Wind Chill", 
    "Debris Flow", "Dense Fog", "Dense Smoke", "Drought", "Dust Devil", "Dust Storm", 
    "Excessive Heat", "Extreme Cold/Wind Chill", "Flash Flood", "Flood", "Freezing Fog", 
    "Frost/Freeze", "Funnel Cloud", "Hail", "Heat", "Heavy Rain", "Heavy Snow", "High Surf", 
    "High Wind", "Hurricane", "Ice Storm", "Lake-Effect Snow", "Lightning", "Rip Current", 
    "Seiche", "Sleet", "Storm Surge/Tide", "Strong Wind", "Thunderstorm Wind", "Tornado", 
    "Tropical Depression", "Tropical Storm", "Tsunami", "Waterspout", "Wildfire", 
    "Winter Storm", "Winter Weather"
]

EVENT_TYPES = [
    "Avalanche", "Blizzard", "Cold/Wind Chill", 
    "Drought", "Dust Storm", "Excessive Heat", "Extreme Cold/Wind Chill", 
    "Flash Flood", "Flood", "Hail", "Heat", "Heavy Rain",
    "Hurricane", "Lightning", "Rip Current", "Storm Surge/Tide", "Tornado", 
    "Tropical Storm", "Tsunami", "Wildfire", "Winter Storm"
]

# ===================================================================================
# Get Storm Event Summary Data by State
# ===================================================================================

# Create a main dictionary to store the summary data.
storm_summaries = {}

# For each event type, get the summary data for each state and add it to the main dict.
for e in EVENT_TYPES:

    e_key = e + " Events"

    # Make a nested dictionary for the state.
    storm_summaries[e_key] = {}

    # Get the data for the event type.
    df = DATA[DATA["EVENT_TYPE"] == e]

    # Count the total number of each storm event in each state.
    grouped_states = df.groupby("STATE")
    events_dict = grouped_states["EVENT_ID"].count().sort_values(ascending=False).to_dict()

    # Get death and injury data for this event type and each state.
    direct_injuries_dict = grouped_states["INJURIES_DIRECT"].sum().sort_values(ascending=False).to_dict()
    direct_deaths_dict = grouped_states["DEATHS_DIRECT"].sum().sort_values(ascending=False).to_dict()
    indirect_injuries_dict = grouped_states["INJURIES_INDIRECT"].sum().sort_values(ascending=False).to_dict()
    indirect_deaths_dict = grouped_states["DEATHS_INDIRECT"].sum().sort_values(ascending=False).to_dict()

    # Add the data for each state to the summary dictionary.
    for (state, num_events) in events_dict.items():
        storm_summaries[e_key][state] = {}
        storm_summaries[e_key][state]["Events"] = num_events
        storm_summaries[e_key][state]["Injuries"] = int(direct_injuries_dict[state]) + int(indirect_injuries_dict[state])
        storm_summaries[e_key][state]["Deaths"] = int(direct_deaths_dict[state]) + int(indirect_deaths_dict[state])

    #print(storm_summaries[e_key])

# ===================================================================================
# Show Data by State
# ===================================================================================

def print_summary(storm_summaries):

    print("="*75)
    print(f"*{'STORM EVENT DATA FOR THE UNITED STATES IN 2022':^73}*")
    print("="*75)

    for event_type in storm_summaries:
        print("\n")
        print("*"*50)
        event_str = event_type + " 2022"
        print(f"{event_str:^50}")
        print("*"*50)

        print(f"{'STATE':<21} | EVENTS | INJURIES | DEATHS")
        print("-"*50)

        for state in storm_summaries[event_type].keys():
            num_events = str(storm_summaries[event_type][state]["Events"])
            num_injuries = str(storm_summaries[event_type][state]["Injuries"])
            num_deaths = str(storm_summaries[event_type][state]["Deaths"])

            # Show blanks instead of zeroes.
            if num_injuries == "0":
                num_injuries = ""

            if num_deaths == "0":
                num_deaths = ""

            print(f"{state:<21}   {num_events:>6}   {num_injuries:>8}   {num_deaths:>6}")

print_summary(storm_summaries)

