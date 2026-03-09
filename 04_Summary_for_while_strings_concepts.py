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


=============


TO REVISE

-- FACTORIAL
-- COUNT OF VOWEL
-- PRIME OR NOT



10 
2,3,5,7

15
2,3,5,7,11,13


# step 1: Get the input from the user 
# step 2: Iterate each number from 1 till the input value (1,input) -> (1,10), -> (1,50) (for loop)
# step 3: Each number -> Find the total no of factors (prime number logic)
# step 4: Factor count -> 2 -> PRIME else -> NOT PRIME (if else logic)




Print the table for the given number till 10 multiples
Print the table upto the given number till 10 multiples 

ENUMERATE 

BREAK vs CONTINUE

BREAK in nested loop 

HOW to stop outer for loop if inner breaks 


WHILE LOOP 

- SUM of the given numbers
- PRODUCT of the given numbers 


==============

IF + LOOPS 

==============

STRINGS
LIST 
TUPLE
SET
DICT

==========================


lst = [1,12,34,47,65,5,-3,89]

for p,x in enumerate(lst):
    if x == -3:
        print("Found the required value",x,"and the position value is",p)
        
        
while <condition>:
    #logic
    #logic stat2
    #logic stat3
    
While loop logic will keep on execute until the given condition becomes false.

num_ = int(input("enter the number : "))

x = 1

while x <= num_:
    print(x)
    x = x+1

print("End of the program")



First 30 even numbers using while loop 


num_ = int(input("Enter the number : "))

x = 1

even_cnt = 0

while even_cnt < num_:
    
    if x % 2 == 0:
        print(x)
        x = x+1 
        even_cnt = even_cnt+1
        
     

num_ = int(input("Enter the number : "))
x = 1
even_cnt = 0

while even_cnt < num_:  
    if x % 2 == 0:
        print(x) 
        even_cnt = even_cnt+1
        
    x = x+1
    


num_ = int(input("Enter number : "))
sum_ = 0
x = 1

while x <= num_:
    sum_ = sum_ + x 
    x = x+1

print("Total sum :",sum_)


## CONTINUE



n = int(input("Enter any number : "))

sum_ = 0
x = 1

while x <= n:
    if x == 3:
        x = x+1
        continue
    else:
        sum_ = sum_ + x 
    x = x+1


print("Final result -> ",sum_)


while True:

    x = int(input("Enter your first number"))
    y = int(input("Enter your second number"))

    if y == 0:
        break 
    else:
        res_ = x / y
        print("The result -> ", res_)

print("End of program")



n = int(input("Enter any number : "))

for i in range(1,n+1):
    if i == 4:
        break 
    else:
        print(i)

print("End of program")





rows_ = int(input("give no of rows : ")) #3
cols_ = int(input("give no of cols : ")) #3

for i in range(1,rows_+1):
    if i == 2:
        continue
    else:
        for j in range(1,cols_+1):
            if j == 3:
                break
            else:
                print("(",i,",",j,")",end=" ")

    print()

print("End of program")



# SUM OF THE NUMBERS in given value

n_ = int(input("Enter any number : "))
sum_ = 0

while n_ > 0 :
    print("Before ",n_)
    r_ = (n_ % 10)
    sum_ = sum_ + r_
    n_ = n_ // 10 
    print("After ",n_,r_,"\n")

print("Sum of given numbers -> ",sum_)



# PRODUCT OF THE NUMBERS in given value

n_ = int(input("Enter any number : "))

prod_ = 1

while n_ > 0 :
    #print("Before ",n_)
    r_ = (n_ % 10)
    prod_ = prod_ * r_
    n_ = n_ // 10 
    #print("After ",n_,r_,"\n")

print("Sum of given numbers -> ",prod_)


===================================================================


STRINGS 

str -> "int,char,special,-,_"



slicing
------------

begin:end:step 

step : default -> 1

    +ve 
    direction -> left to right
    if end value is 0 then result empty
    
    default :
        begin - 0
        end - length of string 
        
    
    
    -ve
    direction -> right to left
    if end value is -1 then result empty 
    
    default : 
        begin -> -1 
        end : -(length pf string + 1)
        
        
----------------------



# SLICING

# [begin:end:step] (all arguments are optional)

# step is 1 (Default)

# 1. We have to decide (left -> right) ot (right to left) {Step will decide}
# STEP value (+ve) : LEFT TO RIGHT ; (-ve) : RIGHT TO LEFT
# LEFT TO RIGHT :
    # START : Default -> 0
    # END : Default -> length of string; Explicity end value mention : end - 1
    # END -> 0 -> Result empty

# RIGHT TO LEFT : 
    # START : -1 (Default)
    # END : -(length of string + 1) ; end value + 1
    # END -> -1 -> RESULT EMPTY
        
    
    
#print(s[-400]) # INDEXING WILL GIVE INDEX OUT OF RANGE ERROR

print(s[-1:-400:-1]) # SLICING WILL NEVER GIVES YOU INDEX OUT OF RANGE ERROR


s_ = 'LOLO'

if s_ == s_[::-1]:
    print('The given string is palindrome')
else:
    print("Sorry it is not a palindrome")



# LENGTH

s_ = 'JEEVAN KRISHNA IS A GOOD BOY'

print(len(s_))



# MEMBERSHIP OPERATIONS IN STRING
# IN vs NOT IN


S_ = 'GEETHA Geetha'

if 'Geetha ' not in S_:
    print('YES')
else:
    print('NO')
    
    
 s1 = 'JEEVAN '
s2 = 'SELWANTH'

print(s1+s2)
print(s1*2)



# STRIPPING THE SPACES

