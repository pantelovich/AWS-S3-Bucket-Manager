import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 3 for Rock, 1 for Paper or 2 for Schissors."))

if choice == 3:
    print(f"You chose: {rock}")
elif choice == 1:
    print(f"You chose: {paper}")
elif choice == 2:
    print(f"You chose: {scissors}")
else:
    print("You typed an invalid number. You lose!")

computerChoice = random.randint(1,3)
print("Computer chose:")
if  computerChoice == 3:
    print(rock)
elif computerChoice == 1:
    print(paper)
elif computerChoice == 2:
    print(scissors)

if choice == computerChoice:
    print("It's a draw!")
while choice == 1:
    if computerChoice == 3:
        print("You win!")
    else:
        print("You lose!")
    break
while choice == 2:
    if computerChoice == 3:
        print("You lose!")
    else:
        print("You win!")
    break
while choice == 3:
    if computerChoice == 1:
        print("You lose!")
    else:
        print("You win!")
    break



import random

# class game:
#     def __init__(self):
#         self.rock = '''
#             _______
#         ---'   ____)
#             (_____)
#             (_____)
#             (____)
#         ---.__(___)
#         '''
#         self.paper = '''
#             _______
#         ---'   ____)____
#                 ______)
#                 _______)
#                 _______)
#         ---.__________)
#         '''
#         self.scissors = '''
#             _______
#         ---'   ____)____
#                 ______)
#             __________)
#             (____)
#         ---.__(___)
#         '''

#     def getChoice(self):
#         return int(input("What do you choose? Type 3 for Rock, 1 for Paper or 2 for Schissors."))
    
#     def getComputerChoice(self):
#         return random.randint(1,3)
    
#     def printChoice(self, choice):
#         print(f"You chose: {choice}")
#         if choice == 1:
#             print(self.paper)
#         elif choice == 2:
#             print(self.scissors)
#         elif choice == 3:
#             print(self.rock)

#     def printComputerChoice(self, computerChoice):
#         print("Computer chose:")
#         if  computerChoice == 3:
#             print(self.rock)
#         elif computerChoice == 1:
#             print(self.paper)
#         elif computerChoice == 2:
#             print(self.scissors)

#     def compareChoices(self, choice, computerChoice):
#         if choice == computerChoice:
#             print("It's a draw!")
#         while choice == 1:
#             if computerChoice == 3:
#                 print("You win!")
#             else:
#                 print("You lose!")
#             break
#         while choice == 2:
#             if computerChoice == 3:
#                 print("You lose!")
#             else:
#                 print("You win!")
#             break
#         while choice == 3:
#             if computerChoice == 1:
#                 print("You lose!")
#             else:
#                 print("You win!")
#             break

#     def play(self):
#         choice = self.getChoice()
#         computerChoice = self.getComputerChoice()
#         self.printChoice(choice)
#         print("Computer chose:")
#         self.printComputerChoice(computerChoice)
#         self.compareChoices(choice, computerChoice)

# game_instance = game()
# game_instance.play()