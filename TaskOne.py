def input_int(tmin,tmax):
    print("Please, enter a number.")
    while True:
        usernumber = input()
        if not usernumber.isdigit():
            print("Please, enter a number, not a symbol!")
            continue
        usernumber = int(usernumber)
        checklist = range(tmin,tmax + 1)
        if usernumber in checklist:
            break
        else:
            print("Your number is out of limits")
            continue
    return usernumber
