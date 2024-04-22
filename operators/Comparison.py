"""
    Comparison: Comparison operators are used in many ways conditional statemnets, loops .

    in complex numbers Python doesn't support < and > operators,
    however it does support equality (==) and inequality (!=) operators.

    we can comapir two list but we can't compair list and tuple even it has same values it will return False.

"""
a = 5
b = 10
c = 5.0
c1 = 5.6
d = 3+6j
d1 = 6+8j
print(a==b)     # False
print(a<=b)     # False
print(a>=b)     # False
print(a!=b)     # True
print(c==a)     # True compairing int and float
print(c<=c1)     # True
print(c>=c1)     # False
print(c!=c1)     # True
print(d == d1)     # False
print(d!=d1)    #True
#print(d<=d1)   '<=' not supported between instances of 'complex' and 'complex'
# print(d<d1)  raise an exception

# comparing boolane values
x = True
y = False
print(x==y)   #False
print(x!=y)  # True
print(x<=y)  #False
print(x>=y)  #True

sai = [5,6,7,8]
kiran = [1,2,3,4]
rangu = (1,2,3,4)
print(sai==kiran) #False
print(sai==rangu)  #False

#compairing strings
rsk = "sai"
rs = "hai"
print(rs==rsk) #False because h will come fast so false

# dictionary comaparision
daa = { "name" : 'sai', "age": 23
}
db = {"name":"hai", "age":23}
print(daa==db)  # false alphabet order is wrong

