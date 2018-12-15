# Sessions 7&8
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc


s= input("give me a string of characters""\n")

longest = ""
solution = ""
previous = "a"
for i in s:
   if i >= previous:
       solution= solution+i
   else:
       if len(solution) > len(longest):##is our chain bigger than the one we have?
           longest = solution
       solution = i
       ##this breaks the chain
   previous = i ##if the chain is broken, the character becomes previous and keeps on reading the next one

print("The longest substring in alphabetical order is:",longest)
