import math
import random

import mytools
from utils import greet as g
from utils import add as a

print("Hello World")

# name = "Nishith"
# age = 36
# height = 5.8
# is_developer = True
#
# print("Name : ",name)
# print("Age", age)
# print("height", height)
# print("is Developer", is_developer)
#
#
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_developer))

# name = input("Enter your name: ")
# print("Hello,",name)
#
# age = int(input("Enter your age "))
# print("In 5 years you will be =", age+5)

# name = "Nishith"
# age = 36
# # print("Age ",age, "Name",name)
#
# print(f"{name},in 5 years you will be {age+5}, years old")


# name = input("What is your name?")
# print(f"Welcome, {name}")

# birth_year = int(input("What is your birth Year"))
# current_year = 2025
#
# age = current_year - birth_year
# print(f"You are {age} years old.")

# weight = float(input("Enter your weight in Kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height **2)
# print(f"Your BMI is : {bmi: .2f}")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# print(f"Sum: {a + b}")
# print(f"Difference: {a - b}")
# print(f"Product: {a * b}")
# print(f"Quotient: {a / b}")
# print(f"Remainder: {a % b}")

# age = int(input("enter your age : "))
# if age>=18:
#     print("You are eligible to Vote")
# else:
#     print("You are not eligible to Vote")

# age = int(input("Enter your age:"))
# citizen = input("Are you and Indian citizen ? (yes/no) : ")
#
# if age >=18 and citizen.lower() == "yes":
#     print("You are eligible to vote in India.")
#
# else:
#     print("Not eligible to Vote in India")

# x = int(input("Enter a number: "))

# if x > 0:
#     print("Positive number")
# elif x == 0:
#     print("Zero")
# else:
#     print("Negative number")


# score = int(input("Enter your score (0–100): "))
#
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# age = int(input("Enter your age: "))
# citizenship = input("Are you an Indian citizen? (yes/no): ")
#
# if age >= 18:
#     if citizenship.lower() == "yes":
#         print("You can vote.")
#     else:
#         print("You must be a citizen to vote.")
# else:
#     print("You must be at least 18 to vote.")


# num = int(input("Enter a number: "))
#
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# password = input("Enter your password: ")
#
# if len(password) < 6:
#     print("Too short")
# elif password == "123456":
#     print("Too easy. Try a stronger one.")
# else:
#     print("Password accepted")

# for i in range(5):
#     print(i)

# count = 0
# while count <=5:
#     print(count)
#     count+=1

# for i in range(10):
#     if i == 5:
#         break  # exit the loop
#     if i % 2 == 0:
#         continue  # skip even numbers
#     print(i)

# for i in range(1,11):
#     print(i)

# n = int(input("Enter a number: "))
# total = 0
# for i in range(1,n+1):
#     total = total +i
# print (f"Sum of first {n} numbers is: {total}")

# num = int(input("Enter a number: "))
# for i in range (1,11):
#     print(f"{num} X {i} = {num * i}")

# n = int(input("Enter a number: "))
# result  = 1
# i = 1
#
# while i<=n:
#     result *= i
#     i+=1
#
# print(f"Factorial of {n} is: {result}")


# def greet_user(name):
#     print(f"Hi {name}, great to see you.")
#
# greet_user("Nishith")

# def add(a,b):
#     return a+b
#
# result = add(5,10)
#
# print("Sum : ",result)
#
# def greet(name = "friend"):
#     print(f"Hello, {name}!")
#
#
# greet()
# greet("Nishith")

# def multiply(a,b):
#     return a*b;
#
# print("Product : ",multiply(5,10))

# def greet(name):
#     print(f"Hello {name}")
# name = input("Please enter your name ")
#
# greet(name)


# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result
#
# num  = int(input("Enter a number : "))
# print (f"Factorial of {num} = {factorial(num)}")

# def calculator(a,b,operator):
#     if operator == "+":
#         return a+b
#     elif operator == "-":
#         return b-a
#     elif operator == "*":
#         return a*b
#     elif operator == "/":
#         return b/a
#     else:
#         return "Invalid Operator"
#
# print(calculator(5,10,"+"))

# fruits = ["apple" , "banana", "cherry"]
#
# print(fruits[0])
#
# print(fruits[1])
#
# fruits[1] = "mango"
#
# print(fruits)
#
# print(fruits[-1])
# print(fruits[-2])
#
# fruits.append("orange")
#
#
# fruits.insert(1,"grapes")
#
# fruits.remove("mango")
# print(fruits)
# popped = fruits.pop()
#
# print(popped)
# print(fruits)
#
# for fruit in fruits:
#     print(fruit)
#
# if "apple" in fruits:
#     print("apple is present in fruits")
#
# print(len(fruits))
#
# fruits.sort()
#
# print(fruits)
#
# fruits.reverse()
# print(fruits)
#
# numbers = [1,2,3,4,5,6]
#
# print(numbers[1:4])
#
# print(numbers[:3])
#
# print(numbers[::2])
#
# cities = ["Delhi" , "Hyderabad", "Mumbai", "Chennai" , "Kolkata"]
#
# print("Cities : ",cities)
#
# cities.append("Pune")
# cities.append("Bangalore")
#
# print("Cities : ",cities)
#
# cities.sort()
#
# print("Cities : ",cities)
#
# print("Top 3 Cities", cities[:3])
#
# nums = [1,2,3,4,5,6,7]
#
# print("Count of 2 : ", nums.count(2))
#
#
# colors = ("red","green","blue")
#
# single = ("single",)
#
# print(colors)
# print(single)
#
# print(colors[0])
# print(colors[-1])
#
# # colors[1] = "pink"
#
# for color in colors:
#     print(color)
#
# print(colors.count("red"))
#
# print(colors.index("blue"))
#
# states = ("Telangana","Maharashtra","Kerala","Assam")
#
# print("States : ",states)
#
# print("Second State : ", states[1])
#
# print("Last State : ", states[-1])
#
# for state in states:
#     print("Welcome to : ",state)
#
#
# numbers = (1,2,3,4,5)
#
# print("Count of 2 : ",numbers.count(2))
#
# print("Index of 4 : ", numbers.index(4))


