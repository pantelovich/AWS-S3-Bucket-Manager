from selectors import EpollSelector


print('''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Left or Right?").lower()
if direction == "left":
    direction1 = input("Swim or Wait?").lower()
    if direction == "wait":
        direction = input("Which door? Red, Blue or Yellow?").lower()
        if direction == "yellow":
            print("You win!")
        elif direction == "red":
            print("Burned by fire. Game Over.")
        elif direction == "blue":
            print("Eaten be beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")