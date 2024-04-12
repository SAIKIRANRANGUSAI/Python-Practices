"""
membership(in , not in) ->it checks wether an item present in and container or not Both return a Boolean result.
        ->in is reverse to not in
    it chcek wether a substring is present in the string or not

    Membership Operator with Dictionaries: only keys will work values will me false

"""
a = "sai"
print("s" in a) # true
print("k" in a) #false
print("lkadb" not  in a)   # true

# Membership Operator with Lists and Tuples
x = [10,20,30,40,50,60]
b = 10
c = 20
d = b-c
e = b*c
f = b/c
print(b in x) # True
print(d in x) # False
print(e in x) # False
print(f not in x) # true


# Membership Operator with sets
ver = {1,2,3,4,5,6}
x = 1
y = 4

print(x in ver) #True
var2 = {(1,4), 4,5,6,4}
print((x,y) in var2) #true

# Membership Operator with Dictionaries

dictt = {1:20, 2:40}
print(1 in dictt) #true
print(20 in dictt)#false