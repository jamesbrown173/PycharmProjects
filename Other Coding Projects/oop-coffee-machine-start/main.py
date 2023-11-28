from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

print(money_machine.report())
print(coffee_maker.report())

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(money_machine.report())
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if (coffee_maker.is_resource_sufficient(drink)) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#







