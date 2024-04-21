sai = "sai kiran rangu is cool"
di_ctonary = {}
for i in sai:
    if i not in di_ctonary:
        di_ctonary[i] = 1
    else:
        di_ctonary[i] +=1

print(di_ctonary)
emp = 0
for x,y in di_ctonary.items():
    if y > emp:
        emp = y
        res = x

print(res)
emp2 = 0
for x,y in di_ctonary.items():
    if y < emp and y > emp2:
        emp2 = y
        res2 = x
print(res2)