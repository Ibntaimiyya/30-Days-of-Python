#Exercises: Level 1
#Explain the difference between map, filter, and reduce.
'''
    map: applies a function to each item in an iterable and returns the result.
    map(function, iterable)
    filter: filters out items from an iterable based on a condition.
    filter(function, iterable)
    reduce: applies a rolling computation to sequential pairs of values in a list.
    reduce(function, iterable)
'''
#Explain the difference between higher order function, closure and decorator
'''
    Higher order function: A function that takes another function as an argument or returns a function.
    Closure: A function that has access to the outer function's scope even after the outer function has finished executing.
    Decorator: A function that takes another function as an argument and extends its behavior without modifying it.
'''
#Define a call function before map, filter or reduce, see examples.
def call():
    return 'I am a function'
print(call())

#Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print('Countries List:')
for country in countries:
    print(country)


#Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print('Names:')
for name in names: 
    print(name)

#Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Numbers List:')
for number in numbers:
    print(number)