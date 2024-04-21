a = (1, 2, 3, 5, 2, 7, 3, 7, 9, 4, 3, 6, 1)
b = dict.fromkeys(a)

c = {}  # Dictionary to store counts
for i in a:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

for key, value in c.items():
    print(key, ":", value)
