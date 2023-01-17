# CoffeeMaker class for the coffee machine project.

class CoffeeMaker:
    """The machine that makes the coffee and manages the current levels of resources."""
    def __init__(self):
        self.resources = {
            "water": 300,   # Int current amount of water (in ml)
            "milk": 200,    # Int current amount of milk (in ml)
            "coffee": 100,  # Int current amount of coffee (in ml)
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Determines whether there are enough resources 
        for a given MenuItem drink to be made.
        Returns True when the order can be made, 
        False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, drink):
        """Makes the given MenuItem drink. 
        Deducts the required ingredients from the total resources."""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"\nHere is your {drink.name} ☕️. Enjoy!")
