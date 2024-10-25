# Continue: when condition met then current ietartion will skip the present iteration
# and move to next iteration.

for i in range(5):
    if i ==3:
        continue
    print(i)
else:
    print("itsration is completed")