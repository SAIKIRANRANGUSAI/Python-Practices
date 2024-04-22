"""
    A function is a block of code that performs a specific task it only runs when it called.
        -> function can return data as a result.
                -> ends the execution of the function
                -> returns a value to the function call
                -> returns the control of the program to the function call
        -> function is defined using 'def' keyword.
        -> You can pass data knows as parameters in to function.
        -> A parameter is a variable listed  inside the parentheses in function defination.
        ->  A argument is the value that send to the function
            Arguments are inputs given to the function
            we can specify default arguments in parameters like (name = "sai")
            if we not send arugemt tofunction it will take default values it will not give error.
        -> WE should create a variabel to call function when we use return statement only or use print().
        -> *args allows a function to take any number of positional arguments.
        ->  **kwargs allows the function to accept any number of keyword arguments.(like dict)
"""
def sai(hello):
    print("hello",hello)

sai("sai")

# returning the values
def kiran(a,b):
    sum = a+b
    return sum

result = kiran(3,4 )
print(result)
print(kiran(5,6))