#Write a program to find the frequency of the input number in a list 
#[5, 2, 3, 5, 3, 2, 3, 3, 1, 4]

given_list = [5, 2, 3, 5, 3, 2, 3, 3, 1, 4]
#input the number
your_input = int(input("Enter the number"))

#to find the frequency of the given 
frequency = given_list.count(your_input) #count of your_input in the given_ list


print(f"the frequency of the {your_input} in the given list is {frequency}")