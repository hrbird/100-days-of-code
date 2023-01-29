# A program that demonstrates how to handle IndexError exceptions/errors.

fruits = ["apple", "cherry", "blueberry", "huckleberry", "lemon meringue"]

def make_pie(fruit_index):
    try:
        # Try to get the given fruit from the fruits list.
        fruit = fruits[fruit_index]

    except IndexError:
        # If the index is out of range, print "Fruit pie" instead.
        print("fruit pie")

    else:
        # If the index is in range, print the given fruit pie.
        print(fruit + " pie")

for i in range(0, 10):
    make_pie(i)


