"""
    Generator:a generator is a function that returns an iterator that produces a sequence of values when iterated over.
        -> Generators are useful when we want to produce a large sequence of values,
            but we don't want to store all of them in memory at once.
        -> The "yield" keyword is used to produce a value from the generator
            and pause the generator function's execution until the next value is requested
        -> we can also print all values with using for loop or using next(sai)
        ->  Generator Expression: same as list comparison but insted of creating new list it will create
          generator object that can be iterated over to produce the values in the generator.
                squares_generator = (i * i for i in range(5))
        -> 
"""
def sai(n:int):
    for i in range(n**n):
        yield i
if __name__ == '__main__':

    result = sai(6)
    print(next(result))
    print(next(result))
    for i in result:
        print(i)
        if i == 13:
            break
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))