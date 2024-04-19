n = input("enter some words: ")
na= list(n.split())
c = 0
for i in na:
    if len(i)==2 or i[0]==i[-1]:
        c+=1
print(c)