MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_checker(user_choice):
    enough_resources = True
    """Check to see if the required resources of the drink match the resources available, output True or False."""
    if MENU[user_choice]["ingredients"]["water"] < resources["water"]:
        print("Waters good!")
        if MENU[user_choice]["ingredients"]["milk"] < resources["milk"]:
            print("Milks good!")
            if MENU[user_choice]["ingredients"]["coffee"] < resources["coffee"]:
                print("Coffee's good!")
            else:
                print("Not enough coffee!")
                enough_resources = False
        else:
            print("Not enough milk!")
            enough_resources = False
    else:
        print("There's not enough water!")
        enough_resources = False
    return enough_resources


enough_resources = (resources_checker(user_choice))
print(enough_resources)






# TODO 7. Turn off the Coffee Machine by entering “off” to the prompt
user_choice = "on"



while user_choice != "off":
    # TODO 1. Print report of all coffee Machine Resources

    # TODO 2. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    user_choice = input("What would you like to order? What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        print("Shutting down!")
        break
    if user_choice == "report":
        print(f"Here are your current resources...\n")
        for key in resources:
            print(f"{key.title()} = {resources[key]}")
        break
    # TODO 3. Check resources sufficient?




    # TODO 4. Process coins. (If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.)

    drink_cost = MENU[user_choice]["cost"]
    print(drink_cost)


    print(f"Your drink costs ${drink_cost}")
    coins_inserted = float(input("You've got enough resources so please insert your coins.... : "))

    # TODO 5. Check transaction successful? (Check that the user has inserted enough money to purchase the drink they selected.)

    def coin_checker(coins_inserted):
        """Checks the number of coins against the cost on the menu"""
        if coins_inserted >= MENU[user_choice]["cost"]:
            print("Coins all good!")
            enough_coins = True
        else:
            print("Not enough coins!")
            enough_coins = False
        return enough_coins

    enough_coins = coin_checker(coins_inserted)
    print(enough_coins)


    # TODO 6. Make Coffee

    if enough_coins == True and enough_resources == True:
        print("Here's your coffee!")
    else:
        print("Bye!")
