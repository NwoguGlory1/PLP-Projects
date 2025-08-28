# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
x = int(input("Enter the no of integers you want in the list:  "))
inputted = []  
for i in range (x):
    y =  int(input(f"Enter the {i+1}th number:  "))
    inputted.append(y)
    total = sum(inputted)
print(total)