# This program pretends to be a coffee machine that can 
# make a list of drinks, process coins and return change, and
# check current levels of resources (water, milk, coffee grounds).

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Special codes to turn machine off or show a report.
OFF_CODE = 99
REPORT_CODE = 0

class CoffeeMachine:
    """The whole machine that manages the CoffeeMaker, MoneyMachine,
    Menu, and MenuItem objects."""
    def __init__(self):
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.menu = Menu()
        self.is_on = True

    def start_machine(self):
        """Starts the coffee machine, which allows the user to order
        and pay for drinks, as well as see reports of the current levels
        of resources. This function loops until the user enters the code
        to turn off the machine."""
        while self.is_on:
        
            print("What would you like?")
            print("\nPlease enter the number of your choice.")
            print(self.menu.get_menu_list())

            order_num = int(input("\n> "))

            if order_num > 0 and order_num <= self.menu.get_number_of_items():
            
                # If the user enters a number within the range of items, select the ordered drink.
                my_drink = self.menu.find_drink_by_num(order_num)
                my_drink.show_drink()

                # Check if there are sufficient resources left.
                if self.coffee_maker.is_resource_sufficient(my_drink):

                    # Process the payment for the drink.
                    if self.money_machine.make_payment(my_drink.cost):

                        # If the payment is successful, make the drink.
                        self.coffee_maker.make_coffee(my_drink)
            
            elif order_num == REPORT_CODE:
                # If the user enters the special "report" code, 
                # show a report of the machine's current resources.
                print("\nCurrent Resources:")
                self.coffee_maker.report()
                self.money_machine.report()

            elif order_num == OFF_CODE:
                # If the user enters the special "off" code, turn off the machine.
                print("\nTurning off coffee machine...")
                self.is_on = False

            else:
                print(f"Sorry, {order_num} is not an option.")

            print("\n=============================\n\n")

def main():

    coffee_machine = CoffeeMachine()

    coffee_machine.start_machine()
    
    

if __name__ == "__main__":
    main()