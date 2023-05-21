import random
names = input("Enter names separated by commas: ")

list = names.split(",")

#CLean up the names
for i in range(len(list)):
    list[i] = list[i].strip().capitalize()


# luckyPerson = random.choice(list)
luckyPerson = random.randint(0, len(list)-1)
person = list[luckyPerson]
print(f"The lucky person is: {person}")