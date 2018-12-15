# Sessions 9&10
# No homework
# Excercises:
# Write a function that computes the sum of 10 random numbers

import random
total = 0

for x in range(10):
 y = random.randint(1,10)
 total = total + y
print(total)

# Write a function that tests if a number is odd or even based on
# an extra parameter:
#   f(number, odd=True)

n = input("Please enter a number" "\n")
n = int(n)

if n % 2 == 0:
   print("The number is even")

else:
   print("the number is odd")


# Write a function that creates a list of random number of
# random numbers J

import random
rand_list = []

def x():
   for x in range(10):
       y = random.randint(1, 10)
       rand_list.append(y)

   print(rand_list)

# Write a function that finds the maximum for the above list

def y():
   print("The highest value in the list is: ")
   print(max(rand_list))

x()
y()


# Write a function that sorts the above list
def z():
   rand_list.sort()
   print(rand_list)


# Write another function that sorts it (different algorithm)

def a():

   s_rand_list = sorted(rand_list, reverse = True)
   print(s_rand_list)

