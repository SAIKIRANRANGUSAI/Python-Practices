"""
recursion: A function calling itself untill a base condtion is true to produce an correct output
        -> same as function

"""
def sai(n):
    if n>0 and n==1:
        return 1
    elif n == 2:
        return 2
    else:
        return n*sai(n-1)
result = sai(5)
print(result)
