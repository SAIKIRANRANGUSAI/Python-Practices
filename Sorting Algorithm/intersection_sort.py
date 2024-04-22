ls = input("enter values: ")
sai = list(map(int,ls.split()))
for i in range(len(sai)):
    key = sai[i]
    j = i-1
    while j>=0 and key < sai[j]:
        sai[j+1]  = sai[j]
        j-=1
    sai[j+1] = key

print(sai)
