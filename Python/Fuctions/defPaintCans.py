import math
testH = int(input("Height of wall: "))
testW = int(input("Width of wall: "))
coverage = 5

# def cans():
#     return (testH * testW) / coverage
# print("You will need {} cans of paint".format(math.ceil(cans())))


def paintCalc(testH, testW, coverage):
    area = testH * testW
    cans = math.ceil(area/coverage)
    print(f"You'll need {cans} cans of paint.")

paintCalc(testH, testW, coverage)