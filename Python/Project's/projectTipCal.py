print("Welcome to the tip calculator")
bill = float(input("What was the total of the bill? "))
people = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to give? "))#%
total = (((bill * tip)/100) / people)
print(round(total, 2))