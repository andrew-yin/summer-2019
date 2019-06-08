'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2

Solution by: Andrew Yin
'''

bob_count = 0
b_prev = False
bo_prev = False

for char in s:
    if char == "b" and bo_prev == False:
        b_prev = True
    elif char == "o" and b_prev == True:
        bo_prev = True
        b_prev = False
    elif char == "b" and bo_prev == True:
        b_prev = True
        bo_prev = False
        bob_count += 1
    else:
        b_prev = False
        bo_prev = False
            
print("Number of times bob occurs is:" + " " + str(bob_count))
