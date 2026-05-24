COFFEE = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3.0,
    }
}

MONEY = 0
RESOURCES = {
    "water": 1000,
    "milk": 800,
    "coffee": 100,
}

def report() -> None:
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money:${MONEY}")
    

def is_resources_sufficient(coffee_chosen: str) -> bool:
    '''Returns True when order can be made, 
    False if ingredients are insufficient.'''
    for item in coffee_chosen:
        if coffee_chosen[item] > RESOURCES[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global MONEY
        MONEY += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        RESOURCES[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_machine_on = True

while is_machine_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        report()
    elif choice not in COFFEE and choice != "off" and choice != "report":
        print("Invalid choice.")
    else:
        drink = COFFEE[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["price"]):
                make_coffee(choice, drink["ingredients"])

