for i in range(1,10): # Row ---- Vertical
    for j in range(1,10):  # Column ---Horizontal
        if i*j < 10:
            print(' ', i*j,' ', end=" ")
        else:
            print(i*j,'  ', end=" ")
    print()