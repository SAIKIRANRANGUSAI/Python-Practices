"""
identity is used to compair the objects and find wether they belongs to same memory or they are sharing the memory.
        -> is, is not
          ->The 'is' operator evaluates to True if both the operand objects share the same memory location.
                use id() to find the id
            The list or tuple contains the memory locations of individual items only and not the items itself.
            Hence "a" contains the addresses of 10,20 and 30 integer objects in a certain location which may be different from that of "b".



"""
a = [1,2,3,4]
b = [1,2,3,4]   # both a and b are having samevalues butthey are not same but the indivudal is same like b[0] and a[0] is same
c = a
print(a is b) # false
print(a is c)  # true
print(id(a))  #2629294444544  a and c id are same
print(id(c))  #2632568295424
print(id(b))  #2629295896192

print(id(a[0]), id(b[0]))  # both the a and b 0 indexing value location is 140733004899112 140733004899112
print(a[0] is b[0])  #True