'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

Solution by: Andrew Yin
'''

cur_str = ""
long_str = ""

for i in range(0,len(s)):
    cur_str += s[i]
    if len(cur_str) > len(long_str):
        long_str = cur_str
    if i < len(s)-1 and s[i] > s[i+1]:
        cur_str = ""
        
print("Longest substring in alphabetical order is: " + long_str)
