year = int(input("Enter a year: "))


if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("A leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("Not a leap year")
elif year % 4 == 0 and year % 100 !=0:
    print("A leap year")
else:
    print("Not a leap year")

