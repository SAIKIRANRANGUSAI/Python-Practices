ls = input("enter values: ")
sai = list(map(int,ls.split()))
for step in range(len(sai)):
    min_index = step
    for i in range(step+1, len(sai)):
        if sai[i]<sai[min_index]:
            min_index = i
    sai[step],sai[min_index] = sai[min_index],sai[step]


print(sai)