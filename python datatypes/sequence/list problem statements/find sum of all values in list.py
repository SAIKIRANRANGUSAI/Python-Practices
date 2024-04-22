a = input("enter values: ")
na = list(map(int,a.split()))
emp = 0
for i in na:
    emp+=i

print(emp)