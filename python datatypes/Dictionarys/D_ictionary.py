"""
    Dictionarys: are used to store data values as key:value pairs
        -> It is ordered and changeble only values and no dublicates keys allowed
        -> each key and value is saprated by : like "name":"sai" and each pair is saparated by ,
        -> keys are unique but values may not.
        ->The values of a dictionary can be of any type,
           but the keys must be of an immutable data type such as strings, numbers, or tuples.
        -> Only a number, string or tuple can be used as key
        -> if we repeat key more than one time but iyt will only take once pair
        -> we can access the values by keys by slicing name with key sai["name"] or by get like sai.get("age")
        -> we can add new pair if not exists if pair is there then we can change values
        -> we can update values by keys
        -> use del to delete entire dict if you specify any key then that key will delete
        -> use pop  to delete a pair by key like sai.pop("age") we should use key or else not possible
        -> we can use popitem() to delete last pair in dict it dose not take any argument by default delete last pair
        ->There are two important points to remember about dictionary keys −
            (a) More than one entry per key not allowed. Which means no duplicate key is allowed.
            When duplicate keys encountered during assignment, the last assignment wins.
             (if there is two same keys then last key will print)

             (b) Keys must be immutable. Which means you can use strings, numbers or tuples as
             dictionary keys but something like ['key'] is not allowed(list and sets are not allowed)
        -> convert sets to dict use dict.fromkeys(sai)
        -> we can create empty dict by two type sai={} and sai = dict()
        -> To change the key in dict first take new key = old key then del or pop old key
                    sai["new_key"] = sai["old_key"]
                    sai.pop["old_key] or del sai["old_key"]
        -> use "update" for join another dict to execting dict but only gives unique values.
        -> we can use update for update the values if not there then add new pair like sai.update(age=55)
                we should not use "" for string in update values.
        -> we can add two dict by unpacking but we sholud use two ** like c = {**sai, **k}
        -> we can use union to add two dict c = a|b
        -> use |= to join to existing dict like a |= b
        -> to get the pair we get by dict name or by name.items()
        -> to get keys or values use sai.keys or sai.values
        -> we can loop through dict by direct name or by name.items() or by name.key() or
        -> we can use nased dict

        ->
"""

d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)
print(d1["Fruit"]) # ['Mango', 'Banana']
#print(d1["Mango"]) if we use values to acces key we'll get error mesage.

# adding new pair
d1["age"] = 23
print(d1) # {'Fruit': ['Mango', 'Banana'], 'Flower': ['Rose', 'Lotus'], 'age': 23}

# updating the value using key
d1["age"] = 22
print(d1) # {'Fruit': ['Mango', 'Banana'], 'Flower': ['Rose', 'Lotus'], 'age': 22}

# delete one pair in dict
del d1["age"]
print(d1) # {'Fruit': ['Mango', 'Banana'], 'Flower': ['Rose', 'Lotus']}


# nasted dict
hello ={
    "sai": {"name": "kiran", "age": 23},
    "kiran": {"name":"kiran","age":24}
}                       # {'name': 'sai', 'age': 23}
                        # {'name': 'sai', 'age': 23}

print(hello)