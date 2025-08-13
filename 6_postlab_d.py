number = int(input("Enter a number: "))
last = number % 10
first = number
while first >= 10:
    first //= 10
print("First digit:", first)
print("Last digit:", last)
