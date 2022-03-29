from menu import MENU,resources
import os
from time import sleep
from art import banner,coffee

current_resources = resources
current_resources['money'] = 0
coin_dict = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}

def report(cr):
    '''Print list/report of the resources and their current values'''
    [print(f"{key.capitalize()}: {cr[f'{key}']}ml") for key in cr if key != 'money'] 
    print(f"Money: ${cr['money']}")

def check_resources(cr,u_inp):
    required_water = MENU[u_inp]['ingredients']['water']
    required_coffee = MENU[u_inp]['ingredients']['coffee']

    if u_inp == 'espresso': required_milk = 0
    else: required_milk = MENU[u_inp]['ingredients']['milk']

    if cr['water'] >= required_water and cr['coffee']>= required_coffee and cr['milk'] >= required_milk: return True

def process_user_input(u_inp,cr):
    
    if u_inp == "off": return "off"
    if u_inp == "report": report(cr)
    if u_inp in MENU:
        available = check_resources(cr,u_inp)
        product = u_inp
        if available:
            cost = MENU[u_inp]['cost']
            print(f"The {product} is ${cost}")
            print("Please insert coins.")
            process_coins(cost,product)
        else:
            print(f"Unfortunately the {product} cannot be made, the coffee machine will soon be resupplied.")

def process_coins(needed,prod):
    received = 0
    for elements in coin_dict:
        received += int(input(f"How many {elements}?: "))*coin_dict[f"{elements}"]
        print(f"Received: {received}") 
        if received >=needed: break

    change = round(received-needed,2)

    if change>=0:
        if change > 0:
            print(f"Here is ${change} in change.")

        print(f"Enjoy your {prod}!")
        print(coffee)
        update_resources(prod,needed)

    elif change<0:
        print("Insufficient, your coins are refunded.")

def update_resources(prod_used,money_earned):
    current_resources['money'] += money_earned
    for ingredient in MENU[f"{prod_used}"]["ingredients"]:
        current_resources[f"{ingredient}"] -= MENU[f"{prod_used}"]["ingredients"][f"{ingredient}"]

while True:
    os.system('cls || clear')
    print(banner)

    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    instruction = process_user_input(user_input,current_resources)
    
    if instruction == "off": break
 
    sleep(5)