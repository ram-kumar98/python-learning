# module is a python file where it can store the variables, functions and logic.
# Every python file (.py) acts as a module.


# If we want to use the members of one module to another module, we should use import module_name (without .py)


#mod1.py
----------------
x = 10 

def f1():
    print("Hey this is the function f1 from mod1.py")

def f2():
    print("Hey this is the function f2 from mod1.py")

#mod2.py
--------------

import mod1 as m1

print(m1.x)
m1.f1()
m1.f2()

# If we want to import specific functionality from another module, then 
from mod1 import f1
f1()

# Importance of __name__ (To understand it better go and watch recording)


x = 10 

def f1():
    print("Hey this is the function f1 from mod1.py")

def f2():
    print("Hey this is the function f2 from mod1.py")

if __name__ == "__main__": 
    print("This is the first line from mod1.py")
    f1()
    f2()
    print("This is the last line from mod1.py")







