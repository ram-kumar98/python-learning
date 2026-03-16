# SET 
-----------
# IF we want to store the unique values in a varaible then we can go for SET.
# Duplicates are not allowed.
# Insertion order is not preserved. But we can sort the elements.
# Heterogenous elements are allowed.
# Set is mutable
# SYN : { } (curly braces)
# Mathematical operations like union, intersection , difference etc., on sets.


# CREATION OF SET 
-----------------------

s_ = { 40, 10, 45, 2190, 48, 50, 19, 20, 30, 60, -2,320, 8}
print(type(s_))
print(s_)

<class 'set'>
{320, 8, 40, 10, 45, 2190, 48, 50, 19, 20, 30, 60, -2} (# DATA ORDER CHANGED)

# FROM TUPLE,LIST,RANGE
t_ = (1,2,3,3) / [1,2,3,3] / range(0,11)
s_ = set(t_) / 
print(s_)

#EMPTY SET
s_ = set()
print(type(s_))
print(s_)

# NOTE : IF you create a set with empty values please do not use empty curly braces {} (It will assume as Dictionary in python)


# ADDING DATA INTO SET
s_ = set()
print(s_)
# ADD 
a = 10
s_.add(a)
print(s_)

op:
set()
{10}


#UPDATE METHOD IN SET
# TO ADD MULTIPLE ELEMENTS TO A SET.
# THE ITEMS IN UPDATE MUST BE AN ITERABLE.
s_ = {10,20,30}
l_ = [40,50,60]
t_ = (70,80,90)
r_ = range(0,10)
s_.update(l_,t_,r_)
print(s_)

#COPY 

s_ = {10,20,30}
s1_ = s_.copy()
print(s1_)

op:
{10,20,30}

# POP (Removes random number from set and it will retursn you)
s_ = {10,20,30}
print(s_.pop())
print(s_)



# Remove (Removes a specified element from the set)
s_ = {10,20,30}
s_.remove(30)
print(s_)

#Note : If the given element to remove is not available in the set, then we will get an error.

# Discard
s_ = {10,20,30}
s_.discard(-30)
print(s_)

# Exactly like Remove fuctionality , only thing if element is not avalable then it wont throw any error.



# CLEAR
s_ = {10,20,30}
s_.clear()
print(s_)


# It clear outs all elements from the set.



# MATHEMATICAL OPERATIONS


# UNION

s1_ = {10,20,30}
s2_ = {20,30,40}

s3_ = s1_.union(s2_)

print(s1_)
print(s2_)
print(s3_)

op:
{10, 20, 30}
{40, 20, 30}
{20, 40, 10, 30}


# INTERSECTION (Common elements available from 2 sets)
s1_ = {10,20,30}
s2_ = {20,30,40}

s3_ = s1_.intersection(s2_)

print(s1_)
print(s2_)
print(s3_)

op:
{10, 20, 30}
{40, 20, 30}
{20, 30}


# DIFFERENCE 

s1_ = {10,20,30}
s2_ = {20,30,40}

# Returns the elements available from set1 which is not available in set2

print(s1_.difference(s2_)) #10
print(s2_.difference(s1_)) #40

op:
{10}
{40}

# SYMMETRIC_DIFFERENCE

# Returns elements present in either set1 or set2 but not in both.
s1_ = {10,20,30,40}
s2_ = {30,40,50,60}

print(s1_.symmetric_difference(s2_))

op:
{10, 50, 20, 60}


# MEMBERSHIP OPERATIONS IN SET

s1_ = {10,20,30,40}
s2_ = {30,40,50,60}

print(40 in s1_)
print(-40 in s1_)
print(-40 not in s1_)

op:
True
False
True


# SET WILL SUPPORT COMPREHENSION
s1_ = {10,20,30,40}

s2 = {x+10 for x in s1_}

print(s2)


op:
{40, 50, 20, 30}



# WHETHER SET WILL SUPPORT INDEXING OR SLICING CONCEPT OT NOT ? NO
# WHY NO ? SET DOES NOT STORE YOUR DATA IN A SAME ORDER.








