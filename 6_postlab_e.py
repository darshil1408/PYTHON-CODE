number = input("Enter a number: ")
if len(number) > 1:
    l = list(number)
    l[0], l[-1] = l[-1], l[0]
    number = "".join(l)
print("Number after swapping:", number)
