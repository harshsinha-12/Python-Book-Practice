n = input("Enter the 1st time:")
n2 = input("Enter the 2nd time:")
t1 = int(n)
t2 = int(n2)
if t1 > t2:
    f = t1 - t2
    s = str(f)
    print(f"Difference in time is {s[1:2]} hours and {s[2:4]} minutes")
else:
    f = (2400 - t2) + t1
    s = str(f)
    print(f"Difference in time is {s[1:2]} hours and {s[2:4]} minutes")    
    t1 = input("Enter the 1st time (in military format, e.g. 0900): ")
    t2 = input("Enter the 2nd time (in military format, e.g. 1730): ")

    h1, m1 = int(t1[:2]), int(t1[2:])
    h2, m2 = int(t2[:2]), int(t2[2:])

    if h1 > h2 or (h1 == h2 and m1 > m2):
        h2 += 24

    minutes = (h2 - h1) * 60 + (m2 - m1)
    hours, minutes = divmod(minutes, 60)

    print(f"Number of hours and minutes between the two times: {hours} hours and {minutes} minutes")
