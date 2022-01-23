from ingredients import MENU, resources


report = {}
report = resources
report["money"] = 0


def is_enough_resources(s):
    """This function returns true if there is enough resources for making a drink, or false if not"""
    if MENU[s]["ingredients"]["water"] <= report["water"] and MENU[s]["ingredients"]["coffee"] <= report["coffee"]:
        if s == "espresso":
            return True
        elif MENU[s]["ingredients"]["milk"] <= report["milk"]:
            return True
    else:
        return False


def resource_missing(s):
    """This function returns first resources that missing"""
    if MENU[s]["ingredients"]["water"] > report["water"]:
        return "water"
    elif MENU[s]["ingredients"]["coffee"] > report["coffee"]:
        return "coffee"
    elif s !='espresso' and MENU[s]["ingredients"]["milk"] > report["milk"]:
        return "milk"


def value_of_received_money():
    """This function inputs user nickles and return given money"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies


key_word = False

while not key_word:
    drink = input("What would you like? espresso/latte/cappuccino: ").lower()
    if drink == 'espresso' or drink == 'latte' or drink == 'cappuccino':
        if is_enough_resources(drink):
            value = value_of_received_money()
            if MENU[drink]["cost"] <= value:
                change = round(value - MENU[drink]["cost"], 2)
                report["water"] -= MENU[drink]["ingredients"]["water"]
                report["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                report["money"] += MENU[drink]["cost"]
                if drink != "espresso":
                    report["milk"] -= MENU[drink]["ingredients"]["milk"]
                print(f"Here is ${change} change.\nHere is your {drink}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            missing = resource_missing(drink)
            print(f"Sorry there is not enough {missing}.")
    elif drink == "report":
        print(f"Water: {report['water']}ml.")
        print(f"Milk: {report['milk']}ml.")
        print(f"Coffee: {report['coffee']}g.")
        print(f"Profit: ${report['money']}")
    elif drink == "off":
        key_word = True