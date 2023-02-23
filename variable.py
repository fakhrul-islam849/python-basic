# no need to declare a variable even if type can be change after assign
print('Declare a variable')
x = 5
x = 'changed'
print(x)

# specify the variable with casting
print('specify variable type')
x = str(3)
y = int(3)
print(x)
print(y)

# get type of variable
print('Get Tpe of variable')
x = 5.0
y = 'I am string'
print(type(x))
print(type(y))

# string variable can be declared either single or double quotes
print('String variable definition')
x = 'string'
x = "string"
print(x)

# variable are case sensitive
print('case Sensitive')
a = 4
A = 5
print(a)
print(A)

myVariable = 'Jewel' # camel case
MyVariable = 'Jewel' # pascal case
my_variable = 'jewel' #snake case

# output variable as pythonisawesome
x = "I "
y = 'Love '
z = 'coding'
print(x + y + z)

# if use operator between number variable will work mathematical operator
x = 5
y = 4
print(x+y)

# output multiple variable
x = 8
y = 'String'
print(x, y)