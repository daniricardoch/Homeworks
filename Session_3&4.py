#Sessions 3&4
#Write a program that asks for your name and prints: “Hello <name>!”
name = input("What is your name?" "\n ")
print ("Hello " + name + "!")

#Write a program that takes 2 numbers as input and prints the rounded up division result
num1 = int(input("What is the first number?" "\n"))
num2 = int(input("What is the second number?" "\n"))
print("The rounded division is: ")
print(num1//num2)

#Write a program that takes the radius of circle as input and prints the surface of the circle
r = float(input("What is the radius?" "\n"))
print("The area is: ")
print(r**2 * 3.14)

# Write a program that behaves like a pocket calculator that can do: (+,-,*,/) of 2 numbers.
# #The numbers and the operation is read from the user. Hint: use eval() function that takes
# #a string and evaluates that string as if it were a Python expression.


num1 = int(input("What is the first number?" "\n"))
num2 = int(input("what is the second number?" "\n"))

op = input("Choose an operation:(+,-,*,/)""\n")

if op == "+":
    result = num1 + num2
    result = str(result)
    print("The addition is: " + result)


elif op == "-":
    result = num1 - num2
    result = str(result)
    print("The subtraction is: " + result)

elif op == "*":
    result = num1 * num2
    result = str(result)
    print("The multiplication is: " + result)

elif op == "/":
    result = num1 / num2
    result = str(result)
    print("The division is: " + result)

else:
    print("Error recording the operation")


