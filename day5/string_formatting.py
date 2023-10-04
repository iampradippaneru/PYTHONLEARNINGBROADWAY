# we do string formatting using f-string

name= "Jon"
message = f"Hello I am {name}"
print(message)


name = "John DOe"
age = 23
message = f"Hello i am {name}. I am {age} years old"
print(message) # Hello i am John DOe. I am 23 years old 

#using format specifier (%s, %d, %f etc)
print('I am %d and i am %s years old') %(name, age)

#using .format() method
print ( "I am {}" .format(name))


