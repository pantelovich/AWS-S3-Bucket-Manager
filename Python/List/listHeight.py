studentHeights = [180, 124, 165, 173, 189, 169, 146]



# print (f"The summary of the heights is: {sum(studentHeights)}")
# print(f"The are {len(studentHeights)} entries so far")
# average = sum(studentHeights)/len(studentHeights)

# print (f"The round average height is: {round(average,2)}")

# averageHeight = "{:.2f}".format(average)
# print (f"The formatted average height is: {averageHeight}")#Same as above but formatted

studentHeights = input("Input a list of student heights ").split()

totalHeight = 0 
for height in studentHeights:
    totalHeight += height
print(f"The total height is: {totalHeight}")

numberOfStudents = 0
for student in studentHeights:
    numberOfStudents += 1
print(f"The number of students is: {numberOfStudents}")

averageHeight = round(totalHeight/numberOfStudents , 2)
print(f"The average height is: {averageHeight}")