s1_ = 'NAGESH  '
s2_ = '  NAGESH'
s3_ = '  NAGESH  KUMAR '

s11 = s1_.rstrip()
s22 = s2_.lstrip()
s33 = s3_.strip()

print(len(s11))
print(len(s22))
print(len(s33))


# REMOVING ALL THE SPACES FROM A GIVEN STRING

s_ = input("Enter any string : ")

#NAGESHKUMAR

s_new = ""

for x in s_:
    if x != " ":
        s_new = s_new+x

print("Newly formed string -> ",s_new)


#USING REPLACE METHOD

s_ = input("Enter any string : ")

s_new = s_.replace(" ","")

print("Newly formed string -> ",s_new) 





#Find the index of the given character

S_ = input("Enter any string : ")
char_ = input("Enter the character that you are looking for -> ")

index_ = 0
found_ = False

for x in S_:

    if x == char_:
        print("Index value is -> ",index_)
        found_ = True 
        break
    index_ = index_ + 1


if not found_:
    print("Sorry we could not find your character !!!")



# FIND

SYN : given_String.find('char')

# IF char is available it will give you first occurence of the index value 
# IF Char is not available then it is going to give you -1 as the index 



#INDEX 

SAME AS FIND 

ONLY DIFFERENCE IS IF THE GIVEN CHARACTER IS NOT AVAILABLE IN THE GIVEN STRING , THEN 
IT WILL THROW AN ERROR.


rfind,rindex same functionality as find and index , only difference is it will search the char or strings from right to left (reverese)

S_ = input("Enter any string : ")
print(S_.rindex('E'))




# COUNT THE GIVEN CHARACTER IN A GIVEN STRING

s_ = input("Enter your string value here ---> ")

c_ = input("Enter your char for searching -> ")

count_ = 0

for i in s_:

    if i == c_:
        count_ = count_ + 1

print("Total count for a given character is -> ",count_)




# SPLIT FUNCTION 


string_.split(delimiter)



"FIRST_NAME|MIDDLE_NAME|LAST_NAME]" -> split (-) 

FIRST_NAME,LAST_NAME

[FIRST_NAME,MIDDLE_NAME,LAST_NAME]

Return type -> LIST  (Output)



s_ = 'STRING1_STRING2_STRING3'

print(s_.split('_'))


s_ = 'STRING1|STRING2|STRING3'

print(s_.split('|'))

['STRING1', 'STRING2', 'STRING3']


string1:string2:string3 


# JOIN OPERATION 


lst_ = ['STRING1', 'STRING2', 'STRING3']

str_ = ''.join(lst_)

print(str_)


# USING INBUILT LOGIC (JOIN EQUIVALENT)


lst_ = ['STRING1', 'STRING2', 'STRING3','STRING4']

final_str = ""

last_index = len(lst_) - 1

for p,i in enumerate(lst_):
    if last_index != p:
        final_str = final_str + i + ':'
    else:
        final_str = final_str + i

print("My final output -> ",final_str)


#PLAYING WITH CAPITAL AND SMALL LETTERS IN A GIVEN STRING

str_ = 'abc'

str_.upper()

str_.lower()

str_.swapcase() 

str_.title() 

str_.capitalize()



str_ = "Python learNing is fUn and joy"


print(str_.upper())
print(str_.lower())
print(str_)
print(str_.swapcase())
print(str_.title())
print(str_.capitalize())



# FInd the count of given word 'is' (case insenstive) in a given string

str_ = "It IS one of the most important skill that you should have. Is that really important ? " 


#is -> count (of its case)
cnt_ = 0

for i in str_.lower().split(" "):

    if i == 'is':
        cnt_ = cnt_ + 1

print("Finally we found count -> ",cnt_)



# STARTSWITH AND ENDSWITH

s_ = 'Python is good programming language but people used to fear about that.'

# Python or not (string starting with Python or not)

print(s_.startswith('python'))

print(s_.endswith('Done.'))


## SOme more methods for strings

print("Jeevan123".isalnum())
print("Jeevan123".isalpha())
print("Jeeva".isdigit())
print("Jeeva".islower())


# STRING FORMATTING


name = 'Dhoni'
age = '40'

str_1 = "Hello this is {} and my age is {}".format(name,age)
str_2 = "Hello this is {0} and my age is {1}".format(name,age)
str_3 = "Hello this is {x} and my age is {y}".format(x=name,y=age)
str_4 = f"Hello this is {name} and my age is {age}"

print(str_1)
print(str_2)
print(str_3)
print(str_4)



# STRING BREAKING

str_ = "Hey this is Jeevan Krishna from Nellore, currently I'm working on Devops domain" \
        " and I really want to learn new skills as well"

print(str_)




# string =

even position words -> 

He is good boy 

He si good yob


# step 1: split the string on "space" delim 
# step 2 : loop through list 
        # condition (position check) 
        # enumerate 
        # 1,3 (odd positions) 



str_ = "THis is python discussion session happening at 8.00 AM daily."

res_= ""

for p,i in enumerate(str_.split(" ")):

    if p % 2 != 0:
        res_ = res_ + i[::-1] +" "
    else:
        res_ = res_ + i +" "

print("Result -> ",res_)



# PROGRAM TO GET THE VOWEL AND CONSONANT COUNT

str_ = "Python are used to check whether."
vow_cnt = 0
cons_cnt = 0

for i in str_:
    if i.lower() in "aeiou" :
        vow_cnt = vow_cnt+1
    elif i.lower() not in "aeiou" and i.isalpha() :
        cons_cnt = cons_cnt+1

print("Vowel count -> ",vow_cnt)
print("Consonant count -> ",cons_cnt)





