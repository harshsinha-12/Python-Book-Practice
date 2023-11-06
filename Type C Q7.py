N = int(input("Enter the number:"))
s = 0
if N > 0:
    for i in range(N, 2*N + 1):
        s = s + i
    print("Sum of the numbers:", s)
else:
    for i in range(2*N, N+1):
        s = s + i
    print("Sum of the numbers:", s)