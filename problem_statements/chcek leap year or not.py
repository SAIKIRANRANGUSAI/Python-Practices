n = int(input("Please enter year which you want wether it's an leap year or  not: "))
if n%4 == 0:
    if n%100 == 0:
        if n%400 == 0:
            print(" I'ts an leap year")
        else:
            print("its not a leap year ")
    else:
        print("its an leap year")
else:
    print("its not a leap year")

