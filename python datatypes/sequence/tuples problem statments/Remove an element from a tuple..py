n = (1,2,3,4,5,6,7,8)
l = list(n)
num = 4
for i in l:
    if i == num:
        l.remove(i)
n = tuple(l)
print(n)
