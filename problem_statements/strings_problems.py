# write a python program to calculate the length of the String:
sai = "sai"
print(len(sai)) # 3
print("another way")
c = 0
for i in sai:
    c+=1
print(c)  #3

# write a program to count the nuber of char in a string

s = 'google.com'
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
print("another way")
lis = ''
c = []
for i in s:
    if i not in lis:
        lis+=i
        c.append(1)
    else:
        ind = lis.index(i)     # {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        c[ind]+=1
result = dict(zip(lis,c))
print(result)

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
sai = 'saikiranrangu' # i want to get sagu
print(sai[0:2]+sai[-2:]) #sagu


#4.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#String : 'restart'
#Expected Result : 'resta$t'
sai4 = "saikiransai"
first = sai4[0]
m = first
for i in sai4[1:]:
    if i == first:
        m +="$"
    else:
        m +=i
print(m)   #saikiran$ai

#5.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

a,b = 'xyz', 'abc'
c = a[:2]

d = b[:2]
c,d = d, c
new = c + a[2:]
newb = d + b[2:]

print(new, " ", newb)  #abz   xyc

#6  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
"""Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""
sai6 = 'helloing'
if len(sai6) >=3 :
    if sai6[-3:] != "ing":
        print(sai6+"ing")
    else:                    #helloingly
        print(sai6+"ly")

#7.Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'
s7 = "The lyrics is not that poor!"
f = s7.find("not")
f1 = s7.find('poor')
print(f,f1)
if f < f1:
    print("The lyrics is good!")
else:
    print("The lyrics is poor!")

#8.Write a Python function that takes a list of words and return the longest word and the length of the longest one.
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9

def sai(hello: list):
    le = ''
    for i in hello:
        if len(i) > len(le):
            le = i
    return le

hello = ["sai", "kiran","Exercises"]
print(sai(hello))  #Exercises

#9. Write a Python program to remove the nth index character from a nonempty string
s9 = "saikiran"
n9 = 4
s9l = list(s9)
rs9 = s9l.pop(n9)
s9 = ''.join(s9l)   #saikran
print(s9)

#10 Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
s10 = "saiki"
res10 = s10[-1:] + s10[1:-1] + s10[:1]
print(res10)

#11 Write a Python program to remove characters that have odd index values in a given string.