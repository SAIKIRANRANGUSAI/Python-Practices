n = 11
isprime = True
if n<=1:
    isprime = False
else:
    for i in range(2,n):
        if n%i==0:
            isprime = False
            break


if isprime:
    print("its a prime")
else:
    print("its not a prime number")

#while loop
num = 12
is_prime = True
if n <= 1:
    is_prime = False
else:
    i = 2
    while i<=n:
        if n%i==0:
            is_prime = False
            break
        i+=1
if is_prime:
    print("its a prime")
else:
    print("its not a prime")


