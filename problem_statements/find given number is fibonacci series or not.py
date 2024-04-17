n = 8
a = 0
b = 1
if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    for i in range(1,n):
        c = a + b
        a = b
        b = c
    print(c)

# using while loop with function
def sai(num):
    n1=0
    n2 =1
    if num ==0:
        return 0
    elif num ==1 or num ==2:
        return 1
    else:
        while num>1:
            fib = n1+n2
            n1 = n2
            n2 = fib
            num-=1
        return fib

res = sai(8)
print(res)

# witrh recusion
def kiran(z):
    if z ==0:
        return 0
    elif z ==1 or z ==2:
        return 1
    else:
        return kiran(z-1)+kiran(z-2)
result = kiran(8)
print(result)
