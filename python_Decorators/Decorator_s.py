"""
    Decorators: Decorators is a function that takes places in another function and returning it
      by adding some functionalities without modifing the original function.
   -> Decorator is a design pattern that allows you to modify the functionality of function by wapping it
      in another function.
   -> The outer function is called the decorator

      """
def sai(func):
    def star(*a,**ka):
        print("*"*12)
        func(*a,*ka)
        print("*"*10)
    return star

@sai
def rangu(mes):
    print(mes)
rangu("hello")