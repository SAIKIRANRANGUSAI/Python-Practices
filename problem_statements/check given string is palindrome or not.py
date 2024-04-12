sai = "sas"
kiran = sai[::-1]
if sai == kiran:
    print("it's is palindrome")
else:
    print("It's is not a palindrome")

#another way
num = 1221

rangu = num
rev = 0
while (num>0):
    rem = num%10
    rev = rev*10+rem
    num = num//10

if rangu == rev:
    print("it's is palindrome")
else:
    print("It's is not a palindrome")
