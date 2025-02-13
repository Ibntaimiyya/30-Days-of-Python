#Exercises: Level 1 ####
'''
Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make
function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median,
mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile,
and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations
as methods for the Statistics class. Check the output below.
'''
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics:
    def __init__(self, data):
        self.data = data
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return max(self.data) - min(self.data)
    def mean(self):
        return round(sum(self.data) / len(self.data))
    def median(self):
        data = sorted(self.data)
        n = len(data)
        if n % 2 == 0:
            median1 = data[n//2]
            median2 = data[n//2 - 1]
            median = (median1 + median2) / 2
        else:
            median = data[n//2]
        return median
    def mode(self):
        data = sorted(self.data)
        mode = max(data, key = data.count)
        return {'mode': mode, 'count': data.count(mode)}
    def variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)
    def std(self):
        result = self.variance() ** 0.5
        rounded_result = round(result, 1)
        return rounded_result
    def freq_dist(self):
        data = sorted(self.data)
        freq_dist = [(x, data.count(x)) for x in set(data)]
        return sorted(freq_dist, key = lambda x: x[1], reverse = True)
    def describe(self):
        return f'Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\nMax: {self.max()}\nRange: {self.range()}\nMean: {self.mean()}\nMedian: {self.median()}\nMode: {self.mode()}\nVariance: {self.variance()}\nStandard Deviation: {self.std()}\nFrequency Distribution: {self.freq_dist()}'
data = Statistics(ages)

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def total_income(self):
        return sum(self.incomes.values())
    def total_expense(self):
        return sum(self.expenses.values())
    def account_info(self):
        return f'{self.firstname} {self.lastname} \nTotal Income: {self.total_income()} \nTotal Expense: {self.total_expense()}'
    def add_income(self, description, amount):
        self.incomes[description] = amount
    def add_expense(self, description, amount):
        self.expenses[description] = amount
    def account_balance(self):
        return self.total_income() - self.total_expense()
print(data.describe())

### Exercise lvl 2 ###

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(income['amount'] for income in self.incomes)

    def total_expense(self):
        return sum(expense['amount'] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'total_income': self.total_income(),
            'total_expense': self.total_expense(),
            'account_balance': self.account_balance()
        }

# Let me use my name:
person = PersonAccount('Abdulhamid', 'Abubakar')
person.add_income(5000, 'Salary')
person.add_income(200, 'Freelance')
person.add_expense(1500, 'Rent')
person.add_expense(200, 'Groceries')

print(person.account_info())