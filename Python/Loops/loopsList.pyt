numbers = [5, 3, 7, 8, 1, 10, 12, 20, 30, 1]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# print(numbers[5])

# for i in range(0, len(numbers)): #len() always gives the total number of items in list
#     print(numbers[i])

# for n in numbers:
#     print(n)

def addNumbers(numbers):
    total = 0

    for n in numbers:
        total += n
        print(n, total)
    return total

print(addNumbers([3, 7 ,8 ,2]))
