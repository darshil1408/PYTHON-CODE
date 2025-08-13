def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))
