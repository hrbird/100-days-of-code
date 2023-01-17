# MenuItem and Menu classes for the coffee machine project.

class MenuItem:
    """A menu item (drink) that the coffee maker can make."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name        # String name of drink
        self.cost = cost        # Float cost of drink
        self.ingredients = {
            "water": water,     # Int amount of water (in ml)
            "milk": milk,       # Int amount of milk (in ml)
            "coffee": coffee    # Int amount of coffee (in ml)
        }

class Menu:
    """A menu with drinks. Manages all of the MenuItem objects."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24),
        ]

    def get_items(self):
        """Returns all the names of the available menu items in one string."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def get_menu_list(self):
        """Returns all the names of the available menu items in a numbered list."""
        options = "Drink Menu:"
        for i in range(len(self.menu)):
            options += f"\n{i + 1}. {self.menu[i].name}"
        return options

    def get_number_of_items(self):
        """Returns the number of possible drink items as an integer."""
        return len(self.menu)

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. 
        Returns that MenuItem if it exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")

    def find_drink_by_num(self, num):
        """Searches the menu for a particular drink by menu number. 
        Returns that MenuItem if it exists, otherwise returns None."""
        index = num - 1
        if index >= 0 and index < len(self.menu):
            return self.menu[index]
        print("Sorry, that item is not available.")
