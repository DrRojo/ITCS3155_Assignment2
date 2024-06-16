import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()
        if choice in recipes:
            cost = recipes[choice]["cost"]    #what is difference of " and '
            ingredients = recipes[choice]["ingredients"]

            if sandwich_maker_instance.check_resources(ingredients):
                print(f"Your sandwich costs ${cost}")
                coins = cashier_instance.process_coins()  # Had issues calling this correctly
                if cashier_instance.transaction_result(coins, cost):
                    print(sandwich_maker_instance.make_sandwich(choice, ingredients))
                else:
                    print("Transaction canceled. Please try again.")
            else:
                print("My apologies friend, we do not have enough ingredients to complete your sandwich.")
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
