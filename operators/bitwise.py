"""
bitwise operators are normally used to perform bitwise operations on integer-type objects.

to find binary number number use bin(a)
    -> AND and or and NOT(~): same as and in logical
            0 & 0 is 0      0
            1 & 0 is 0      1
            0 & 1 is 0      1
            1 & 1 is 1      1
    -> in XOR(^) if both true or both false then false
    0 ^ 0 is 0
    0 ^ 1 is 1
    1 ^ 0 is 1
    1 ^ 1 is 0

    -> Bitwise left and right(<<, >>) it is nothing but moving with index number
        a = 60 -> 00111100
        print(a<<2) # moving with indexing 2
        a = 60 -> 00111100
            2<<   11110000 = 240
        a = 60 -> 00111100
           2>>    00001111 = 15

"""
a = 60
b = 13
print(bin(a))
print(a&b) #12
"""
a = 60 -> 111100  
b = 13 -> 001101
ans =     001100   = 12         
"""
print(a|b)
"""
a = 60 -> 111100  
b = 13 -> 001101
ans =     111101   = 61 
 """
print(bin(61))  # 0b111101

""" binary XOR (^) 
a = 60 -> 111100  
b = 13 -> 001101
ans =     110001   = 49
"""

print(a^b)  #0b110001 49
print(bin(49))


print(~b)  # b values isn 13 but hera we are reversing the value


print(a<<2)  #240 it will give direct number
print(a>>2)  # 15

