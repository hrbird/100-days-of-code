

# Conversion to different mass metrics.
lb_kg = 2.204623
lb_stones = 14

# List of random things and their average weight in pounds.
randomWeights = [
    ["golden retrievers", 65],
    ["small bales of hay", 50],
    ["watermelons", 20],
    ["bicycles", 18],
    ["cats", 10],
    ["gallons of milk", 8.6],
    ["chickens", 5.7],
    ["chihuahuas", 4],
    ["pillows", 2.75],
    ["loaves of bread", 1.25],
    ["coffee mugs", 0.55],
    ["bricks", 0.5],
    ["bananas", 0.25],
    ["bars of soap", 0.22],
    ["toothbrushes", 0.039]
]

# Get the user's weight in pounds.
weight = input("What is your weight in pounds? ")

# Check that the user entered an int or float.
try:
    w = float(weight)
    
    print(f"\nYou weigh {w / lb_kg:.2f} kilograms or {w / lb_stones:.2f} stones.")
    print("\nYou also weigh about...")

    # Convert the user's weight into each of the random conversions
    # and print the results on separate lines.
    for r in randomWeights:
        print(f"{w / r[1]:.1f} {r[0]}")

except ValueError:
    print(f"Oops! {weight} is not a number!")


# -----------------
# - SAMPLE OUTPUT -
# -----------------
# What is your weight in pounds? 115
#
# You weigh 52.16 kilograms or 8.21 stones.
#
# You also weigh about...
# 0.7 great danes
# 1.8 golden retrievers
# 2.3 small bales of hay
# 2.4 water tank jugs
# 4.3 toddlers
# 5.8 watermelons
# 6.4 bicycles
# 10.5 gallons of paint
# 11.5 cats
# 13.4 gallons of milk
# 20.2 chickens
# 23.0 toasters
# 41.8 pillows
# 92.0 loaves of bread
# 209.1 coffee mugs
# 230.0 bricks
# 28.8 chihuahuas
# 348.5 apples
# 460.0 bananas
# 522.7 bars of soap
# 2948.7 toothbrushes
# 16772.7 pennies
