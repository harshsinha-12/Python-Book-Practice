D = input("Enter date in MMDDYYYY format:")
DD = D[2:4]
Y = D[4:8]
M = int(D[0:2])
if M == 1:
    print(f"January {DD}, {Y}")
elif M == 2:
    print(f"February {DD}, {Y}")
elif M == 3:
    print(f"March {DD}, {Y}")
elif M == 4:
    print(f"April {DD}, {Y}")
elif M == 5:
    print(f"May {DD}, {Y}")
elif M == 6:
    print(f"June {DD}, {Y}")
elif M == 7:
    print(f"July {DD}, {Y}")
elif M == 8:
    print(f"August {DD}, {Y}")
elif M == 9:
    print(f"September {DD}, {Y}")
elif M == 10:
    print(f"October {DD}, {Y}")
elif M == 11:
    print(f"November {DD}, {Y}")
elif M == 12:
    print(f"December {DD}, {Y}")