a = 134
rev = 0
while a>0:
    digits = a%10
    rev = rev *10+digits
    a = a//10
print(rev)
