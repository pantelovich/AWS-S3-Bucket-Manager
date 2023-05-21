programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# print(programming_dictionary["Bug"])

# Adding new items to dictionary!!!

programming_dictionary["loop"] = "The action of doing something over and over again."

# Create an empty dictionary!!!

empty_dictionary = {}

# Wipe an existing dictionary!!!

# programming_dictionary = {}
# programming_dictionary.clear()

# print(programming_dictionary)

# Edit an item in a dictionary!!!

# programming_dictionary["Bug"] = "A moth in your conputer."
# print(programming_dictionary["Bug"])

# Delete an item from a dictionary!!!

# programming_dictionary.pop("Bug")
# print(programming_dictionary)

#loop though a dcitionary!!!

for i in programming_dictionary:
    # print(i)
    print(f"{i}: {programming_dictionary[i]}")

