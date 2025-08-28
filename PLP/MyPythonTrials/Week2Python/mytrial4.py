#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

x = input("Enter your name: ")
y = int(input("Enter your age: "))
z = input("Enter your favorite color: ")
my_dict = {"Name": x, "Age": y, "Fav_color": z}
print(my_dict)