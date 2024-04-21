sai =" sai kiran rangu"
dictno_ry = {}
for i in sai:
    if i not in dictno_ry:
        dictno_ry[i] = 1
    else:
        dictno_ry[i] +=1
print(dictno_ry)

for x,y in dictno_ry.items():
    if y == 1:
        print(x)
        break


