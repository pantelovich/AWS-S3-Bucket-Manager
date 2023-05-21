print("Prime number checker")
num = int(input("Please enter a number: "))

def checker(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    if isPrime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

checker(num)