# list comprehension offers a shorter syntax when you want to create a new list based on the values of existing list.
sai = ["a","e","k","h","i","l"]
new = [x for x in sai if x not in "aeiou"]
print(new)

# print square roots of given number
n = list(map(int, input("Please enter the numbers separated by spaces: ").split()))
square = [x**2 for x in n]
print(square)
print(n)

#nasted list comparistion- nasted for loop
a = [1,2,35]
b = [4,5,7]
nnew = [(x,y) for x in a for y in b]
print(nnew)  # [(1, 4), (1, 5), (1, 7), (2, 4), (2, 5), (2, 7), (3, 4), (3, 5), (3, 7)]

# conditional ststemeents
list1=[x for x in range(0,21,2) if x%2==0]
print (list1)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]