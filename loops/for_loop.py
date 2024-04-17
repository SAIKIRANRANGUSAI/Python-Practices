# use for loop if you want to loop through a fixed numbers of elements
# for loop is used to iterate iterables
# With for loop we can execute a fixed set of statements once per each itsm in ietrable
# we can't iterate numbers directly. we should use range.


"""for i in range(0,10,2):
    print(i, end=" ")"""


# print right angle triangle
n = 5
for a in range(n):
    for b in range(0,a+1):
        print("*", end="")
    print()
