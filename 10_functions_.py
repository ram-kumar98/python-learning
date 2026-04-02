# functions

# Advantage of functions is to make code reusable.

# In built functions , User defined functions
# Defining a function is not alone sufficient to execute it. We have to call the function to execute it.

# syntax 

def wishing():
    print("Hello, Good Morning")
    print("Welcome to Python Programming")

wishing() 
wishing()
wishing()



def add_num(a,b): #parameters
    print(a+b)

add_num(15, -3) #arguments



def add_num(n1,n2):
    return n1+n2

sum_ = add_num(10,20)

#task1 (adding 2 numbers) (n1+n2)
print("The sum of 2 numbers is: ",sum_)

#task2 (avg of 2 numbers) (n1+n2/2)
print("The average of 2 numbers is: ",sum_/2)

#task3 (n1+n2/n1-n2)
print("The result of n1+n2/n1-n2 is: ",sum_/(10-20))



# Positional Arguments (1)
# The values taken by the function is purely based on the position of the arguments. 
# No of parameters and arguments should be same.

def wish(name,message="Hello"):
    return message + " !!! " + name

# print(wish("Alice","Good Morning","Hello"))

# Traceback (most recent call last):
#   File "f:\info\python_learning\functions_explore.py", line 8, in <module>
#     print(wish("Alice","Good Morning","Hello"))
# TypeError: wish() takes 2 positional arguments but 3 were given


# KeyWord Arguments (2)
# Swapping of arguments wont create any issues due to the use of keywords. 
# Here we can use both positional and keyword arguments. But the kW arguments should be placed at last.
#print(wish("Alice",message="Good Morning"))


# Default Arguments (3)
# Default parameter values should be defined at last of the function definition.

#print(wish(name="Alice"))


# Variable Length Arguments (4)
# names is a tuple which can take any number of arguments.(0 to n)

def wish(*names):
    print(type(names))
    print(names)
    for name in names:
        print("Hello " + name)
        print()

#wish()
# wish("Alice","Bob")
# wish("Alice","Bob","Charlie")


def sum_num(*n):
    print(n)
    sum_ = 0 
    for i in n:
        sum_ += i
    
    return sum_

# print(sum_num(1,2,3))
# print(sum_num(1,2,3,4,5))
# print(sum_num())



# KW Arguments (5)
# data is a dictionary which can take any number of key value pairs.

def student_report(**data):
    print(data)
    for key,value in data.items():
        print(f"{key} : {value}")


student_report(name="Alice",age=20,grade="A")
student_report(name="Bob",age=22,grade="B",city="New York")



# Scope of variables in Python 

# L -> E -> G -> B
#---------------------
# L : Local (Variables defined inside a function and accessible only within that function)
# E : Enclosing (I will come to this in  a moment)
# G : Global (Variables defined at the top level of a module or outside of any function)
# B : Built-in

# # NOTE (IMPORTANT)
# When we dont have local variable, we can access its global variable as a read mode but we cannot modify it.
# IF you want to modify the global variable inside a function, you need to use the 'global' keyword.




x = 100

def demo(): 
    global x
    x = x + 10
    print(x) 

def demo1():
    global x
    x = x + 20
    print(x)

print(x) #100
demo() #110
demo1() #130
print(x)


# ENCLOSING 
# L -> E -> G -> B
# Whenever we dont have local variable in a nested function, we can access the variable from the parent function. This is called ENCLOSING SCOPE.
# In Enclosing scope, we can access the variable from the parent function but we cannot modify it. If we try to modify it, we will get an error.
# To modify the variable from the parent function, we can use the keyword NONLOCAL. 

def outer():
    x = 10 #LOCAL
    print("This is the outer function calling before modification",x)

    def inner():
        nonlocal x
        x = x+10
        print("This is the inner function.",x)

    inner()

    print("This is the outer function calling after modification",x)

outer()

# Hey Guys, Solve this problem when u are visiting this !!!

x = "G"

def outer():
    x = 'O' # Local to Outer

    def inner():
        x = 'I' # Local to Inner
        print("Inner:", x)

    print("Outer:",x)
    
    inner()

outer()

print(x)



# LAMBDA FUNCTIONS 

# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# We should use lambda functions when we have a complex logic.
# The syntax of a lambda function is: lambda arguments: expression

def add_(n):
    return n**2

sum_ = add_(3)
print(sum_)

x_ = lambda n: n**2

print(x_(3))


# MAP FUNCTION
----------------------------
# input must be an collection. (list,tuple etc)
# map will take each element from your input collection and pass it as a argument for the given function

# syn : 

map(function,input)
lst_ = [1,2,3]

# map(func,input)
# def list_sq(x):
#     return x**2

print(list(map(lambda x:x**2,lst_)))

# FILTER FUNCTION
-----------------------------
# syn : filter(fuction,input)
# Filter will take each element from your input and it will pass the input argument to function, the function will decide true or false based on your condition.
# if it is true, the element will be persisted if not it will be thrown away.

lst_ = [1,3,4,5]
op: [4]

def even_num(x):
    if x % 2 == 0:
        return True 
    else:
        return False 


lst_ = [1,3,4,5,6,8]
# op: [4]

# def even_num(x):
#     if x % 2 == 0:
#         return True 
#     else:
#         return False 
        
print(list(filter(lambda x: x % 2 == 0 ,lst_)))


# Function aliasing

def f1():
    print("This is function 1")

f2 = f1

f1()
f2()


# Function can return another function

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    return inner

f = outer() 
f()




