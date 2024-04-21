num = 12345

rev = 0
while num!=0:
    di = num % 10
    rev = rev * 10 + di
    num = num // 10
print(rev)
