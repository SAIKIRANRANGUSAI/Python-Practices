#  break allows you to exit a loop when an external condition is met.

for i in range(10):
    print(i)
    if i ==5:
        break
print("done")

#with while loop
a = 0
while a<10:

    if a == 3:
        break
    print(a)  # now we are printing after the break statement so we will not print 3
    a+=1
print("done")
