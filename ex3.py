n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print("* ", end="")
    print()


print(" ")
for i in range(n+1, 0, -1):
    for j in range(i+1, 1,-1):
        print("* ", end="")
    print()


for i in range(n ,0 ,-1):
    for j in range(n):
        if j<n-i:
            print(" ", end='')
        else:
            print("* ", end="")
    print()