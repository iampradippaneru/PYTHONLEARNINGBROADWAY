# Dictionary is a mutable data type in python

a ={} # empty dictionary
print (a) #{}
a = dict()# built in function
print (a) #{}


#CREATING A NON EMPTY DICTIONARY 
a = { "name" : "john" , "age" : 30 }
print(a) # { "name" : "john" , "age" : 30 }

a = dict(name= "john" , age = 30)
print(a) # { "name" : "john" , "age" : 30 }

a = {"first_name": "john" , "last name" : "joe" }
print(a)

#a= dict{first name = "john" , last name = "joe"}
a = dict(first_name = "john", last_nme = "joe")


########### accesing dictionary element #####3
####### Accessing dictionary elements ##############
student = {"name": "Jane", "age": 30, "address": "KTM"}
address = student['address']  # a = [1, 2, 3, 4]  # a[3]
print(address)  # KTM
print(student["roll_no"])  # KeyError beacuse this is index calling

name = student.get("name")
print(name)  # Jane
print(student.get("roll_no"))  # None because this is method

#### Adding and Updating Dictionary elements
student = {"name": "Jane", "age": 30, "address": "KTM"}
student['roll_no']= 2 # adding in the dictionary
print(student) # {"name": "Jane", "age": 30, "address": "KTM" , "roll_no":2}

student["name"] = "Alex" #updating dictionary
print(student) # {"name": "Alex", "age": 30, "address": "KTM" , "roll_no":2}

student.update({"email" : "pradippaneru444@gmail.com"}, {"contact" : "9806573776"} )
print(student) # 

student.update(email = "pradippaneru444@gmail.com",contact= "9806573776" )
print(student) # 


# Removing Dictionary Elements
student={"name": "Jane", "age": 30, "address": "KTM",
         "email" : "pradippaneru444@gmail.com" , "contact" : "9806573776" }

contact = student.pop("contact")
print(student) # {"name": "Jane", "age": 30, "address": "KTM", "email" : "pradippaneru444@gmail.com" }
print(contact) # {"contact" : "9806573776}

x= student.popitem() # it pops last key value pair
print(student) # {"name": "Jane", "age": 30, "address": "KTM", "email" : "pradippaneru444@gmail.com"  }
print(x) #{"contact" : "9806573776}

key , value = student.popitem() #{"contact" : "9806573776}
print(student) #{"name": "Jane", "age": 30, "address": "KTM", "email" : "pradippaneru444@gmail.com"  }
print(key)  # "contact"
print(value) #"9867358373"

#Restriction in distionary keys
# All the immutable object can be used as a dictionary key
# There is no restiction in dictionary values
# key should be immutable value can be anything

data = {1 : "John", 4: "Doe"}
print(data[4]) # "Doe"

data = {1.1: "John" , 3.2 : "Doe"} #valid
data = {[1 , 2 ] : "john" , "age" : 30} #invalid as the list is mutable
data = {1.1: "Jon", 3.2: "Doe"}  # Valid
data = {[1, 2]: "Ram", "age": 30}  # Invalid
data = {(1, 2): "Ram", "age": 30}  # Valid
data = {(1, [2, 3]): "Ram", "ages": [30, 31]}  # Invalid