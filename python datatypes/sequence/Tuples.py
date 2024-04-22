"""
    Tuples is a collection of data items of different data types
    which is ordered and unchangeable allows dublicate.
    -> for empty tuples just used () pantatis but for single item use , (44,)
    ->To access values in tuple, use the square brackets for slicing along with the index or
      indices to obtain value available at that index. For example
        tup1 = ('physics', 'chemistry', 1997, 2000)
        tup2 = (1, 2, 3, 4, 5, 6, 7 )
        print "tup1[0]: ", tup1[0]
        print "tup2[1:5]: ", tup2[1:5]
    -> Tuples are immutable which means you cannot update or change the values of tuple elements.
     but you can add two tuples
     -> we can delete a tuple by 'del' keyword but after deleting we can't see the tuple
     -> can't delete items or values in tuple but we can delete entire tuple.
     -> slicing and indexing is possible same as a list.
     -> if we not specify pantasis or square brazes then default it will be tuple
            sai = 'sai',"kiran","rangu",1,3,54,56,7
        now sai is a tuple by default
    -> we can convert list to tuple and dict and also string to tuple by using tuple()
            s = tuple(a)
    -> tuple is mutable we can't update values if we update then we get typeError.
    -> if you want to update tuple then convert into list and update and convert into tuple
       but after converting into tuple the id will change that means new tuple is created existing tuple ramain same.
   -> unpacking - sai = (1,2,3)
                 x,y,z = sai # x = 1, y = 2, z = 3
    -> count is used to find the occurance sai.count("sai")
    -> methods used = del,update,+,*


"""
# creatingh a tuple
sai = (1,2,3,"saikiran",True,"rangu")

#index and slicing in tuple
print(sai[0]) # 1
print(sai[0:3])
# reverse s tuple
print(sai[::-1])
kiran = "sai","kiran",1,2,3  # kiran is also a tuple
# adding tow tuples
print(sai+kiran) # (1, 2, 3, 'saikiran', True, 'rangu', 'sai', 'kiran', 1, 2, 3)

# we can delete entire tuple but not items in tuple
del kiran # if we print kiran we will get error because kiran is not there del will delete entire tuple

#updating tuple by converting into list
print(id(sai))
kiran = list(sai)
kiran[1] = "hello"
sai = tuple(kiran)
print(sai)  # (1, 'hello', 3, 'saikiran', True, 'rangu') we updated but not in same sai we creted a new tuple
print(id(sai)) # 2161053299328 != 2161055541920 two ids are different

# unpacking and with *
rangu = 1,2,3
a,b,c = rangu
print(a,b,c) # 1 2 3

rsk = (1,2,3,4,5)
x,*y,z = rsk
print(y)  # [2, 3, 4] in this senario x will tke one value zz will take one value but *y will tahek remaining all values

# convering dict to tuple and list to tuple
ls = [1,2,3,4]
print(ls)
lst = tuple(ls)
print(lst)  # (1, 2, 3, 4)

#dict to tuple
dis = {"name": "sai","age":23}
print(dis)
dist = tuple(dis.values())
print(dist) # it will only print the keys default if we specify values() then values print

sets = {1, 2, 3, 4, 54, 3} # {1, 2, 3, 4, 54} it will remove dublicate values
print(sets)
setst = tuple(sets)
print(setst)   # converted sets to tuples
