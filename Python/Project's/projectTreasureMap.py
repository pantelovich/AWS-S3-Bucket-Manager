
map = [['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']]
#position = int(input("Where do you want to put your character (row, column)? "))
for row in map:
    print(' '.join(row))
    
# Get the user's desired position as input
position = input("Where do you want to put your character (row, column)? ")
# Check if the input is valid and update the map if so
if len(position) == 2 and position.isnumeric():
    row = int(position[0]) - 1
    col = int(position[1]) - 1
    if 0 <= row < 3 and 0 <= col < 3:
        map[row][col] = ' X'
    else:
        print("Invalid position")
else:
    print("Invalid input")
# Print the updated map
for row in map:
    print(' '.join(row))


# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the trasure?")
# horizontal = int(position[0])
# vertical = int(position[1])
# map[horizontal - 1][vertical - 1] = " X"
# print(f"{row1}\n{row2}\n{row3}")


# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# if position == 11:
#     row1 = [' X', '⬜️', '⬜️']
# elif position == 12:
#     row1 = ['⬜️', ' X', '⬜️']
# elif position == 13:
#     row1 = ['⬜️', '⬜️', ' X']
# elif position == 21:
#     row2 = [' X', '⬜️', '⬜️']
# elif position == 22:
#     row2 = ['⬜️', ' X', '⬜️']
# elif position == 23:
#     row2 = ['⬜️', '⬜️', ' X']
# elif position == 31:
#     row3 = [' X', '⬜️', '⬜️']
# elif position == 32:
#     row3 = ['⬜️', ' X', '⬜️']
# elif position == 33:
#     row3 = ['⬜️', '⬜️', ' X']
# else:
#     print("Invalid position")
# print(f"{row1}\n{row2}\n{row3}")


# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")