
"""
    List are used to store multipule items of different datatypes in a single variable.
        -> its is a collection which the ordered and changable and allows dublicate. and it support indexing
        -> indexing startes with [0].
        -> if you want add new item in list it will add at end by append()
        -> use insert to add the item using index like insert(2,"sai")
        -> use pop if you want to delete an item use indexing or by default it will delete the last one item[-1].
        ->use remove for removing paticular item in list like sai.remove("banana") if there is two values it will remove starting.
        -> use del for deleting through indexing like del sai(0) if we not specify anything it will delete entire list
        -> clear is used to clear all the data in the list.
        ->In list we can use any type of data like[1,3,4,"sai",True]
        ->we can change the item through indexing like sai[2] = "rangu"
        -> if we want to add two lists then use (+) for same iterable like use extend for different iterable
        -> List comparishion: it offers  shortest syntax to create new list based on the values of existing list
            sai = [x for x in kiran if x % 2 == 0]
        -> sort is used to rearrange the items in order by default it will take assending order by left to right.
            used for reverse a.sort(reverse=True)
        -> copy is used to copy the list
            a = [5,3,4,567,2,"saiki"]
            b = a.copy()
            print(id(a))
            print(id(b))

"""

sai = [1,2,3,4,"sai","kiran",True]
print(sai)   # [1, 2, 3, 4, 'sai', 'kiran', True]
#looping through list

for i in sai:
    print(i, end=" ")  # 1 2 3 4 sai kiran True
print()

# Creating a list
ls = [1,2,3,5,"sai",True,4.0]
print(ls)

#add items using append(add at ending)
ls.append("hello")
print(ls)   # [1, 2, 3, 5, 'sai', True, 4.0, 'hello']

 # add by using insert(its will add by indexing)
ls.insert(2,"hai")
print(ls)   # [1, 2, 'hai', 3, 5, 'sai', True, 4.0, 'hello']


# update or modify the values in list
ls[1] = "hm"
print(ls)  # [1, 'hm', 'hai', 3, 5, 'sai', True, 4.0, 'hello']
# we can update by varibale also
ls2 = [1,"aljkdha",4,5,6,"skanhs",85]
ls[1:3] = ls2
print(ls)  # [1, 1, 'aljkdha', 4, 5, 6, 'skanhs', 85, 3, 5, 'sai', True, 4.0, 'hello']

# modifify list by adding 4 items in 1:3 in two values
ls[1:3] = [1,4,"saiki","rangu"]
print(ls) # [1, 1, 4, 'saiki', 'rangu', 3, 5, 'sai', True, 4.0, 'hello']

# pop will delete by indexing if we not specify then it will delete last item.
ls.pop(2)
print(ls)  # [1, 1, 'saiki', 'rangu', 3, 5, 'sai', True, 4.0, 'hello']
ls.pop()
print(ls) # [1, 1, 'saiki', 'rangu', 3, 5, 'sai', True, 4.0]

# remove will delete by value (ls.remove("sai")). if the value not found in list then it will get valueError
ls.remove("saiki")
print(ls)  # [1, 1, 'rangu', 3, 5, 'sai', True, 4.0]

#del is used to delete items using indexing it can delete by using slicing.
# if we not specify values then entire list will detete
del ls[1:3]
print(ls)

# clear is used to clear entire list
ls.clear()
print(ls)   # []

# extend is used to join the list and tupple
# we can add two lists by add keyword but if we want to add kistband tuple use extend

a = [1,23,34]
b = [5,5,"djsd","djksgd"]
c = (1,34,5,6,4,"sai")
a = a+b
print(a)  # [1, 23, 34, 5, 5, 'djsd', 'djksgd']
b.extend(c)
print(b)  # [5, 5, 'djsd', 'djksgd', 1, 34, 5, 6, 4, 'sai']