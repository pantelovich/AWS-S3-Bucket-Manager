def formatName(fName, lName):
    if fName == "" or lName == "":
        return "Invalid input"
    formatedfName = fName.title()
    formatedlName = lName.title()
    return f"{formatedfName} {formatedlName}"


print(formatName(input("Enter your first name: "), input("Enter your last name: ")))
