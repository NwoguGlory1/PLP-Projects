# Basic Calculator program

x =int( input("Type in your first number: "))
y = int(input("Type in your second number:  ")) 
z = input("Type in any of these math operators you want (+, -, *, /):  " )
if z == "+":
    print(f'x + y = {x + y}')
elif z == "-":
    print(f'x - y = {x - y}')
elif z == "*":
    print(f'x * y = {x * y} ')
else:
    print(f'x / y = {x / y} ')
