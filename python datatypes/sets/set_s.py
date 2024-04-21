"""
    Sets: sets are collection of items which is immutable and unorder and no dublicate values.
    ->  we can store different datatypes in sets.
    -> we can convert list,tuple,strings,dict to sets
    -> if we enter dublicate values in sets but it will print unique values only
    -> we can chcek elements present in sets or not by using "in" :keyword
    ->set is not a sequence data type,
       its items cannot be accessed individually as they do not have a positional index (as in list or tuple).
       if we want to access use loops
   -> we can add elements by using "add" keyword but we can only one at a time.
   -> we can add two sets by using "update" keyword we can also add any iterable.
   -> we can join two set by using"|" like c = a|b , | is ued as union operator
   -> "unique" also used to combine the sets
   -> we can add two sets by unpacking like c = {*a, *b}
   -> use "remove" for removing the element from the set
   ->The "discard()" method in set class is similar to remove() method. The only difference is,
     it doesn't raise error even if the object to be removed is not already present in the set collection.
   -> remove random item in the set use pop()
   -> use clear if you want to remove all the values in set
   -> Remove Items that Exist in Both Sets use difference_update() remove common items
   -> use c = a.difference(b) to get non common items in new set we can say(a-b)
   -> use intersection_update() to get common items
   -> intersection() will return common items by createing new list
   -> symmetric_difference_update() will return all uncommon elemets in two sets
   -> symmetric_difference() this will create new set and get non common items in both sets
   -> "copy()" is used to copy the set like b = a.copy() both values are same but id is difference.
   -> operators in sets are union(|), intersection(&),a-b or b-a (to get uncommon),
      Symmetric Difference(^) getting uncommon in both sets and joining them in one
"""

# we can add items by using "add"

demoset = {1,2,3,4,5}
demoset.add("hello")
print(demoset)  # {1, 2, 3, 4, 5, 'hello'}

# adding two set or set+ any iterable by "update"
a1 = {1,2,3,"saikiranb"}
a2 = (1,2,3,4,"kiram")
a1.update(a2)
print(a1)  # {1, 2, 3, 4, 'saikiranb', 'kiram'}

# adding using union(|)
res2 = a1|demoset
print(res2)  # {1, 2, 3, 4, 'kiram', 5, 'saikiranb', 'hello'}

# we can use unique to add two sets
x = {1,2,3,4}
y = {4,5,6,7,8}
z = x.union(y)
print(z)

# adding by unpacking
unp = {*x,*y}
print(unp)  # {1, 2, 3, 4, 5, 6, 7, 8}

# removing an elemnet from set
rem = {1,2,3,4,5}
rem.remove(3)
print(rem)  # {1, 2, 4, 5}
#discar it willl not get error if not find
rem.discard(4)
print(rem) # {1, 2, 5}


# accessing the sets
sai = {1,3,4,5,7,6,6}
for i in sai:
    print(i,end=" ")
print()


# converting iterables to set
a = (1,2,32,34,32)
b= [1,2,3,4]
c = "saikiran"
d = {"name":"sai","age":23}
a_s = set(a)
bs = set(b)
cs = set(c)
ds = set(d.values())
print(a_s) # {32, 1, 2, 34}
print(bs) # {1, 2, 3, 4}
print(cs) # {'i', 's', 'a', 'n', 'r', 'k'}
print(ds) # {'sai', 23}


# difference_update() is used to remove common items in one list
hello = {1,2,3,4,5}
hai = {1,3,7,8,"sai"}
hello.difference_update(hai)
hai.difference_update(hello)

print(hai)  # {1, 3, 7, 8, 'sai'}
print(hello)  # {2, 4, 5}

# difference() same as difference_update() but creating in new list
result_diffe = hello.difference(hai)
print(result_diffe)  # {2, 4, 5}

# intersection_update(obj) only return common values

inter1 = {1,2,3,4}
inter2 = {3,4,5,6}
inter1.intersection_update(inter2)
print(inter1) # {3, 4}

# intersection(obj) only return common values by creating new set
result_inter = inter2.intersection(inter1)
print(result_inter)  # {3, 4}

# symmetric_difference_update(obj) is used to get unique values in both a and b
sym1 = {1,2,3,4}
sem2 = {3,4,5,6}
sem2.symmetric_difference_update(sym1)
print(sem2)  # {1, 2, 5, 6}

#symmetric_difference() get a,b unique value by creating new set
result_sem = sym1.symmetric_difference(sem2)
print(result_sem) # {3, 4, 5, 6}