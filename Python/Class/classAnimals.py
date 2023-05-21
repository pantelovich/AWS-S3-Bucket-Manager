class Animals:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def __str__(self):
        return "Animals - Name: {} - Sound: {}".format(self.name, self.sound)
    
    def make_sound(self):
        return self.sound

list_of_animals = [Animals("dog", "woof"), Animals("cat", "meow"), Animals("cow", "moo"), Animals("mouse", "")]
for animal in list_of_animals:
    if animal.sound:
        print("Animal: ", animal.name, " Sound: ", animal.make_sound())
    else:
        print("Animal: ", animal.name, "doesn't make a sound")
