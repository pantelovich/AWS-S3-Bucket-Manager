class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def calculateTotal(items):
    total = 0
    
    for item in items:
        total += item.price
    return total

print(calculateTotal([item("apple", 3), item("banana", 2), item("strawberry", 5), item("pineapple", 1)]))


# prices = {
#     "apple": 3,
#     "banana": 2,
#     "strawberry": 5,
#     "pineapple": 1
# }

# def fruitList(fruits):
#     total = 0
#     for item in prices:
#         if item in prices:
#             total += prices[item]
    # for fruit in fruits:
        # if fruit == "apple":
        #     total += 3
        # elif fruit == "banana":
        #     total += 2
        # elif fruit == "strawberry":
        #     total += 5
        # elif fruit == "pineapple":
        #     total += 1
    #     else:
    #         print("Item does not exist")
    # return total

#print(fruitList(['apple', 'banana', 'strawberry', 'pineapple','Pasta']))




