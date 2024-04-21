sai = (1,2,3,4,5,5,6,7,8,9)
max = sai[0]
min = sai[0]
for i in sai:
    if i > max:
        max = i
    elif i< min:
        min = i
print(max)
print(min)
