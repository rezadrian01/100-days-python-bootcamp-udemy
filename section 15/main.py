MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
change = 0

is_on = True

def resource_is_sufficient(ingredients):
    """Return true if the resource is sufficient"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            return False
    return True

def coins_process(menu):
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pinnies: ")) * 0.01
    if total < MENU[menu]['cost']:
        print("Sorry that's not enough money.")
        return False
    global change, profit
    change = round((total - MENU[menu]['cost']), 2)
    profit += MENU[menu]['cost']
    return True

def deduct_resource(ingredients):
    global resources
    for item in ingredients:
        resources[item] -= ingredients[item]


while is_on:
    menu = input("What would you like? (espresso/latte/cappuccino): ")
    if menu == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money ${profit}")
    elif menu == 'off':
        is_on = False
    else:
        if menu not in MENU:
            print("Invalid menu")
        else:
            if resource_is_sufficient(MENU[menu]['ingredients']):
                if coins_process(menu):
                    deduct_resource(MENU[menu]['ingredients'])
                    print(f"Here is ${change} dollars in change.")
                    print(f"Here is your {menu}. Enjoy!")
            else:
                print("Sorry the resource is not enough")