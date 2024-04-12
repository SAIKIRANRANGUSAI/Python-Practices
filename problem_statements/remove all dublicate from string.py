sai = "saikiran rangu is cool"
emp = []
for i in sai:
    if i not in emp:
        emp.append(i)
sai = ''.join(emp)
print(sai)