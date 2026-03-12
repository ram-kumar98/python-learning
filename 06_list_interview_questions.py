

1)
Write a program to find duplicate characters in a string.
ram kumar
-> ram ku

inp_ = input("Enter any string-> ")
out_ = ""
for c in inp_:
    if c in out_:
        print(c,'repeated')
    else:
        out_ = out_ + c 
print("Target deduplicated string is ->",out_)


Enter any string-> JEEVAN KUMAR
E repeated
A repeated
Target deduplicated string is -> JEVAN KUMR




2)
Create a output list which does not have duplicates.
Input:
[1,2,2,3,4,4,5]

Output:
[1,2,3,4,5]

inp_ = [1,2,2,3,4,4,5]
out_ = []
for v in inp_:
    if v not in out_:
        out_.append(v)

print("Final output list -> ",out_)


inp_ = [1,2,2,3,4,4,5]
out_ = []
for v in inp_:
    if inp_.count(v) > 1 and v not in out_:
        out_.append(v)

print("Final output list -> ",out_)




3)
Find common elements between two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]

Output:
[3,4]


list1 = [1,2,3,4,3]
list2 = [3,4,5,6]
inp_ = list1+list2
out_ = []
for v in inp_:
    if inp_.count(v) > 1 and v not in out_:
        out_.append(v)
print("Final output list -> ",out_)





4)
Move all zeros to the end of a list
Input:
[1,0,2,0,3,0,4]

Output:
[1,2,3,4,0,0,0]

inp_ = [1,0,2,0,3,0,4]
nz = []
z = []
for i in inp_:
    if i != 0 : 
        nz.append(i)
    else:
        z.append(i)

nz.extend(z)
print("Final output list -> ",nz)




5)
Array = [2, 7, 6, 3, 4, 1]
Get the possible pairs of integers (x,y) : 
Condition sum of x,y is odd and sum is either 9 or 5.

inp_ = [2, 7, 6, 3, 4, 1] 
out_ = []
for i in inp_:
    for j in inp_:
        if ((i+j) in [5,9]) and ((i+j) % 2 != 0) and ([i,j] not in out_) and ([j,i] not in out_) :
            out_.append([i,j])

print(out_)
