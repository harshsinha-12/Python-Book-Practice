for i in range(1,11):
    for j in range(1,11):  # Column ---Horizontal
        if i*j < 10:
            print(' ', 1.6*j,' ', end=" ")
        else:
            print(1.6*j,'  ', end=" ")
    print()