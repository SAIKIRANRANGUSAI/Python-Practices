n = 5
for i in range(n,0,-1):
    print("* "*i)

# Another way
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


# Another way
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

n = 5
