dog = {}
print(dog)
# 2. Add name, color, breed, legs, age to the dog dictionary

dog['Name']= 'Sam'
dog['Color']= 'Brown'
dog['Breed']= 'Argentinian'
dog['Legs']= 'White'
dog['Age']= '5'
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student_dictionary = {}
student_dictionary['first_name'] = 'Abdulhamid'
student_dictionary['last_name'] = 'Abubakar'
student_dictionary['gender'] = 'Male'
student_dictionary['age'] = '30'
student_dictionary['marital_status'] = 'Married'
student_dictionary['skills'] = ['DNA extraction', 'PCR', 'Gel-electrophoresis', 'Sequence Analysis', 'Python']
student_dictionary['country'] = 'Nigeria'
student_dictionary['city'] = 'Kano'
student_dictionary['address'] = {'stret':'No. 1065, Naibawa Unguwar-gabas', 'Zip-code':'7000001'}
print(student_dictionary)

# 4. Get the length of the student dictionary
length = len(student_dictionary)
print(length)

print(student_dictionary['skills'])
student_dictionary['skills'].append('Typing')
print(student_dictionary)

keys = student_dictionary.keys()
print(keys)

values = student_dictionary.values()
print(values)

print(student_dictionary.items())
del student_dictionary['skills']
print(student_dictionary)
del [dog]

