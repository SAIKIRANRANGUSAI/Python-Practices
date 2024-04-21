"""
        Errors: errors are the interoption of executing a program or code.
        Errors are the problems in a program due to which the program will stop the execution. On the other hand,
         exceptions are raised when some internal events occur which changes the normal flow of the program.

        Errors are of two types:
            -> syntax error
            -> logical error
            -> Runtime errors
         Syntax error:
                ->when the proper syntax of language is not followed then syntax error will occur
                -> It's a Compile-Time Errors

        logical errors:
                -> Logical errors occur when there's a flaw in your program's algorithm or logic.
                    like the logic is incorrect.
                -> occur when your code doesn't produce the expected output
                   because of a flaw in the algorithm or the overall logic of your program.
               -> logical errors don't generate error messages or exceptions.
                  Instead, your code runs without issues, but it doesn't achieve the intended results.

        runtime error :

                ->When in the runtime an error that occurs after passing the syntax test is called exception or logical type.
                  For example, when we divide any number by zero then the ZeroDivisionError exception is raised,
                  or when we import a module that does not exist then ImportError is raised.

              some of most commonly seen errors are
               -> TypeError	:It occurs when a function and operation are applied in an incorrect type.
               -> NameError	It occurs when the variable is not defined.
               -> ImportError	It occurs when an imported module is not found.
               -> MemoryError	It occurs when a program runs out of memory.
               -> IndexError	When the wrong index of a list is retrieved.
               ->
"""
"""a =  # SyntaxError: invalid syntax 
print(a)"""
#if a<b    SyntaxError: expected ':'
 #   print("hello")



