sai = "sai kiran rangu6"
kiran = sai.split()
c =[]
for i in kiran:
    if len(i) > len(c):
        c = i
print(c)