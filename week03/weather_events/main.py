# Displays storm event data for the US in 2022 using the pandas library.

from os.path import dirname, join
import pandas

# Get the file path of the StormEvents_2022 CSV file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./StormEvents_2022.csv")

# Load the contents of the file into a panda DataFrame.
DATA = pandas.read_csv(file_path)

# Copy rows about Tornado events into a new DataFrame.
T_DATA = DATA[DATA['EVENT_TYPE'] == "Tornado"]

# ===========================================================================
# List of States
# ===================================================================================

# First group the data by state
tornado_states = T_DATA.groupby(by=["STATE"])

# Count the number of total tornado events per state.
total_tornado_counts = tornado_states["EVENT_ID"].count().sort_values(ascending=False).to_dict()

# Get a list of all of the state names, ordered by the number of tornadoes, from highest to lowest.
all_states_list = list(total_tornado_counts.keys())

# ===================================================================================
# Get Tornado Summary Data by State
# ===================================================================================

# Create a main dictionary to store the summary data.
state_summaries = {}

# For each state, get the summary data and add it to the main dict.
for s in all_states_list:

    # Make a nested dictionary for the state.
    state_summaries[s] = {}

    # Get the data for the state.
    state_data = T_DATA[T_DATA["STATE"] == s]

    # Count the number of total tornado events in the state.
    state_summaries[s]["total_tornadoes"] = state_data["EVENT_ID"].count()

    # For each Fujita Scale category, count how many tornadoes there were.
    state_summaries[s]["EF0_count"] = state_data[state_data["TOR_F_SCALE"] == "EF0"]["EVENT_ID"].count()
    state_summaries[s]["EF1_count"] = state_data[state_data["TOR_F_SCALE"] == "EF1"]["EVENT_ID"].count()
    state_summaries[s]["EF2_count"] = state_data[state_data["TOR_F_SCALE"] == "EF2"]["EVENT_ID"].count()
    state_summaries[s]["EF3_count"] = state_data[state_data["TOR_F_SCALE"] == "EF3"]["EVENT_ID"].count()
    state_summaries[s]["EF4_count"] = state_data[state_data["TOR_F_SCALE"] == "EF4"]["EVENT_ID"].count()
    state_summaries[s]["EF5_count"] = state_data[state_data["TOR_F_SCALE"] == "EF5"]["EVENT_ID"].count()
    state_summaries[s]["EFU_count"] = state_data[state_data["TOR_F_SCALE"] == "EFU"]["EVENT_ID"].count()

    # Get the sums of total injuries and deaths.
    state_summaries[s]["direct_injuries"] = state_data["INJURIES_DIRECT"].sum()
    state_summaries[s]["indirect_injuries"] = state_data["INJURIES_INDIRECT"].sum()
    state_summaries[s]["direct_deaths"] = state_data["DEATHS_DIRECT"].sum()
    state_summaries[s]["indirect_deaths"] = state_data["DEATHS_INDIRECT"].sum()


# ===================================================================================
# Show Data by State
# ===================================================================================

print("="*75)
print(f"*{'TORNADO DATA FOR THE UNITED STATES IN 2022':^73}*")
print("="*75)

print(f"\n{'':<15}{'TOTAL':>10} | {'FUJITA SCALE CATEGORIES':^28} | {'TOTAL':>8}{'TOTAL':>8}")
print(f"{'STATE':<15}{'TORNADOES':>10} | {'EF0':>4}{'EF1':>4}{'EF2':>4}{'EF3':>4}{'EF4':>4}{'EF5':>4}{'EFU':>4} | {'INJURIES':>8}{'DEATHS':>8}")
print("-"*75)

for s in state_summaries:
    total = state_summaries[s]['total_tornadoes']
    ef0 = state_summaries[s]['EF0_count']
    ef1 = state_summaries[s]['EF1_count']
    ef2 = state_summaries[s]['EF2_count']
    ef3 = state_summaries[s]['EF3_count']
    ef4 = state_summaries[s]['EF4_count']
    ef5 = state_summaries[s]['EF5_count']
    efu = state_summaries[s]['EFU_count']
    injuries = state_summaries[s]['direct_injuries'] + state_summaries[s]['indirect_injuries']
    deaths = state_summaries[s]['direct_deaths'] + state_summaries[s]['indirect_deaths']

    print(f"{s:<15}{total:>10} | {ef0:>4}{ef1:>4}{ef2:>4}{ef3:>4}{ef4:>4}{ef5:>4}{efu:>4} | {injuries:>8}{deaths:>8}")