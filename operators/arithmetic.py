"""
python uses symboles for basic arithmetic operators

    Arithmetic operators are binary operators in the sense they operate on two operands. Python fully supports mixed arithmetic.

        int with float = float
        int or float with complex = complex
        int with str = str
        float will not support in string
        <, > will not support in  complex
        two complex can't module(%)
        Complex class in Python doesn't support the modulus operator (%) and floor division operator (//).
"""
a = 3
b = 5
c = 4.0
c2 = 7.0
d = 4+6j
d2 = -3+7j
f = 3.0
e = 6.75E-3  #(E-3 = 10 to the power of -3  = 0.00675)
print(a+b)   # int+int = int  8
print(a+c)   # int + float = float 7.0
print(a+d)   # int + complex = (7+6j) = complex
print(a-b)  # -2
print(a-c)   # -1.0  int - float
print(d-d2)  # (7-1j)  complex-complex(-*- = +)
print(a-e)  # int * float = float  2.99325
print(d*d2)   # comp * comp = (-54+10j)
print(a/b)   # 0.6 int / int = float
print(b//a)  # 1 int // int = int
print(c//f)  # 1.0 = float // float = float
print(c/f)   # float / float = float upto 15
print(a/c)   # 0.75
print(a/d)   # (0.23076923076923078-0.3461538461538462j)
print(d/d2)  # complex / complex is possible but %  and  // is not poaaiblw
#print(d%d2)  unsupported operand type(s) for %: 'complex' and 'complex'

