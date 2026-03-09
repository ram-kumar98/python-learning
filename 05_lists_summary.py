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


















