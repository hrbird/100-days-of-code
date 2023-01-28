# Displays storm event data for the US in 2022 using the pandas library.

from os.path import dirname, join
import pandas

# Get the file path of the StormEvents_2022 CSV file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./StormEvents_2022.csv")

# Load the contents of the file into a panda DataFrame.
DATA = pandas.read_csv(file_path)

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

    print(f"\nGetting data for {e}...")

    for (state, num_events) in events_dict.items():
        storm_summaries[e_key][state] = {}
        storm_summaries[e_key][state]["Events"] = num_events
        storm_summaries[e_key][state]["Injuries"] = int(direct_injuries_dict[state]) + int(indirect_injuries_dict[state])
        storm_summaries[e_key][state]["Deaths"] = int(direct_deaths_dict[state]) + int(indirect_deaths_dict[state])

    print(storm_summaries[e_key])

# ===================================================================================
# Show Data by State
# ===================================================================================

def print_summary(storm_summaries):

    print("="*75)
    print(f"*{'STORM EVENT DATA FOR THE UNITED STATES IN 2022':^73}*")
    print("="*75)

    for event_type in storm_summaries:
        print()
        print("-"*75)
        print(f"{event_type}:")
        print("-"*75)

        for state in storm_summaries[event_type].keys():
            num_events = storm_summaries[event_type][state]["Events"]
            num_injuries = storm_summaries[event_type][state]["Injuries"]
            num_deaths = storm_summaries[event_type][state]["Deaths"]

            print(f"{state}:    Events: {num_events}    Injuries: {num_injuries}    Deaths: {num_deaths}")

print_summary(storm_summaries)