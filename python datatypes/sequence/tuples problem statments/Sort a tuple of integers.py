s = (1,3,3,5,3,6,3,7,8,86,4,4)
sai = list(s)
for i in range(len(s)):
    for j in range(len(sai)-1-i):
        if sai[j] > sai[j+1]:
            sai[j],sai[j+1] = sai[j+1],sai[j]
s = tuple(sai)
print(s)