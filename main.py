#Input and Output
name = input("Enter your name")
print(f"Good morning {name}")

#conditionals  statements
a = int(input("Enter 1st no :"))
b = int(input("Enter 2nd no :"))
c = int(input("Enter 3rd no :"))
if(a>b and a>c):
    print("A is greatest no.")
elif(b>a and b>c):
    print("B is greatest no.")
else:
    print("C is greatest no.")        

#Loops
# *
# **
# ***
# ****

for i in range(5):
    print("*" * (i))

#print 0 to 4    
i=0
while(i<5) :
    print(i)
    i +=1   
    
    
#list
a = ["saloni",8,9,True,5]
for i in a:
    print(i) 

#tuple
p = (5,7,2,9,0)
for i in p:
    print(i)       
    
# sets  it does not provide ordered value and cannot access by index no
q = set() #empty set
w = {3,7,"saloni",True,9}   
for i in w:
    print(i)
    
#dictionary
dict = {} #empty dictionary
z = {"saloni":5,"rohan":8,"Shubham":6}   
print(z["saloni"])

#file handling reading and writing in file
    
with open("saloni.txt", "w") as f:
        f.write("welcome back")
with open("saloni.txt", "r") as f:
    print(f.read()) 


           