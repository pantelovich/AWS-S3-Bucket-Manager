alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(text,shift):
#     Text = ""
#     for i in text:
#         index = alphabet.index(i)
#         # newIndex = index + shift
#         # if newIndex > 25:
#         #     newIndex = newIndex - 26
#         newIndex = (index + shift) % 26
#         Text = Text + alphabet[newIndex]
#     return Text

# def decrypt(text,shift):
#     Text = ""
#     for i in text:
#         index = alphabet.index(i)
#         newIndex = index - shift
#         if newIndex > 25:
#             newIndex = newIndex + 26
#         Text = Text + alphabet[newIndex]
#     return Text

# if direction == encode:
#     print("The encrypted text is: "+ encrypt(text,shift))
# elif direction == "1":
#     print("The decrypted text is: "+ decrypt(text,shift))
# elif direction != encode or direction != "1":
#     print("Please enter a valid input")

def caesar(text,shift,direction):
    Text = ""
    if direction == "decode":
        shift *= -1
    elif direction == "encode":
        shift *= 1
    for i in text:
        if i in alphabet:
            index = alphabet.index(i)
            newIndex = (index + shift) % 26
            Text = Text + alphabet[newIndex]
        else:
            Text = Text + i
    return Text


continueGame = True
while continueGame == True:
    direction = input("Type encode to encrypt, type decode to decrypt:\t").lower()
    text = input("Type your message:\t").lower()
    shift = int(input("Type the shift number:\t"))
    print(f"The new message is:\t {caesar(text,shift,direction)}")
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\t").lower()
    if choice == "no":
        continueGame = False
        print("Goodbye")
        break
    else:
        continueGame = True

