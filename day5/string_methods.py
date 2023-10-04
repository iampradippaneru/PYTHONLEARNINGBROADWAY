#1. capatilize
message = "hello world"
result= message.capitalize()
print(result)  # "Hello WOrld"

#2. title()
result = message.title()
print(result) # Hello World

#3. upper()
result = message.upper()
print(result) # HELLO WORLD

#4. lower()
result = message.lower()
print(result) # hello world

#split()
#this method returns lists.
message = "Hello World"
result = message.split()
print(result) #["Hello", "World"]

result = message.split("o")
print(result) # ["Hell", " W", "rld"]

result = message.split("l")
print(result) # ["He", "", "o Wor" "d"]

#join()
data = ["Hello", "World"]
result = " ".join(data)
print(result)
# data.join(" ") # it release error because join() should be called with string object not with list

#find()
message = "Hello world"
result= message.find("w")
print(result) #6

result = message.find("rld")
print(result) #8 

result= message.find("wold")
print(result) #-1

#replace
message = "hello world"
result = message.replace("hello", "Hello")
print(result) #Hello world

