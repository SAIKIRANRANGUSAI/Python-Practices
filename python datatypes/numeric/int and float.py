"""
    Numeric: numeric datatypes stores the numeric data values(number)
        numeric datatypes are of three types:

                -> int(4)
                -> float(4.0) limit 15 digits
                -> complex(2+3j) 2 is real part and 3j is a imaginary part

        to find the datatype use type()

         computer programmers need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems.
         print(0b1101011)  # prints 107 binary

        print(0xFB + 0b10)  # prints 253 # hexadecimal

        print(0o15)  # prints 13  # octal

        To specify the ttype of the variable use casting.
"""
a = 10
b = 20.0
c = 30+5j
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>

# we can use _ between number its like we can add break in number.
j = 100_88_736327_234
print(j)
"""
   Type consersion: converting the varuable type of a paticular datatype to another data type is type consersion
   
 """

x = 5
y = 20.9
i = float(x)
j = int(y)
print(i) # 5.0 converted int to float
print(j) # 20 converted float to int


# genarating random numbers
import random
for _ in range(6):
    random_number = random.randint(1, 10)  # Generate a random integer between 1 and 100 (inclusive)
    print("random num is : ",random_number, end=" ")


print(1+2.9)  # 3.9
print(2*2.0) # 4.0
print(4.2/2)  # 2.1
print(4%2)  #  remainder = 0
print(2%4) #  if the value is small the it will print small value
print(2*"4") #44
print(2*"sai")  #saisai
print("sai"+"sai")  #saisai
#print("sai"*"sai") #can't multiply sequence by non-int of type 'str'
#print(2.0*"sai")  can't multiply sequence by non-int of type 'float'
print(2 ** 3)  # Output: 8
print(5 / 2)   # Output: 2.5
print(5 // 2)  # Output: 2


