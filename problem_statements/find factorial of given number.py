n = 4
f = 1
if n == 0:
    print(0)
elif n ==1:
    print(1)
else:

    while n>1:
        f = f*n
        n -=1
print(f)

n1 = 3
fi = 1
# using for loop
for i in range(1,n1+1):
    fi = fi*i
print(fi)

#using function
def sai(num):
    if num ==0:
        return 0
    elif num ==1:
        return 1
    else:
        fac = num*sai(num-1)
        return fac
n = sai(5)
print(n)

#recursive function

def rec_fac(numb):
    if numb == 0:
        return 0
    elif numb == 1:
        return 1
    else:
        return numb*rec_fac(numb-1)
rf = rec_fac(6)

print(rf)
