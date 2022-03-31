from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
os.system('cls || clear')

machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    choices = menu.get_items()
    selection = input(f"What type of coffee would you like? {choices}: ")   

    if selection == "report": 
        machine.report()
        money_machine.report()
    elif selection == "off": break
    else:
        drink = menu.find_drink(selection)

        if machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):                                                         
                machine.make_coffee(drink)                                 
        else: break