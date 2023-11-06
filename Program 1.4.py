n = int(input("Enter a Number between 0-999:"))
if n < 0 or n > 999:
    print("Invalid Input")
elif n < 10:
    print("One digit Number")
elif n < 100:
    print("Two digit Number")
elif n < 1000:
    print("Three digit Number")