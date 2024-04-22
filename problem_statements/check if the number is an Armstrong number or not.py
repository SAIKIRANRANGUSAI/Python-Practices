n = int(input("please enter the numbers which you want to chcek: "))
sum = 0
lenghths = len(str(n))
temp = n
while temp>0:
    digits = temp%10
    sum +=digits**lenghths
    temp//=10
if n == sum:
    print("i'ts an armstrong number")
else:
    print("i'ts not an armstrong number")