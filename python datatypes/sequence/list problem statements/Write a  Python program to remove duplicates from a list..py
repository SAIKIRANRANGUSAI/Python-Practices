n = input("enter: ")
na = list(n.split())
c = na.copy()
print(c)
a = []
for i in na:
    if i not in a:
        a.append(i)
    else:
        c.remove(i)
print(c)
