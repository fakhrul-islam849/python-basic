# variable outside function is global variable and can be use anywhere
x = "awesome"

def myFunction():
  print("Python is " + x)

myFunction()

# local variable
x = 5

def myFunction():
    # local variable can only be accessed inside function even if same variable used in global
    x = 2
    print('local', x)

myFunction()
print('global', x)


# define global variable inside global

x = 4

def myFunction():
    global y
    y = 7
    global x    #global can also be used to change value of global variable
    x = 3

myFunction()
print('Global define function', y)
