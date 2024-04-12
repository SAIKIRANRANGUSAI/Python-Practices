sai = "sai kiran rangu"
dic_t = {}
for i in sai:
    if i not in dic_t:
        dic_t[i] = 1
    else:
        dic_t[i] +=1
coun_t = 0
for x,y in dic_t.items():
    if y > coun_t:
        coun_t = y
        z = x
print(z)



