n = 19
if n<= 1:
    print("not prime")
else:
    for i in range(2,n):
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            print(i)
