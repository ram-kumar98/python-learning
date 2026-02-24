# RANGE
# ----------
# range function
# syn:
#     range(start,end,step)
# forward
# backward

# 1. print the numbers from 1to 100, 20 to 0

for i in range(1,101):
    print(i,end=" ")
    
for i in range(20,-1,-1):
    print(i,end=" ")

# 2. print the squares from 1 to 30

for i in range(1,31):
    print(i ** 2,end= " ")
    
    
# 3. print the even numbers from 1 to 50


for i  in range(1,51):
    if i % 2 == 0:
        print(i,end=" ")

print()

for i in range(2,51,2):
        print(i,end=" ")
        
        

# 4. print the sum of a given list/ print the sum of 'n' natural numbers 

# 1+2+3+4+5 = 15

n = int(input("Enter any number : "))

sum_ = 0

for i in range(1,n+1):
    sum_ = sum_ + i
    
print("Total sum for a given natural number is :",sum_)



# 5. Check the given number is a prime number or not

n = int(input("Enter any number : "))

cnt_ = 0

if n == 1:
    print("Hey give me another number")
else:
    for i in range(1,n+1):
        if n % i == 0:
            cnt_= cnt_ + 1

if cnt_ == 2:
    print("It is a PRIME number")
elif cnt_ > 2:
    print("It is a not PRIME number")
    


# 6. print the factorial of a given number


# 5! => 5*4*3*2*1

# 6! => 6*5*4*3*2*1

n = int(input("Enter any number : "))

res_ = 1

for i in range(1,n+1):
    res_ = res_ * i 

print("Factorial result of a given number is",res_)



