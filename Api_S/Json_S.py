"""
    JSON (JavaScript Object Notation) is a popular data format used for representing structured data.
      It's common to transmit and receive data between a server and web application in JSON format.

        Key points about JSON:
        -> String values should be enclosed in double quotation marks ("").
        -> Booleans should be represented in lowercase (true or false) and None also.
        -> You can convert Python objects of various types into JSON strings, including dictionaries, lists, tuples, strings, integers, floats, booleans (true and false), and None.


"""
import json

sai = {
    "names":[{"name1":"sai","name2":"kiran","name3":"rangu"}],
    "age":23,
    "color":"white",
    "man":True
}

# Convert the dictionary to a JSON string
sai_json = json.dumps(sai)

# Load the JSON string back to a dictionary
kiran = json.loads(sai_json)
print(kiran)
print(sai_json)
# only dict will access if we wamt to access the json object then convert it to dict and then you can access values
print(kiran["age"])
#print(sai_json["age"]) typeError
