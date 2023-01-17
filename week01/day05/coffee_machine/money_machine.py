# MoneyMachine class for the coffee machine project.

class MoneyMachine:
    """The part of the machine that processes coins, accepts or refuses payments, and calculates change."""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0         # Float amount of profit made from drinks
        self.money_received = 0 # Float value of coins put into machine

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Asks user for the number of each type of coin they inserted.
        Returns the total value calculated from the inserted coins."""
        print("\nPlease insert coins.")
        for coin in self.COIN_VALUES:
            num_coins = int(input(f"How many {coin}?: "))
            self.money_received += num_coins * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Processes coins that are inserted, then determines if the money
        will cover the cost of the ordered drink. If the user overpaid,
        the function calculates and returns exact change. If the user did
        not pay enough, the payment will not be processed, and the money 
        will be refunded.
        Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"\nHere is {self.CURRENCY}{change:.2f} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("\nSorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
