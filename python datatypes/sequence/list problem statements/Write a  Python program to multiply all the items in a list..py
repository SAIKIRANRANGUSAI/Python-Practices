a = input("emter numbers: ")
na = list(map(int,a.split()))
m = 1
for i in na:
    m*=i
print(m)