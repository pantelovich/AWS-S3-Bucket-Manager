for i in range(0,101,7):
    print(i)

print("-"*10)

for i in range(0, 101):
    if i % 7 != 0:
        continue
    print(i)

print("-"*10)

for i in range(0, 101):
    if i % 7 != 0:
        print(i, "is not a multiple of 7")
    else:
        print(i, "is a multiple of 7")
