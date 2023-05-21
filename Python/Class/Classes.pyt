class Character:
    def __init__(self, name, eyes, hair, height):
        self.name = name
        self.eyes = eyes
        self.hair = hair
        self.height = height

player1 = Character("Bob", "Blue", "Brown", "170")
player2 = Character("Sue", "Green", "Blonde", "185")
print(player1.eyes, player1.hair, player1.height)
print(player2.hair, player2.eyes)