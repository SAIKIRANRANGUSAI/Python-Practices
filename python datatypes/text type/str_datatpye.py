"""
    string (str) : a string is a sequence of characters its is immutable(can't change) but we can replace
    if you want to update string then convert string into list and update and then convert back
     if we want to create string then use '' or "" or ''' '''
        string can be enclosed in either single quotes(' ') or double(" ") or thrible(''' ''').
            -> use single or double quotes for single line string
            -> for multiline string use thruble(''' ''')

        -> use uppercase letter for Constrants(unique value Should not change) but in python we can change.
              -> conatrants should not overwrite

      The .casefold() method returns a copy of a string with all characters in lowercase. It is similar to .lower(),
      but whereas that method deals purely with ASCII text, .casefold() can also convert Unicode characters.

  Methods used in string:
  -> upper, lower
  ->patition- saparte in string (line 45)
  ->rstrip, split - split done in list format
  ->replace, find
  -> index, replace, find(if not found then return -1), isnumeric(check if it is numeric or not)

        python does't have char.
"""
#accessing the char in string

sai = 'sai kiran'
print(sai[0]) #s
print(sai[3]) # it will print empty space becz we have empty space between the words
print(sai[0:2]) # sa
print(sai[0:-1]) # sai kira

# Indexing : allows you to access individual characters in a string directly
p = "sai kiran rangu"
print(p[2])  #  i, Single Character Indexing
print(p[1:-2])  # ai kiran ran ,Substring Slicing
k = p.index('i',1,5) #2 # finding a value in specic indexing number.
print(k)

rsp = "sai kiran rangu"
kkr = rsp.index("kiran", 2, 15) # 4 we can specify start and ending in string and also direct value
print("index",kkr)

kiran = 'sai kiran rangu'
rangu = kiran.split()  # use split()to saparate the string in list[,]
print("reverse:",rangu)
print(rangu[::-1]) # reversing the string op: ['rangu', 'kiran', 'sai']

# printing the string  by adding new string
a = 'sai kiran'
print(a[:3] +'rangu') # we can printing through indexing

# replace the str
a = 'saikiran, saikiran, saikiran'
sai = a.replace('sai','rangu', 1) # in this sanareio it will replace any once if there is multipe same items
print(sai)  # rangukiran

# string partition
h = "hello sai kiran rangu how are you doing"
print(h.partition('how'))   # its is saparting how from list : ('hello sai kiran rangu ', 'how', ' are you doing')


# chcek and no in

ss = "sai kiran rangu"
print("kiran" in ss) # true
print("kiran" not in ss)# Flase
#another way
if "sai" in ss:
    print("found") # return "found" if it satisfy if condition

# upper and lower and captlize(starting letter would be in captal if it captal then it will make lower)
# casefold(same as lower but it has a specific feture)
hh = "sai"
hhc =hh.capitalize()
print(hhc)
print(hh.upper()) #SAI


#escape string
rskk = "sai\'s birthday on 25th of marcch"
print(rskk) # sai's birthday on 25th of marcch

#string formate use string formate if we want add string + number
age = 23
#txt = "my age is " + age    (if we use this we'll get error so)
txt = "my age is {}"
print(txt.format(age)) # my age is 23

