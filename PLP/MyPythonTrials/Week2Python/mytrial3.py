#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

x = input("Enter a set of random integers seperated by space: ")
y = input("Enter another set of random integers seperated by space: ")
#string is returned
set_one = (x.split()) #  list of splitted string is converted to set 
set_two = (y.split())
#expression for item in iterable if condition
set_of_intA = {int(item) for item in x.split()}
set_of_intB = {int(item) for item in y.split()}
#create a new set that contains only the elements that are common to both sets.
set_final = set_of_intA.intersection(set_of_intB)
print(f"The common integers to the two sets of sets you gave are: {set_final}")
