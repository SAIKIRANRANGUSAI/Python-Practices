def sai(sai):
    if len(sai) % 2 == 0:
        return sai[::-1]


input_user = input("enter something")
print(sai(input_user))