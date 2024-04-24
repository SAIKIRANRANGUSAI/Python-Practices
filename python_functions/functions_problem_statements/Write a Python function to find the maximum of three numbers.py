def sai(a,b,c)->int:
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(sai())