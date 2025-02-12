# 1. Declare an empty list
this_is_an_empty_list = []
print(this_is_an_empty_list)

# 2.  Declare a list with more than 5 items

Kano = ['Kumbotso', 'Nassarawa', 'Tarauni', 'Dala', 'Gwarzo', 'Municipal']
print(Kano)

# 3. Find the length of your list
Kano = ['Kumbotso', 'Nassarawa', 'Tarauni', 'Dala', 'Gwarzo', 'Municipal']
print(len(Kano))

# 4. Get the first item, the middle item and the last item of the list
Kano = ['Kumbotso', 'Nassarawa', 'Tarauni', 'Dala', 'Gwarzo', 'Municipal']
first_item = Kano[0]
print(first_item)

middle_item = Kano[3]
print(middle_item)

last_item = Kano[-1]
print(last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Abdulhamid', '30', '6.5', 'Married', 'Naibawa' ]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies) # Answer to Question #7

print('The number of companies is:' ,len(companies)) # Answer to Question #8
first_company = companies[0]

print('The first company is:', first_company) # answer to Question #9
middle_company = companies [3]
print('The middle company is:', middle_company)
last_company = companies [-1]
print('The last company is:', last_company)
companies[4] = 'Dell'

print(companies) # answer to Question #10
IT_company = 'Metaverse'
companies.append(IT_company) # answwer to Question 11
print(companies)

IT_company_1 = 'Samsung'
companies.insert(1, IT_company_1)
print(companies) # answer to Question 12

companies[1] = companies[1].upper()
print(companies) # answer to Question 13

does_exist = 'Dell' in companies
print(does_exist) # question 15

companies.sort()
print(companies) # Question 16

companies.sort(reverse=True)
print(companies) # Question 17

Slice_first_three = companies [3:]
print(Slice_first_three) # Question 18

Slice_middle_out = companies [4:5]
print(Slice_middle_out) # Question 19

slice_out_last_three = companies [:5]
print(slice_out_last_three) # Question 20

companies.remove('Facebook') # Question 21. Remove the first IT company
print(companies)

companies.remove('Metaverse') # Question 22.
print(companies)

companies.remove('Amazon')# Question 23.
print(companies)

companies.clear() # Question 24
print(companies)

# Question 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

Joint_string = front_end + back_end
print(Joint_string)

# Question 27
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'Python')
print(full_stack)

full_stack.insert(6, 'SQL')
print(full_stack)

### Beginning of Exercise Lvl 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages) # - [19, 19, 20, 22, 24, 24, 24, 25, 25, 26] the minimum age is 19

ages.sort(reverse=True)
print(ages) # - [26, 25, 25, 24, 24, 24, 22, 20, 19, 19] the maximum age is 26

ages.append(19)
print(ages)

ages.append(26)
print(ages)

ages = [19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]
middle_age = 24
middle_age_1 = 24
median = (middle_age + middle_age_1)/2
print(median)

sum_of_all_ages = sum(ages)
print(sum_of_all_ages)
number_of_ages = len(ages)
average = sum_of_all_ages/number_of_ages
print(average)

maximum_age = 26
minimum_age = 19
range = maximum_age - minimum_age
print(range)

print(minimum_age - average) 
print(maximum_age - average)

absolute_min =abs(minimum_age - average)
absolute_max = abs(maximum_age - average)

print(absolute_min) # absolute value for minimun age is 3.75
print(absolute_max) # absolute value for maximum age is 3.25

print('The absolute value for (minimum - average) is:', absolute_min)
print('The absolute value for (maximum - average) is:', absolute_max)

# list_exercise lvl 3

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

number_of_countries = len(countries)
print(number_of_countries)

# since the number of countries is not even we add 1
middle_country = (number_of_countries + 1)/2
print(middle_country)
print('The middle country on the list is:', middle_country,'th')

# . Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries
print(ch)
print(ru)
print(us)
print(scandic)

                ###BEGINNING OF TUPLE EXERCISE LVL 1 ####

                
# Question 1. Create an empty tuple
an_empty_tuple = ()
print(an_empty_tuple)

# Question 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Salim', 'Mustafa', 'Aminu', 'Abdulbasid', 'Yasir')
sisters = ('Maryam', 'Rukayya', 'Sumayya', 'Fatima')

# Question 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# Question 4. How many siblings do you have?
num_sibling = (len(siblings))
print('I have',num_sibling,'siblings')

# Question 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings[0] = 'Abubakar'
siblings.insert(1, 'Sakina')
print(siblings)
family_members = siblings
print(family_members)

                    ### Tuple Exercises: Level 2 ###

family_members = ['Abubakar', 'Sakina', 'Mustafa', 'Aminu', 'Abdulbasid', 'Yasir', 'Maryam', 'Rukayya', 'Sumayya', 'Fatima']
ab, sa, *siblings = family_members
print(ab)
print(sa)
print(siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Mango', 'Apple', 'Banana', 'Pomegranate')
vegetables = ('Tomato', 'Salad', 'Celery', 'Spinach')
animal_products = ('Meat', 'Milk', 'Diary', 'Hide')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_tp = ('Mango', 'Apple', 'Banana', 'Pomegranate', 'Tomato', 'Salad', 'Celery', 'Spinach', 'Meat', 'Milk', 'Diary', 'Hide')
food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)

food_stuff_list = ['Mango', 'Apple', 'Banana', 'Pomegranate', 'Tomato', 'Salad', 'Celery', 'Spinach', 'Meat', 'Milk', 'Diary', 'Hide']
slicing_salad_celery = food_stuff_list[5:7]
print(slicing_salad_celery) # Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

slicing_first_three = food_stuff_list[:3]
print(slicing_first_three) # slicing the first three

slicing_last_three = food_stuff_list [9:]
print(slicing_last_three) # slicing the last three

print('Banana' in food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

                    ### Sets Exercises: Level 1 ###

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length_it_companies = len(it_companies)
print(length_it_companies)
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Cryptic', 'Sensodyne', 'Terabit'])
print(it_companies)
it_companies.remove('IBM')
print(it_companies)

# If the item is not found remove() method will raise errors
# However, discard() method doesn't raise any errors.

                    # Sets Exercises: Level 2 ###

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.update(B)
B.update(A)
print(A)
print(B)
print(A.symmetric_difference(B))
del A
print(B)
del B

            ### Sets Exercises: Level 3 ###

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_in_set = set(age)
print(age_in_set)
print(len(age)) # the length of the list of ages is 8
print(len(age_in_set)) # the length of the set of ages is 5
print('The length of list of ages is longer having 8 while that of set is 5')

A = {'i', 'am', 'a', 'teacher'}
B = {'i', 'love', 'to', 'inspire'} 
C = {'teach', 'people'}
print(A.difference(B))
print(A.difference(C))
print(B.difference(C))



