day=str(input("enter the week day"))
time=float(input("enter the time"))
if day=="Monday":
    if time>=8.30 and time<=9.30:
        print("breakfast is poori sabzi")
    elif time>=12.30 and time<=14:
        print("lunch is sambar rice")
    elif time>=20 and time<=21:
        print("dinner is chicken rice")
elif day=="Tuesday":
    if time>=8.30 and time<=9.30:
        print("breakfast is poha")
    elif time>=12.30 and time<=14:
        print("lunch is rajma rice")
    elif time>=20 and time<=21:
        print("dinner is roti sabji")
