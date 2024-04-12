# variables are cointainers used to store the data values
  # "name given to memory location" that used to hold the data values
  # varibale name is know as identifier

"""
Rules: variable name can start with lower or upper case
       its is a case sentence( sai and Sai are not same )
       variable name should be in single word
       we can use (_) underscrole to better understanding like sai_kiran
       varibale name should not be a keywords
       variable name should not start with number
       Cannot contain special characters such as !, @, #, $, %, etc. (except underscore).

    variable name can writen in two ways :
       Snake case:
                -> Variable names consist of lowercase letters. can't use upper because upper is constant
                Words within the variable name are separated by underscores (_).
                It is commonly used for naming variables, functions, and other identifiers in Python.
                For example, sai_kiran follows the snake case convention, where sai and kiran are separate words separated by an underscore (_) and written in lowercase letters.

                Using snake case helps improve the readability of the code by making variable names more descriptive and easy to understand.
        camel case: 2 types lower and upper camel case:
                -> All the words starting char will be upper  except the first one.(saiKiranRangu)
                -> All the starting char will be starting with captal.(SaiKiranRangu)
                ->both forms of camel case, the first word starts with either a lowercase letter or an uppercase letter, depending on the convention used, and subsequent words start with uppercase letters.
"""
sai = 10 #case sentence
Sai = 20
print(sai) #op:10
print(Sai) #op: 20
# we can change the variavle after been set
a = 15
a = 25
print(a) #op: 25

# casting : if we want to specify the data of variable, this can done by casting
x = int(10)
y = float(20)
z = str("sai")
print(x,y,z) # op: 10 20.0 sai

# Type casting:
  #  it is nothing by changing the paticular datatype of the varibale to another data type
a = int(5)  # 5
a = float(5) #5.0  "overwriting"
b = float(a) # 5.0
c = str(a)  #5
print(a)
print(b)
print(c)

# check type of variables
a = 5
print(type(a))  # <class 'int'>

# multipule variables
a,b,c = 10,20,30
print(a) # 10

# unpickling: it is nothing but
sai = 10,20,30
r,s,k = sai
print(r,k,s) #10 30 20
