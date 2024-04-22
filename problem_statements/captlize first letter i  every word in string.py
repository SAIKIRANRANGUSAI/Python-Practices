sai = "sai kiran rangu is cool"
rangu = sai.split()
emp =[]
for i in rangu:
    if i not in emp:
        emp.append(i.capitalize())
sai =" ".join(emp)
print(sai)