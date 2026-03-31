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




