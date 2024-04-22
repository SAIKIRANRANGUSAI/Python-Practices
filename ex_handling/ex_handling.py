def sai():
    user_input = input("enter a number: ")
    try:
        number = float(user_input)
        print(number)
    except Exception as e:
        print(e)
        sai()

    else:
        print("try is  working")
    finally:
        print("end of the program")

sai()