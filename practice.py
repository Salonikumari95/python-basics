# 1. Write a python program to add two numbers.

# 2. Write a python program to find remainder when a number is divided by z.

# 3. Check the type of variable assigned using input () function.

# 4. Use comparison operator to find out whether a given
# variable a is greater than 'b' or not. Take a = 34 and b = 80

# 5. Write a python program to find an average of two
# numbers entered by the user.

# 6. Write a python program to calculate the square of a
# number entered by the user.

# 1.
a = 10
b = 15
print(a+b)

# 2.
n = int(input("enter any number:"))
z = 3
print(n % 3)

# 3
name = input("enter your name")
print(type(name))

# 4.
a = 34
b = 84
if (a > b):
    print("A is greater no")
else:
    print("B is greater no")

# 5.
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print(f"Average of two no is : {(a+b)/2}")

# 6.
v = int(input("Enter any number:"))
print(f"Square of no is : {v**2}")


# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

# 2. Write a program to fill in a letter template given below with
# name and date.
# letter =
# Dear <Name>,
# You are selected!
# </Date|>

# 3. Write a program to detect double space in a string.

# 4. Replace the double space from problem 3 with single spaces.

# 5. Write a program to format the following letter using
# escape sequence characters.
# Letter = "Dear Saloni,This python practice is nice.Thanks!"

# 1.
name = input("Enter your name:")
print(f"Good Afternoon {name}")

# 2.
name = input("Enter your name:")
date = input("Enter Day month year:")
print(f'''
      Dear,{name}
      you are selected !
      {date}
      ''')

# 3. & 4.
s = input("Enter any sentence:")
if ("  " in s):
    print("Double space detected")
    print(s.replace("  ", " "))
else:
    print("No double space")

# 5.
print("Dear Saloni, This python practice is nice. Thanks!")


# 1. Write a program to store seven fruits in a list entered by the user.

# 2. Write a program to accept marks of 6 students and display them in a
# sorted manner.

# 3. Check that a type cannot be changed in python.

# 4. Write a program to sum a list with 4 numbers.

# 5. Write a program to count the number of zeros in the following tuple:

# 1.
p = []
for i in range(7):
    fruit = int(input("Enter Fruits name:"))
    p.append(fruit)
print(p)

# 2.
marks = []
for i in range(6):
    m = int(input("Enter your marks:"))
    marks.append(m)
    marks.sort()
print(marks)

# 3.
r = 100
print(type(r))
r = "saloni"
print(type(r))
# No,we can change the type od a variable  in python

# 4.
li = [5, 7, 3, 9]
sums = sum(li)
print(sums)

# 5.
t = (3, 7, 0, 5, 0, 2, 0)
c = t.count(0)
print(c)


# 1. Write a program to create a dictionary of Hindi words with values as
# their English translation. Provide user with an option to look it up!

# 2. Write a program to input eight numbers from the user and display
# all the unique numbers (once).

# 3. Can we have a set with 18 (int) and "18" (str) as a value in it?

# 4. What will be the length of following set S:
# Set()
# s.add(20) s.add(20.0)
# .add(20') length of s after these operations?

# 5. S={}
# What is the type of S?

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite
# language as value and use key as their names.
# Assume that the names are unique.

# 7. If the names of 2 friends are same, what will happen to
# the program in problem 67

# 8. If languages of two friends are same; what will happen
# to the program in problem 62

# 9. Can you change the values inside a list which is contained in set S


dic = {"aaloo": "potato", "tamatar": "tomato", "seb": "apple"}
word = input("enter a hindi word:").lower()
print("Meaning of the word is", dic.get(word, "not found"))

# 2.
nums = []
for item in range(8):
    data = int(input("enter no: "))
    nums.append(data)
    un = set(nums)
print("Unique no is: ", un)

# 3.
s = {18, "18"}
print(s)   # yes because datatype is different

# 4.

st = set()
st.add(20)    # 20 and 20.0 are same because python treats them equal
st.add(20.0)
st.add("20")
print(len(st))

# 5.
se = {}
print(type(se))   # empty dictionary

# 6.
di = {}
for i in range(4):
    name = input("enter your name")
    lang = input("enter your fav language")
    di[name] = lang
print(di)    

# 7.

# if 2 name is same in dictionary last one over write previous because
# dict keys must be unique


# 8.

# if language is same then there is no problems because dict values can be same

# 9.
# as list is mutable so we cannot store it in set
ss = {[1, 3, 2, 5]}


# 1.⁠ ⁠Write a program to find the greatest of four numbers
# entered by the user.

# 2.⁠ ⁠Write a program to find out whether a student is
# passed or fails, if it requires total. 40% and at least 33% in each
# subject to pass. Assume 3 subjects and take mark as an input from the user.

# 3.⁠ ⁠A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a
# program to detect these spams.

# 4.⁠ ⁠Write a program to find whether a given username contains less than 10
# characters or not.

# 5.⁠ ⁠Write a program which finds out whether a given name is present
# in a list or not.

# 6.⁠ ⁠Write a program to calculate the grade of a student from his marks from
# the following scheme:

# 90-100 Ex

