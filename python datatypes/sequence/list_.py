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
"""

sai = [1,2,3,4,"sai","kiran",True]
print(sai)   # [1, 2, 3, 4, 'sai', 'kiran', True]
#looping through list

for i in sai:
    print(i, end=" ")  # 1 2 3 4 sai kiran True
for j in sai:
    if j%2==0:
        pass

