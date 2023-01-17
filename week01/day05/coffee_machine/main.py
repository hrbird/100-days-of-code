# This program pretends to be a coffee machine that can 
# make a list of drinks, process coins and return change, and
# check current levels of resources (water, milk, coffee grounds).

import menu
import coffee_maker
import money_machine

# Special codes to turn machine off or show a report.
OFF_CODE = 99
REPORT_CODE = 0

#TODO: Create a loop to handle multiple orders.

def main():

    my_coffee_maker = coffee_maker.CoffeeMaker()
    my_money_machine = money_machine.MoneyMachine()
    my_menu = menu.Menu()
    
    print("What would you like?")
    print("\nPlease enter the number of your choice.")
    print(my_menu.get_menu_list())

    order_num = int(input("\n> "))

    if order_num >= 1 and order_num <= my_menu.get_number_of_items():
        # If the user enters a number within the range of items, select the ordered drink.

        my_drink = my_menu.find_drink_by_num(order_num)

        print(f"You selected the {my_drink.name}, which costs ${my_drink.cost:.2f}")

        # Check if there are sufficient resources left.
        if my_coffee_maker.is_resource_sufficient(my_drink):

            # Process the payment for the drink.
            if my_money_machine.make_payment(my_drink.cost):

                # If the payment is successful, make the drink.
                my_coffee_maker.make_coffee(my_drink)
    
    elif order_num == REPORT_CODE:
        # If the user enters the special "report" code, 
        # show a report of the machine's current resources.
        print("\nCurrent Resources:")
        my_coffee_maker.report()
        my_money_machine.report()

    elif order_num == OFF_CODE:
        # If the user enters the special "off" code, turn off the machine.
        print("\nTurning off coffee machine...")

    else:
        print(f"Sorry, {order_num} is not an option.")

    print("\n")

if __name__ == "__main__":
    main()