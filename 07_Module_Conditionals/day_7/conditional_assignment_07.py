# Question 1 (Exercise level 1)

age = int(input('Enter your age:'))
num = 18-age
if age>18:
    print('You are old enough to learn to drive')
else:
    print('You need',num,'more years to learn to drive')

# Question 2
your_age = int(input('Enter you age:'))
my_age = 2000
diff = my_age - your_age
abs = abs(diff)
if your_age < 2000:
    print('You are',abs,' year(s) older than me')

else:

    print('You are',abs,'younger than me')

# Question 3

A = int(input("Enter the value of A:"))
B = int(input("Enter the value of B:"))

if A < B:
    print("A is less than B")
elif A < 0:
    print("A is a negative number")
else:
    print("A is greater than B")

    #Exercise lvl 2#
marks = int(input('Please enter the marks:'))
if 0 <=marks <=100: 
    if marks >=90:
        grade = 'A'
    elif marks >=80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60: 
        grade = 'D'
    else: 
        grade = 'F'
    print('Grade:', grade)

    
fruits = ['banana', 'orange', 'mango', 'lemon']
frt = input('Enter your fruit of choice:')
if frt in fruits:
    print('The fruit',frt, ' is already on the list')
else:
    print('No it is not on the list. Find below an updated list:')
    fruits.append(frt)
    print(fruits)

                                ### Exercise lvl 3 ###