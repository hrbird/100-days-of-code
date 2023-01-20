print("Welcome to the tip calculator.")

totalBill = input("What was the total bill? $")
splitNumber = input("How many people will split the bill? (Enter 1 for no splitting): ")

try:
    bill = float(totalBill)
    split = int(splitNumber)

    if split == 1:
        print(f"\nThe total bill is ${bill:.2f}")
    else:
        print(f"\nThe total bill is ${bill:.2f}, split between {split} people.")

    print("Here is a table with common tip percentages:\n")

    print("TIP % | TOTAL WITH TIP | EACH PERSON PAYS")
    print("-----------------------------------------")

    tipPercentages = [10, 12, 15, 20, 25]

    for t in tipPercentages:
        tipPercent = int(t) / 100
        totalWithTip = bill * (1 + tipPercent)
        splitWithTip = totalWithTip / split

        print(f" {t}%  |    ${totalWithTip:.2f}     |    ${splitWithTip:.2f}")

except ValueError:
    print(f"Oops, you did not enter two numbers!")


# -----------------
# - SAMPLE OUTPUT -
# -----------------
# Welcome to the tip calculator.
# What was the total bill? $124.56
# How many people will split the bill? (Enter 1 for no splitting): 7
# 
# The total bill is $124.56, split between 7 people.
# Here is a table with common tip percentages:
# 
# TIP % | TOTAL WITH TIP | EACH PERSON PAYS
# -----------------------------------------
#  10%  |    $137.02     |    $19.57
#  12%  |    $139.51     |    $19.93
#  15%  |    $143.24     |    $20.46
#  20%  |    $149.47     |    $21.35
#  25%  |    $155.70     |    $22.24
