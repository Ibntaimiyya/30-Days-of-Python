# Question 1: Declaring age as an Integer
age = 30
print(int(age))
# Question 2: Declaring heigh as a float
height = 6
print(float(height))
# Question 3: using input() prompt to calculate area of a triangle
base = 20
height = 10
input('Enter base(m):')
input('Enter height(m):')
area = 0.5 * base * height
print('The are of the triangle is' , area)
# Question 4: using input() prompt to calculate the perimeter of a triangle
side_A = 5
side_B = 4
side_C = 3
input('Enter side A:')
input('Enter side B:')
input('Enter side C:')
perimeter = side_A + side_B + side_C
print('The perimeter of the triangle is' , perimeter)
# Question 5: using input() prompt to calculate the area of a rectangle
length = 4
width = 8
input('Enter the length:')
input('Enter the width:')
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is', area)
print('The perimeter of the rectangle is' , perimeter)
#Question 5: using input() prompt to calculate the area and perimeter of a circle
pi = 3.14
radius = 10
input('Enter the radius')
area = pi * radius**2
perimeter = 2 * pi * radius
print('The area of the circle is' , area)
print('The perimeter of the circle is' , perimeter)
#Question 7: 
print(len('python'))
print(len('dragon'))
print(len('python') != len('dragon'))
print('on in dragon', 'on' in 'dragon' and 'on in python', 'on' in 'python')
print('jargon in I hope this course is not full of jargon:', 'jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'on' not in 'python')
print(len('python'))
num_int = 6
print(num_int)
num_float = float(num_int)
print(num_float)
num_string = str(num_int)
print(num_string)
#how do you check a number is even or odd using python

remainder = 5 % 2
print(remainder) # remainder of 1 (hence, 5 is an odd number)
# take another number, say 6
remainder = 6 % 2
print(remainder) # remainder of 0 ( hence, 6 is an even number)
# to Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_division = 7 // 3
print(floor_division) # the value derived was 2 hence not equal to 2.7

# Check if type of '10' is equal to type of 10
print(type('10'))
print(type(10)) # The statement above is a string while this is an integer

#Check if int('9.8') is equal to 10
num_string = 9.8
num_int = int(num_string)
print(num_int) # 9 not equal to 10

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = 40
rate_per_hour= 28
weekly_earning = hours * rate_per_hour 
input('Enter hours:')
input('Enter rate per hour:')
print('Your weekly earning is:', weekly_earning)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
one_minute = 60
one_hour = one_minute ** 2
one_day = 24 * one_hour
one_year = 360 * one_day
hundred_year =100 * one_year
input('Enter your age:')
print("Your age in (secs) is:", hundred_year)

# creating a table in python
print('1 \t1 \t1 \t1 \t1')
print('2 \t1 \t2 \t4 \t8')
print('3 \t1 \t3 \t9 \t27')
print('4 \t1 \t4 \t16 \t64')
print('5 \t1 \t5 \t25 \t125')

