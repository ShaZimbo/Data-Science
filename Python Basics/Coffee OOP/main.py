""" Coffee Machine program using OOP """

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Ask user what they want
while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    # Secret maintenance options
    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    if choice == "off":
        print("Goodbye!")
        break

    if choice != "report" and choice != "off":
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                print(f"The cost of a {drink.name} is ${drink.cost:.2f}")
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)