# 80-90->A

# 70-80-B

# 60-70C

# 50-60D

# <50>F

# 7.⁠ ⁠Write a program to find out whether a given post is talking about
# "Saloni" or not.

# 1.
a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no:"))
c = int(input("Enter 3rd no:"))
d = int(input("Enter 4th no:"))
if (a > b and a > c and a > d):
    print("A")
elif (b > a and b > c and b > d):
    print("B")
elif (c > a and c > b and c > d):
    print("B")
else:
    print("D")
    
    
# 2.

maths = int(input("enter maths marks:"))
hindi = int(input("enter hindi marks:"))
english = int(input("enter english marks:"))
avg = (maths + hindi + english)/3
if (maths >= 33 and hindi >= 33 and english > 33 and avg >= 40):
    print("pass")
else:
    print("fail")
    
# 3.
text = input("enter your comment:").lower()
if ("make a lot of money" in text or "buy now " in text or "subscribe this" in text or "click this" in text):
    print("this comment is spam")
else:
    print("this comment is not spam")
    
# 4.
username = input("enter username:")
if (len(username) < 10):
    print("username is less than 10 character")
else:
    print("more than 10 character")
    
    
# 5.
name = ["saloni", "shubham", "sahil", "aditya"]
if "saloni" in name:
    print("name is present")
else:
    print("name is not present")


# 6.
marks = int(input("enter your marks:"))
if (marks >= 90):
    grade = "ex"
elif (marks >= 80):
    grade = "a"
elif (marks >= 70):
    grade = "b"
elif (marks >= 60):
    grade = "c"
elif (marks >= 50):
    grade = "d"         
else:
    grade = "e"

print(grade) 

# 7.
post = input("enter your post:").lower()
if "saloni" in post:
    print("Yes this post is talking about saloni")         
else:
    print("this post is not talking about saloni")


  
# 1.⁠⁠Write a program to print multiplication table of a given number using
# for loop.

#  2.⁠ ⁠Write a program to greet all the person names stored in a list 'I'
# and which starts. with S.
# 1-["saloni", "Soham", "Sachin", "Rahul"]

#  3.⁠ ⁠Attempt problem 1 using while loop.

#  4.⁠ ⁠Write a program to find whether a given number is prime or not.

#  5.⁠ ⁠Write a program to find the sum of first n natural
# numbers using while loop.

#  6.⁠ ⁠Write a program to calculate the factorial of a
# given number using for loop.

#  7.⁠ ⁠Write a program to print the following star pattern.
# for n=3
# *
# **
# ***

#  8.⁠ ⁠Write a program to print the following star pattern:
# for n=3

#  9.⁠ ⁠Write a program to print the following star pattern.
# for n=3

# 10.⁠ ⁠Write a program to print multiplication table of n using
# for loops in reversed. order.


# 1.
n = int(input("Enter any number:"))
for i in range(1, 11):
    print(n*i)

# 2.
li = ["saloni", "sahil", "rohan", "aditya"]
for i in li:
    if i.startswith("s"):
        print(f"hello {i} have a great day!")

# 3.
n = int(input("enter any no:"))
p = True
for i in range(2, n/2):
    if (n % i == 0):
        print("Not prime")
        p = False
if p == "True":
    print("prime no")
  
# 4.
n = int(input("enter nth value:"))
sum = 0
for i in range(n):
    sum += i

# 5.
n = int(input("enter nth value:"))
fact = 1
for i in range(1, n+1):
    fact *= 1
print(fact)

# 6.
n = 3
for i in range(1, n+1):
    print("*"*i)



#  1.⁠ ⁠Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.

# 2.⁠ ⁠Write a class "calculator" capable of finding square,
# cube and square root of a number.

# 3.⁠ ⁠Create a class with a class attribute a; create an object
# from it and set 'a' directly using object.ao. Does this change the 
# class attribute?

# 4.⁠ ⁠Add a static method in problem 2, to greet the user with hello.

# 5.⁠ ⁠Write a class Train which has methods to book a ticket,
# get status (no of seats) and get fare information of train running under
# Indian Railways.

# 6.⁠ ⁠Can you change the self-parameter inside a class to something
# else (say "harry"). Try changing self to "sif" or "harry" and see the 
# effects.

 
# 1.


class Programmer:
    company = "Microsoft"

    def _init_(self, name, product):
        self.name = name
        self.product = product

    def showInfo(self):
        print(f"The name of the programmer is {self.name} and he/she works on {self.product} at {self.company}")


# Creating objects
p1 = Programmer("Saloni", "Skype")
p2 = Programmer("Ravi", "Edge")

p1.showInfo()
p2.showInfo()

# 2.


class calculator:
    def __init__(self, num):
        self.num = num
     
    def square(self):
        print(self.num**2)

    def cube(self):
        print(self.num**3)    

    def squareRoot(self):
        print(self.num**1/2)
    
    n = 6


calc = calculator(n)
calc.square()
calc.cube()
calc.squareRoot()


# 3.

class sample:
    a = "saloni"

   
obj = sample()
obj.a = "Sallo" 
print(sample.a)
print(obj.a)    