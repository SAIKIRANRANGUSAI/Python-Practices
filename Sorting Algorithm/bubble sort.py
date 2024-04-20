n = input("please enter a list of numbers: ")
new = list(map(int,n.split()))
for i in range(len(new)):
    for j in range(len(new)-1-i):
        if new[j] > new[j+1]:
            new[j],new[j+1] = new[j+1],new[j]
print(new)
