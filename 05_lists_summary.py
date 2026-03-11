# LIST 

INT,STR,BOOLEAN,FLOAT (IMMUTABLE)

a = 0
a = a + 1

#MEMORY -> GARBAGE COLLECTION
#ABC 
0(binary) 

#PQR
1(binary) -> 'a'




name,id,student_email,student_height,is_student_topper
ABC,001,ABC@gmail.com,3.5,False

lst_ = ['ABC',001,'ABC@gmail.com',3.5,False]
lst_ = [1,3,3,4,5,67]
lst_ = ['ABC','PQR','MNC']
lst_ = [
  ['ABC',001,'ABC@gmail.com',3.5,False],
  ['NBC',002,'NBC@gmail.com',2.8,True]
]

10,20,30

lst_ = [10,30,30,20]
1st -> 10 , 2nd -> 30, 3rd -> 20

# PROPERTIES OF A LIST
=======================================
# THROUGH LIST WE CAN ABLE TO STORE MORE THAN ONE VALUE OF SAME DATA TYPE or DIFF DATA TYPE or LISTS OF LISTS.
# WHENEVER WE ARE INSTERTING SOME DATA INTO A LIST, THEIR INSERTION ORDER IS PRESERVED.
# DUPLICATES ARE ALLOWED 
# HERTEROGENOUS DATA TYPES ARE ALLOWED.
# LIST IN PYTHON IS DYNAMIC (No defined length can be given)
# ACCESS THE ELEMENTS OF A LIST USING THEIR 'INDEX' values.
# LISTS ARE MUTABLE IN NATURE

# CREATION OF LIST
=======================

# SAMPLE LIST CREATION
lst_ = [1,3,4]
print(lst_)


# EMPTY LIST CREATION
lst_ = [] # lst_ = list()
# SOME LOGIC 
for i in range(1,11):
    if i % 2 == 0:
        lst_.append(i)

print(lst_)

# USING RANGE FUNCTION LIST CREATION

lst_ = list(range(0,11))

print(lst_)

# CREATION OF LIST OUT OF A STRING

str_ = 'JEEVAN KRISHNA'
print(list(str_))

# ACCESSING THE ELEMENTS IN A LIST USING INDEX POSITIONS (EXACTLY SAME AS STRINGS)
lst_ = [2,5,7,9,11]
print(lst_[0],lst_[-5])

# SLICING THEORY SAME AS STRING 
# AFTER SLICING, WE WILL GET THE OUTPUT AS LIST DATA TYPE.


# FUNCTIONS OR METHODS 

len(list) -> will gives you the length of a list.

lst_ = [1,3,4]
print(len(lst_)) # 3


list.count(element) -> It gives you the no of occurence of a given element in a list.
If the elmenet is not found in a list then we will get 0 rather than error.

lst_ = [1,1,3,4]
print(lst_.count(-1))


list.index(element) -> Returns the index of first occurence of the element in a list

lst_ = [1,2,3,4]
print(lst_.index(1)) # 0
print(lst_.index(-1)) # Error


# APPEND METHOD
# Append will add the element at the end of the given list.


# Add the first 10 even numbers to the empty list.

lst_ = []

for i in range(1,21):
    if i % 2 == 0:
        # We need to add the current value to the lst_
        lst_.append(i)

# append method will add the given element always at the last
# (4,2 ) (x) -> 2,4 (correct) , [2,4,6]
print(lst_)

Output : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# INSERT() METHOD
# WILL INSERT DATA OR ELEMENT OR ITEM AT A GIVEN INDEX POSITION
# SYN : list.insert(index,value)

# IF the given index position is > length of the list then it is going to add the value at the last.


lst_ = [1,2,3,4]
lst_.insert(-4,2.5)
print(lst_)



# EXTEND() METHOD

# IF WE want to add elements from one list to another list, we can use the extend method.

lst1 = ['D','E','F']
lst2 = ['A','B','C']

# ['A','B','C','D','E','F']

lst2.extend(lst1)

print(lst2)



lst_ = []

lst_.extend("STRING")

print(lst_)


# Interview question

lst_ = [[1,2],[3,4],[4,5,6],7,8]
#Output Expected :  [1,2,3,4,4,5,6]
output_ = []

for i in lst_:
    print(i)
    if isinstance(i, list):
        output_.extend(i)
    else:
        output_.append(i)

print(output_)


