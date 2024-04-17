a = [1,2,3,4,5]
b = [1,5,7,8,8]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)