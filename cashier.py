class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert your coins: ")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.10
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Your change is {change} coins.")
            else:
                print(f"Thank you! No change to give back")
            return True
        else:
            print(f"Not enough money. ")
            return False
