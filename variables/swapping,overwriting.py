"""
  Swapping is nothing but exchanging the values between two varibales

"""

a= 5
b= 6
c = 7

a,b,c = c,a,b
print(a,b,c) # 7 5 6

x = 10
y = 30
x,y = y,x
print(x,y) # 30 10
# can use nin another way
temp = a
a= b
b= c
c= temp
print(a,b,c) # 5 6 7 because its a 2nd swap

"""
 Overwrite is nothing but replacing the data or value with new one  in the same variable
 """
s = 10
print(s) # 10
s = 20
print(s) # 20