# Displays storm event data for the US in 2022 using the pandas library.

from os.path import dirname, join
import pandas

# Get the file path of the StormEvents_2022 CSV file.
current_dir = dirname(__file__)
file_path = join(current_dir, "./StormEvents_2022.csv")

# Load the contents of the file into a panda DataFrame.
DATA = pandas.read_csv(file_path)

# Copy rows about Tornado events into a new DataFrame.
T_DATA = DATA[DATA["EVENT_TYPE"] == "Tornado"]

# DataFrame.head() shows a given number of rows at the top.
print(f"Head (5 rows):\n{T_DATA.head(25)}\n")

# DataFrame.columns shows the column names.
print(f"Columns:\n{T_DATA.columns}\n")

for i in T_DATA.head(5).index:
    date_time = T_DATA['BEGIN_DATE_TIME'][i]
    day = T_DATA['BEGIN_DAY'][i]
    begin_time = T_DATA['BEGIN_TIME'][i]
    state = T_DATA['STATE'][i]
    event_type = T_DATA['EVENT_TYPE'][i]

    direct_injuries = T_DATA['INJURIES_DIRECT'][i]
    indirect_injuries = T_DATA['INJURIES_INDIRECT'][i]
    direct_deaths = T_DATA['DEATHS_DIRECT'][i]
    indirect_deaths = T_DATA['DEATHS_INDIRECT'][i]
    
    print(f"\nBEGIN_DATE_TIME: {date_time}, STATE: {state}, EVENT TYPE: {event_type}")
    print(f"DIRECT INJURIES: {direct_injuries}, DIRECT DEATHS: {direct_deaths}")

print(f"\n\nNumber of rows:{len(T_DATA)}")

# ===================================================================================
# Isolate Tornado Data
# ===================================================================================

# Copy rows about Tornado events into a new DataFrame.
T_DATA = DATA[DATA['EVENT_TYPE'] == "Tornado"]

# ===================================================================================
# All States
# ===================================================================================

# Get a list of all of the states in the DataFrame.
all_states_list = list(T_DATA["STATE"].sort_values().unique())

print("\nStates:")
print(all_states_list)

# ===================================================================================
# Total Tornadoes by State
# ===================================================================================

# Group the data by state
tornado_states = T_DATA.groupby(by=["STATE"])

# Count the number of total tornado events per state.
total_tornado_counts = tornado_states["EVENT_ID"].count().to_dict()

print("\n\nTornado Data:")
print(total_tornado_counts)

# ===================================================================================
# Fujita Scale Tornadoes by State
# ===================================================================================

# For each F Scale category, group the tornadoes by state and count them.
ef0_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EF0"].groupby("STATE")['EVENT_ID'].count().to_dict()
ef1_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EF1"].groupby("STATE")['EVENT_ID'].count().to_dict()
ef2_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EF2"].groupby("STATE")['EVENT_ID'].count().to_dict()
ef3_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EF3"].groupby("STATE")['EVENT_ID'].count().to_dict()
ef4_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EF4"].groupby("STATE")['EVENT_ID'].count().to_dict()
ef5_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EF5"].groupby("STATE")['EVENT_ID'].count().to_dict()
efu_state_counts = T_DATA[T_DATA["TOR_F_SCALE"] == "EFU"].groupby("STATE")['EVENT_ID'].count().to_dict()

print("\n\nEF0 DATA:")
print(ef0_state_counts)

# ===================================================================================
# Injuries and Deaths by State
# ===================================================================================

# Get the sums of total injuries and deaths by state.
direct_injury_sums = T_DATA.groupby("STATE")["INJURIES_DIRECT"].sum()
indirect_injury_sums = T_DATA.groupby("STATE")["INJURIES_INDIRECT"].sum()

direct_death_sums = T_DATA.groupby("STATE")["DEATHS_DIRECT"].sum()
indirect_death_sums = T_DATA.groupby("STATE")["DEATHS_INDIRECT"].sum()

print("\n\nDirect Deaths DATA:")
print(direct_death_sums)


# ===================================================================================
# Show Data by State
# ===================================================================================

i = 0
state_name = all_states_list[i]
print(f"{state_name}:")
print(f"Total tornadoes: {total_tornado_counts[state_name]}")
print(f"EF0 tornadoes: {ef0_state_counts[state_name]}")
print(f"EF1 tornadoes: {ef1_state_counts[state_name]}")
print(f"EF2 tornadoes: {ef2_state_counts[state_name]}")
print(f"EF3 tornadoes: {ef3_state_counts[state_name]}")
print(f"EF4 tornadoes: {ef4_state_counts[state_name]}")
print(f"EF5 tornadoes: {ef5_state_counts[state_name]}")
print(f"EFU tornadoes: {efu_state_counts[state_name]}")
