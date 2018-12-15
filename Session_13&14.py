# Sessions 13 & 14
# Write a function that takes the name of a text file as parameter. Print out
# the 3-letter words that start with “b”

fd = open('words')
list = []

for line in fd:
   words = line.split()
   for word in words:
       if len(word) == 3 and word[0] == "b":
           list.append(word)

print(list)

# Write a recursive function that computes a to the power b (a and b are parameters given to the function)

a = int(input("give me the first number \n"))
b = int(input("give me the second number \n"))

def formula(a, b):
   if b == 0:
       return 1
   return a * formula(a, b-1)

print(formula(a,b))

# Write a function that takes an integer as parameter and returns a list of all the divisors of that number:
#   ex: 47 -> [1,47], 28 -> [1,2,4,7,14,28]

a = int(input("give me a number\n"))

def divisors(a):
   list = []
   for i in range (1, a+1):
       if a % i == 0:
           list.append(i)
   return list

list = divisors(a)
print(list)


