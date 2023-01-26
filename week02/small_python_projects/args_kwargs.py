# Demonstrates how to use *args and **kwargs function arguments.

# *args allows any number of positional arguments.
def add(*args):
    """
    Adds all of the given numbers together and returns the sum.

    Args:
        *args: Accepts any number of values
    """
    result = 0
    for a in args:
        result += a

    return result

print("\nThe add(*args) function accepts any number of values and returns their sum.")
print("\nFor example:")
print(f"add(10, 20) = {add(10, 20)}")
print(f"add(3, 5, 7) = {add(3, 5, 7)}")
print(f"add(1, 2, 4, 5, 6, 8) = {add(1, 2, 4, 5, 6, 8)}")
print(f"add(-5, 5, -3, 3, -10, 10, -15, 15, -25, 25, 1) = {add(-5, 5, -3, 3, -10, 10, -15, 15, -25, 25, 1)}")

#
def count_fruit(**kwargs):
    """
    Counts the total number of fruit, given any number of keyword arguments of types of fruit.

    Args:
        **kwargs: accepts any number of keyword arguments 
                keyword: the type of each fruit
                value: integer number of that type of fruit you have
    """
    total = 0
    for (fruit, amount) in kwargs.items():
        #print(f"You have {amount} {fruit}.")
        total += amount
    return total

print("\nThe count_fruit(**kwargs) function accepts any number of types of fruit\n(as keyword arguments) and the count of each type of fruit (as values).\nIt returns the total count of fruit.")
print("\nFor example:")
print(f"count_fruit(grapes=27) = {count_fruit(grapes=27)}")
print(f"count_fruit(oranges=3, kiwis=4) = {count_fruit(orange=3, kiwi=4)}")
print(f"count_fruit(apples=15, bananas=4, watermelon=1, blueberries=10) = {count_fruit(apple=15, banana=4, watermelon=1, blueberries=10)}")