n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# Another way
for i in range(1,n):
    print("* "*i)

