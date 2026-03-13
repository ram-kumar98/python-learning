# Tuple is another data structure in Python and which is almost similar to List but only thing is Tuple is Immutable in nature.
# List and Tuple ( Mutable vs Immutable) -> more no of times question had asked in interviews.
# Tuple is read only version of List.
# If our data is fixed and you think that it is never going change then we can go for Tuple if not go for List.
# Insertion order is preserved. 
# Duplicates are allowed.
# Heterogeneous values are allowed.
# We can able to access the values of a tuple using their index position value.
# Syn : a = (val1,val2,val3...)

t = (1,2,3,4)
print(type(t))
print(t)
Op:
<class 'tuple'>
(1, 2, 3, 4)

# Whenever we want to create a single element inside a tuple it should be (element,) and Avoid (XXXX) -> (element)

# TUPLE CREATION

# Using List
lst_ = [1,2,3]

t = tuple(lst_)

print(type(t))

print(t)


# using Range 

t = tuple(range(0,11))

print(t)


# Accessing and Slicing operations and syntax is exactly similar to LIST.


t1 = (1,2,4)
t2 = (3,4,5)

t3 = t1+t2 

print(t3)

print(t1*2)
output:
(1, 2, 4, 3, 4, 5)
(1, 2, 4, 1, 2, 4)


# IMPORTANT FUNCTIONS AND METHODS FOR TUPLE

t_ = (78,90,1,3,5,7)

print(t_.count(3))

print(len(t_))

print(t_.index(5))

print(min(t_),max(t_),sum(t_))

new_t = tuple(sorted(t_))

print(new_t)
OP:
1
6
4
1 90 184
(1, 3, 5, 7, 78, 90)



# TUPLE UNPACKING IS SAME AS LIST UNPACKING

t_ = (1,2,3)
a,b,c = t_ 
print(a,b,c)


# TUPLE WILL NOT SUPPORT TUPLE COMPREHENSION 
# IF YOU ARE TRYING TO CREATE TUPLE COMPREHENSION THEN IT WILL GIVE YOU A GENERATOR OBJECT. (PLACE HOLDER)
t = (i+10 for i in range(0,11))

print(t)
print(type(t))

<generator object <genexpr> at 0x00000223E77066C0>
<class 'generator'>





