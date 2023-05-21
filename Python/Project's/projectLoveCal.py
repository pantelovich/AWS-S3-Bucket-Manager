print("welcome to love calculator")

name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

combinedString = name1 + name2
lowerCaseString = combinedString.lower()

t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")
l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")

true = t + r + u + e
love = l + o + v + e

loveScore = str(true)+str(love)
loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"your love score is {loveScore}, you o together like coke and mentos")
elif loveScore >= 40 <= 50:
    print(f"Your love score is {loveScore}, you are alright together")
else:
    print("Your love score is {loveScore}")