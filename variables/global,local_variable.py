"""
 Global: The varibale that create outside the function is known as global varibale
        -> global variable can use both in and outside the function.
        -> if there is no local varibale in function so we can use global in function
"""
x = 5
def hello():
    print(x) # 5
hello()
"""
 Local: The varibale that are create inside the function is called local variables
   -> if we create same name variable inside the fun then indide the fun will run 
   -> if we want to use local variable outside the function use keyword global and variable name
"""
b = 'sai'
y = 'rangu'
def hi():
    global y
    y = 'kiran'
    print(b)  # sai
    print(y)  # kiran
hi()
print(y)  # kiran
