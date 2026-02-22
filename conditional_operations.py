# Python Flow Control
# =================

# - Conditional Statements ( IF,ELIF,ELSE)

# Use cases to cover for Conditional Statements
# - Given number is even or not
# - Voter Application Form
# - Grade Classification



# if <cond>:
#     #statement1
#     #statement2
# else:
#     #statements
#     #statements





# user -> age value 
# age value (Greater or equals to 18) -> Major 
# less than 18 -> Minor


# step1 : get the input from the user 
# step2 : Implement the condition based on given requirement
# step3 : Show the person either Major or Minor





name = input("Enter the person name : ")
age = int(input("Enter the age of the above mentioned person : "))

if age >= 18:
    print("The given person name is",name)
    print("The person age is",age)
    print("User application successfully registered..")
else:
    print("Sorry",name,"Your age is not matching with the given criteria...Hence declining your application.")



#1 - get the input 
#2 - check whether given no is even or odd

from sys import argv

num_ = int(argv[1])
print("The given number is",num_)

if num_ == 0:
    print("Hey give me a valid input.")
elif num_ % 2 == 0:
    print("This is an even number.")
else: # Only when all the above conditions are not meeting the requirement
    print("This is an Odd number.")






# Some important points to note:
# 1. The logic inside the If and elif will work only if the given condition returns True.
# 2. If we have multiple conditions with if,elif...
# if any one condition satisfies then remaining conditions will be skipped.
# 3. Else will be executed only if all the given conditions did not satisfy.
# 4. Else block is not mandatory.
# 5. You can have 'n' of elif statements.
# 6. You can use if condition inside if condition.(Nested if condtions)






