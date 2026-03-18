# If we want to store the data in the form of key value pairs then we can go for Dictionary.
# The keys in dict should not have any duplicates. (If you are entering multiple same keys then it will consider the latest k-v pair).
# Also, keys should not be a mutable object. (it should not a list or set or dict , we can keep numbers,string,boolean,float,tuple etc.,)
# Dictionaries are mutables.
# Indexes or slicing is not applicable.


# Creation of dictionary

d = {}
print(type(d))
print(d)

d1 = dict()
print(type(d1))
print(d1)

op:
<class 'dict'>
{}
<class 'dict'>
{}


# Adding data into the dictionary
students_ = {}

no_of_stud_joined = int(input("Enter the student count"))
# 3
for i in range(1,no_of_stud_joined+1):
    # Adding data into the dictionary
    # id : name
    stud_id = int(input("Enter student id -> "))
    stud_name = input("Enter student name -> ")
    students_[stud_id] = stud_name

print(students_)



#Access the data from dictionary

d_ = {}
d_[1] = 'Ravi'
d_[2] = 'Nagesh'
d_[3] = 'Geetha'
print(d_[3])

# If the given key is not available while accessing the data , you will get a KeyError.

# We can handle the above issue using get() method.
d_ = {}

d_[1] = 'Ravi'
d_[2] = 'Nagesh'
d_[3] = 'Geetha'

print(d_.get(-1,'Hey given key is not available'))


# Update the key value pair in dictionary
d_ = {}

d_[1] = 'Ravi'
d_[2] = 'Nagesh'
d_[3] = 'Geetha'

print(d_)

d_[1] = 'Ravi Kumar'

print(d_)

op:

{1: 'Ravi', 2: 'Nagesh', 3: 'Geetha'}
{1: 'Ravi Kumar', 2: 'Nagesh', 3: 'Geetha'}


# Delete a particular key value pair from dictionary 
d_ = {}

d_[1] = 'Ravi'
d_[2] = 'Nagesh'
d_[3] = 'Geetha'

print(d_)

del d_[1]

print(d_)


op:
{1: 'Ravi', 2: 'Nagesh', 3: 'Geetha'}
{2: 'Nagesh', 3: 'Geetha'}




#Clear() will remove all the K-V pairs from the dict
d_ = {}

d_[1] = 'Ravi'
d_[2] = 'Nagesh'
d_[3] = 'Geetha'

print(d_)

d_.clear()

print(d_)
op:
{1: 'Ravi', 2: 'Nagesh', 3: 'Geetha'}
{}





# Deleting the dictionary from memory

d_ = {}

d_[1] = 'Ravi'
d_[2] = 'Nagesh'
d_[3] = 'Geetha'

print(d_)

del d_

print(d_)

op:
{1: 'Ravi', 2: 'Nagesh', 3: 'Geetha'}
Traceback (most recent call last):
  File "f:\info\BIG_DATA\HADOOP\PYTHON\python_learning\set_.py", line 11, in <module>
    print(d_)
NameError: name 'd_' is not defined




# Creating the dictionary from list of tuples

dat_ = [(1,'Ram'),(2,'Ravi')]

dic = dict(dat_)

print(dic)

op:
{1: 'Ram', 2: 'Ravi'}




# Checking how many K-V pairs available in the dict
dat_ = [(1,'Ram'),(2,'Ravi')]

dic = dict(dat_)

print(len(dic))

op: 2




# pop() method

dat_ = [(1,'Ram'),(2,'Ravi')]

dic = dict(dat_)

print(dic.pop(1))

print(dic)



#popitem() method will randomly remove one key value pair from dict and returns you the K-V pair.

dat_ = [(1,'Ram'),(2,'Ravi')]

dic = dict(dat_)

print(dic.popitem())

print(dic)







