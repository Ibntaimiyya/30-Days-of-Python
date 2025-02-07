# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

first_string = 'Thirty'
Second_string = 'Days'
third_string = 'of'
fourth_string = 'Python'
space = " "
sentence = first_string + space + Second_string + space + third_string + space + fourth_string
print(sentence)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first_string = 'Coding'
Second_string = 'for'
third_string = 'All'
space = " "
sentence = first_string + space + Second_string + space + third_string
print(sentence)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding for All'

# 5. Print the length of the company string using _len()_ method and _print()_.
print(len(company))

# 6. Change all the characters to uppercase letters using _upper()_ method.

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
challenge = 'coding for all'
print(challenge.capitalize())
print(challenge.title())
print(challenge.swapcase())

# 9. Cut(slice) out the first word of _Coding For All_ string.

word = 'Coding'
first_four = word[0:4]
print(first_four)

# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
challenge = 'Coding For All'
sub_string = 'Coding'
print(challenge.rindex(sub_string))

# 11. Replace the word coding in the string 'Coding For All' to Python.
challenge = 'Coding For All'
print(challenge.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods
challenge = 'Python for Everyone'
print(challenge.replace('Python for Everyone', 'Python for All'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .

challenge = 'Coding For All'
print(challenge.split())
print(challenge.split(', '))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge.split())

# 15. What is the character at index 0 in the string _Coding For All_.
string = 'Coding For All'
first_Character = string[0]
print(first_Character)# Answer is C

# 16. What is the last index of the string _Coding For All_
string = 'Coding For All'
last_Character = string[-1]
print(last_Character)

# 17. What character is at index 10 in "Coding For All" string.
string = 'Coding For All'
index_10 = string[9:11]
print(index_10)

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
challenge = 'Coding For All'
sub_string = 'C'
print(challenge.index(sub_string))  # 0

# 21. Use index to determine the position of the first occurrence of F in Coding For All
challenge = 'Coding For All'
sub_string = 'F'
print(challenge.index(sub_string))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
challenge = 'Coding For All'
print(challenge.rfind('l'))  # 13

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Using rfind();
Challenge = 'You cannot end a sentence with because because because is a conjunction'
print(challenge.rfind('because'))

# Alternatively using index();
challenge = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(challenge.index(sub_string))

# 24.  Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
challenge = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(challenge.rindex(sub_string))

# 25. Slice out the phrase 'because because because' in the following sentence: 
# You cannot end a sentence with because because because is a conjunction.

sentence = 'You cannot end a sentence with because because because is a conjunction'
remove_3_because = sentence[31:55] # starts at zero index and up to 3 but not include 3
print(remove_3_because) #because because because

# 28. Does '\'Coding For All' start with a substring _Coding_? answer = Yes
# 29. Does 'Coding For All' ends with a substring _Coddding_? answer = No

# 31. Which one of the following variables return True when we use the method isidentifier():

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number

challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] 
final_output = ' '.join(python_libraries)
print(final_output)

# 33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this \nchallenge.')
print('I just wonder \nwhat is next')
   # I just wonder what is next.


# 34. Use a tab escape sequence to write the following lines.
   # Name      Age     Country   City
    #Asabeneh  250     Finland   Helsinki
print('Name    \tAge   \tCountry    \tCity')
print('Asabeneh\t250 \tFinland    \tHelsinki')

# 35. Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

# 36. Make the following using string formatting methods:

a = 8  
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))