# Another interview question (bring the odd numbers from below input and add them into out_ list)
inp_ = [1,2,44,5,6,6,7]

out_ = []

for i in inp_:
    if i % 2 != 0:
        out_.append(i)

print(out_)



# remove() method 
# syn : list.remove(element)

# NOTE : IF multiple occurences of a element in a list then it is going to remove only the first occurence.
# If the given element is not available in the list then it is going to raise an Error.

lst = [1,2,3,4,4,5]

lst.remove(4)
lst.remove(-4)

print(lst)


# POP() MEthod

# It removes and returns the last element of the list (When we did not mention any index value)
# It removes and returns the specific element of the list (When we mention any index value)
# If the index value is not available in the list (Then we will get an Error)

lst_ = [1,2,-2,9,5,8]

print(lst_.pop())
print(lst_)

print(lst_.pop())
print(lst_)

print(lst_.pop())
print(lst_)

Output:
8
[1, 2, -2, 9, 5]
5
[1, 2, -2, 9]
9
[1, 2, -2]



lst_ = [1,2,-2,9,5,8]
print(lst_.pop(3))
print(lst_)

Output: 
9
[1, 2, -2, 5, 8]


# ORDERING THE ELEMENTS IN A LIST

# REVERSE() and #SORT()

# Reverse()
# We can use this reverse() method to reverse the order of the elements in a list.

lst_ = ['A','Z','Y','M']

lst_.reverse()
print(lst_)
Output:
['M', 'Y', 'Z', 'A']

# SORT()
# Sort() method helps us to order the elements based on requirement(either asc or desc)
# Note : The elements inside the list must be homogenous.

lst_ = ['A','a','z','Z','Y','M']
lst_2 = [-7,-1,-2,889,98]

lst_.sort()
lst_2.sort()

print(lst_)
print(lst_2)

Output:
['A', 'M', 'Y', 'Z', 'a', 'z']
[-7, -2, -1, 98, 889]

# Desc order in Sort

lst_ = ['A','a','z','Z','Y','M']
lst_2 = [-7,-1,-2,889,98]

lst_.sort(reverse=True)
lst_2.sort(reverse=True)

print(lst_)
print(lst_2)


Output:
['z', 'a', 'Z', 'Y', 'M', 'A']
[889, 98, -1, -2, -7]


# COPY METHOD 
-------------------------
# Copy method will helps us to copy the elements of the given input list and assign the values to the target list.
# In the below example, input list is lst1 and target list is lst2.
# The lst2 will be created in seperate memory and hence we dont get any issues when lst1 is subjected to any changes.

lst1 = [1,2,3]

lst2 = lst1.copy()

print(lst1)
print(lst2)

lst1.append(4)

print(id(lst1))
print(id(lst2))

print(lst1)
print(lst2)


# LIST CONCATENATION 

lst1 = [1,2,3]
lst2 = [4,5,6,[7,8]]

print(lst1+lst2)
Output:

[1, 2, 3, 4, 5, 6, [7, 8]]


# LIST MULTIPLICATION


lst1 = [1,2,3]
print(lst1*3)

output:
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# LIST COMPARISION

lst1 = ['A','B']
lst2 = ['a','B']

if lst1 == lst2:
    print("Yes ")
else:
    print("No")


output: No


# MEMBERSHIP OPERATIONS ON LIST

lst1 = ['A','B']


if 'a' not in lst1:
    print("Yes")
else:
    print("No")


# MAnual logic

lst1 = ['A','B']
is_val_available = False

for i in lst1:
    if i == 'A':
        is_val_available = True
        break 


if is_val_available:
    print("yes")
else:
    print("no")



# CLEAR FUNCTION
# It will make your list empty.

lst = [1,2,3,4]
print(lst)
lst.clear()
print(lst)


output:
[1, 2, 3, 4]
[]


# LIST COMPREHENSION


# multi line code

lst1 = [1,2,3,4]

lst2 = list()
# lst2 = [1,4,9,16]

for i in lst1:
    a = i ** 2
    lst2.append(a)

print(lst2)


# single line code 

lst1 = [1,2,3,4]

lst2 = [i+10 for i in lst1  if i % 2 == 0 ]

lst3 = [i+10 if i %2 == 0 else i+11 for i in lst1]

print(lst2)

print(lst3)

Output:
[12, 14]
[12, 12, 14, 14]







