# fruits = {"apple" ,"banana" , "cherry"}
#
# print(fruits)
#
# fruits.add("orange")
#
# print(fruits)
#
# fruits.update(["mango","kiwi"])
#
# print(fruits)
#
# fruits.remove("banana")
#
# print(fruits)
#
# fruits.discard("papaya")
#
# print(fruits)
#
# a = {1,2,3}
# b = {3,4,5}
#
# print(a|b)
#
# print(a & b)
# print(a-b)
# print(a^b)
#
# for fruit in fruits:
#     print(fruit)
#
# languages = {"Hindi","Telegu","Tamil","Malayalam","Bengali"}
#
# print(languages)
#
# languages.add("Kannada")
# languages.add("Punjabi")
#
# print(languages)
#
# languages.add("Hindi")
#
# print(languages)
#
# north = {"Hindi","Punjabi","Bengali"}
# south = {"Tamil","Telegu","Kannada"}
#
# print("Union : ",north | south)
#
# print("Common : ", north & south)

# person = {"name" : "Nishith",
#           "age": 36,
#           "city":"Hyderabad"}
#
# print(person)
#
# print(person["name"])
#
# person["age"] = 37
# person["profession"] = "Engineer"
#
# print(person)
#
# print(person.get("name"))
# print(person.get("city"))
#
# print(person.get("country"),"India")
#
# person.pop("city")
#
# print(person)
#
# del person["age"]
#
# print(person)
#
# for key, value in person.items():
#     print(key, ">", value)
#
# keys = person.keys()
# values = person.values()
# items = person.items()
#
# print(keys)
# print(values)
# print(items)
#
#
# student = {"name":"Aarav",
#            "roll_no":25,
#            "grade":"A"}
#
# print(student)
#
# student["city"] = "Delhi"
# student["marks"]  = 92
# print(student)
#
# for key, value in student.items():
#     print(f"{key}:{value}")
#
# print(student.get("section","N/A"))

# name = "Nishith"
# greeting = 'Hello'
# multinine = """This
# is
# multiline"""
#
# print(multinine)
#
# print("HELLO".lower())
#
# print("hi".upper())
#
# print(" hello ".split())
#
# print("abc".replace("a","x"))
#
# print("a,b,c".split(","))
#
# print(" ".join(["hi","there"]))
#
# print("hello".startswith("he"))
#
# print("hello".endswith("lo"))
#
# text = "Python"
#
# print(text[0])
#
# print(text[-1])
#
# print(text[1:4])
#
# print(text[:3])
#
# print(text[::-1])
#
# name = "Nishith"
#
# age = 36
#
# print(f"My name is {name} and I am {age} years old.")
#
# print("Line1\nLine2")
#
# print("Name\tAge")
#
# print("He said \"Hi\"")
#
# name = input("Enter your name: ")
# print(f"Welcome, {name}!")
#
# text = input("Enter a word : ")
# print("Reversed: ", text[::-1])
#
#
# # Vowels in a sentence
# text  = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count+=1
# print("Vowels count: ",count)
#
# # Check Palindrome
#
# word  = input("Enter a word : ")
# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# try:
#     num = int(input("Enter a number : "))
#     print("You entered: ",num)
# except ValueError:
#     print("This is not a valid number.")
#
# try:
#     result = 10/0
#
# except ZeroDivisionError:
#     print("You can't divide by zero.")
#
# try:
#     x = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number!")
# else:
#     print(f"{x}*2 = {x*2}")
# finally:
#     print("This always runs, even if error occurs.")


# age = int(input("Enter age: "))
# if age<0:
#     raise ValueError("Age cannot be negative!")
# else:
#     print("Age is : ",age)

# try:
#     number = int(input("Enter a number"))
#     print("Square: ",number**2)
# except ValueError:
#     print("Please enter a valid number")

# try:
#     a = int(input("Enter a numerator: "))
#     b = int(input("Enter denominator: "))
#     print("Result : ", a/b)
#
# except ZeroDivisionError:
#     print("Denominator cannot be zero.")
#
# except ValueError:
#     print("Please enter valid numbers.")

# try:
#     print("Opening resource...")
#     x = int(input("Enter a number: "))
#     print("Double : ", x*2)
# except:
#     print("Something went wrong.")
# finally:
#     print("Closing resource.")

# print(math.sqrt(25))
#
# print(math.pi)
#
# print(g("Nishith"))
#
# print("Sum : ",a(5,7))

# print(mytools.square(5))
#
# print(mytools.is_even(34))
#
# num = random.randint(1,10)
#
# print(f"Random number : {num}")

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("data.txt","r") as file:
#     for line in file:
#         print(line.strip())

# try:
#     with open("info.txt","r") as file:
#         data  = file.read()
#         print(data)
#
# except FileNotFoundError:
#     print("File not Found")

# with open("output.txt" , "a") as file:
#     file.write("\n This will be added to the file")

# with open("greetings.txt","w") as f:
#     f.write("Hello Nishith!\n Welcome to Python File I/O.")
#
# with open("greetings.txt","r") as file:
#     content = file.read()
#     print("File Content : \n",content)
#
# with open("greetings.txt" ,"a") as file:
#     file.write("\n This is an appended line")
#
# with open("greetings.txt", "r") as file:
#     for line in file:
#         print(line.strip())










