height = input("Please enter your height in meters: ")
weight = input("Please enter your weight in kilograms: ")

bmi = float(weight) / float(height)**2
rounded_bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your BMI is: {rounded_bmi}, you are underweight")
elif 18 < bmi < 25:
    print(f"Your BMI is: {rounded_bmi}, you have a normal weight")
elif 25 < bmi < 30:
    print(f"Your BMI is: {rounded_bmi}, you are overweight")
elif 30 < bmi < 35:
    print(f"Your BMI is: {rounded_bmi}, you are obese")
else:
    print(f"Your BMI is: {rounded_bmi}, you are clinically obese")

# #normal method
# print("Your BMI is: " + str(roundBmi))

# #f-string method
#print(f"Your BMI is: {rounded_bmi}")#f-string method
#print("Your BMI is: " ,roundBmi)

