Menu = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

Resources = {"water": 300, "milk": 200, "coffee": 100}

def print_report(money):
    '''Prints report of all coffe machine resources'''
    print(f"Water: {Resources['water']}ml")
    print(f"Milk: {Resources['milk']}ml")
    print(f"Coffee: {Resources['coffee']}g")
    print(f"Money: ${money:.2f}")

myScreen = Screen()
print(myScreen.canvheight)
myScreen.exitonclick()