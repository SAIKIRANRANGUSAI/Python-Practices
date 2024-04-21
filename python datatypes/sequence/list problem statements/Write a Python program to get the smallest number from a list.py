n = input("enter numbers: ")
na = list(map(int,n.split()))
s = na[0]
for i in na:
    if i < s:
        s = i
print(s)