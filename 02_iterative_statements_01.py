# ELSE 
# Print statement in order


#NESTED IF CONDITIONS:
# given number even as well as > 100

num_ = int(input("Give any number : "))



if num_ % 2 == 0 :
    if num_ > 100:
        print("All conditions satisfied.")
    else:
        print("Hey it is a even number but not > 100.")
else:
    print("Sorry this is not even a even number.")
	
	
	
# FOR LOOP and WHILE LOOP (ITERATIVE STATEMENTS)

# ITERATION : If we execute same logic more than 1 time then we say it is an iteration.
# FOR LOOP
# WHILE LOOP

# FOR LOOP : Defined range (100,10000,10)
# WHILE LOOP : It will keep on run until a specified condition become true.

# FOR LOOP

# SYN

# for <element> in <collection/sequence> :
    # Logic Body

# collection : collection of characters eg: string, collection of numbers : list,range
# collection : collection of numbers,strings in a list.

	
print("Start of the program\n")

for char_ in 'PYTHON':
    print(char_)

print("\nEnd of the program")



print("Start of the program\n")

lst = [-3,-2,-1,0,1,2,3]

for i in lst: #take each value from a given collection of sequence
    print(i) #-3

print("\nEnd of the program")




# I have a list of numbers and I want to only print even numbers
# [1,2,3,4,5,6,6,7,8]

# 2,4,6,6,8

# step  1 : define a lst
# Iterate each element
# Condition to check whether it is a even number or not
# Then print(only if it is even)

lst = [1,2,3,4,5,6,6,7,8]

for ele in lst:
    if ele % 2 == 0: # To check if the given num is even or not
        print("Even number found",ele)

print("Program ran successfully...")


# count the no of vowels in a given word
# JEEVAN (E,E,A) : #3

# step 1: Get the input from the user
# step 2 : Go through each element
# step 3 : Condition to check whether given element is vowel or not
# step 4 : Count the vowel


name_ = input("Enter any string value : ")

cnt_ = 0

for char_ in name_:
    if (char_ in 'aeiou') or (char_ in 'AEIOU'):
        cnt_ = cnt_ + 1


print("We got Vowel count of",cnt_)