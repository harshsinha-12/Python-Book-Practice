a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))

if a > b and a > c:
    if b > c:
        print("The numbers in ascending order are:", c, b, a)
    else:
        print("The numbers in ascending order are:", b, c, a)
elif b > a and b > c:
    if a > c:
        print("The numbers in ascending order are:", c, a, b)
    else:
        print("The numbers in ascending order are:", a, c, b)
else:
    if a > b:
        print("The numbers in ascending order are:", b, a, c)
    else:
        print("The numbers in ascending order are:", a, b, c)


# Storing Conditions:
b, c = 2,3

all = a ==1 and b ==2 and c == 3
print(all)
if all:
    print("Fulfilled")
if all:
    print("Fulfilled")
if all:
    print("Fulfilled")


s = input("Enter a string:")
print(s[::-1])
