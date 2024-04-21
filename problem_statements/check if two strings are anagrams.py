a = "python"
b = 'thopyn'
c = list(a)
c1 = c.sort()
d = list(b)
d1 = d.sort()
if c1 == d1:
    print("It's a anagram")
else:
    print("It's not a anagram")