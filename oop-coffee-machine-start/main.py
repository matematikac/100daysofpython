from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drink = Menu()
preparing_coffee = CoffeeMaker()
money = MoneyMachine()
#drink.find_drink(order) pravi mi MenuItem objekat, od onoga sto sam porucio!
key_word = True
while key_word == True:
    order = input(f"What would you like? {drink.get_items()}: ")
    if order=="espresso" or order=="latte" or order=="cappuccino":
        if preparing_coffee.is_resource_sufficient(drink.find_drink(order)) :
             if money.make_payment(drink.find_drink(order).cost):
                 preparing_coffee.make_coffee(drink.find_drink(order))
    elif order == 'report':
        preparing_coffee.report()
        money.report()
    elif order == 'off':
        key_word = False
    else:
        print("Niste uneli ispravan napitak, mozete da ga duvate, ali pice necete dobiti!")