height = int(input("Height: "))

if height <= 120:
    print("Sorry you are not aloud on this ride")
else:
    age = int(input("Age: "))
    if age < 12:
        print("Please pay $5")
    else:
        print("Please pay $7")

# -----------------------------------------------

class rollercoaster:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

height = int(input("Height: "))

if height <= 120:
    print("Sorry you are not aloud on this ride")
else:
    age = int(input("Age: "))
    if age < 12:
        print("Please pay $5")
    else:
        print("Please pay $7")