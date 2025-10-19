
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
# Sot()
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

# 1.

dic = {"aaloo": "potato", "tamatar": "tomato", "seb": "apple"}
word = input("enter a hindi word:").lower()
print("Meaning of the word is", dic.get(word, "not found"))

# 2.