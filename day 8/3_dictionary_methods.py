# get()
student = {"name": "Alex", "age": 30}
name = student.get("name")
print(name) #John

address = student.get("address", "PKR")
print(address) #"PKR"

name = student.get("name", "Alex")
print(name) # john


#keys()
student = {"name": "John" , "age" : 30,  "address": "KTM"}
print(student.keys())

#values
student = {"name": "John" , "age" : 30,  "address": "KTM"}
print(student.values()) 

#items()
items = student.items()
print(items) #dict_items(["name"])

# keys()
student = {"name": "Jon", "age": 30, "address": "KTM"}
print(student.keys())  # dict_keys(["name", "age", "address"])


# values()
print(student.values())  # dict_values(["Jon", 30, "KTM"])


# items()
items = student.items()
print(items)  # dict_items([("name", "Jon"), ("age", 30), ("address", "KTM")])