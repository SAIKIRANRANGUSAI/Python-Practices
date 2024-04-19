a = input("please enter numbers: ")
na = list(map(int,a.split()))
n = 0
s = 0
for i in na:
    if i>n:
        n = i

for i in na:
    if i<n:
        s =i
print(s)

