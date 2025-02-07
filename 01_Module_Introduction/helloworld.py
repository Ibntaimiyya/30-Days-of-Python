person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
keys = person.keys()
if 'skills' in person:
    print('skills exist in person')
else:
    print('skills does not exist')
print(person['skills'][2])
print(person['skills'][4])

level = input('Please make your entry:')
