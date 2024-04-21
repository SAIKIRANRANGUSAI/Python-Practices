a = input("please enter numbers: ")
na = list(map(int,a.split()))
n = 0
for i in na:
    if i>n:
        n = i
print("largest number in list is {}".format(n))
