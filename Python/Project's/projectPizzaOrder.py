smallPissa = 15
mediumPizza = 20
largePizza = 25
cheese = 1

order = input("whould you like a small, medium or large pizza? ")
bill = 0
if order == "small":
    bill += smallPissa
elif order == "medium":
    bill += mediumPizza
elif order == "large":
    bill += largePizza

pepperoni = input("whould you like pepperoni? ")
if order == "small" and pepperoni == "yes":
    bill += 2
elif order == "medium" or "large" and pepperoni == "yes":
    bill += 3

extraCheese = input("whould you like extra cheese? ")
if extraCheese == "yes":
    bill += cheese
print(f"Your bill is: {bill}$")
