
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if len(param)==0:
        return True
    else:
        return False
print(is_empty(''))
#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(list):
    total = 0
    for i in list:
        total += i
    return total / len(list)
print(calculate_mean([1, 2, 3, 4, 5]))


def calculate_median(list):
    list.sort()
    if len(list) % 2 == 0:
        median = (list[len(list) // 2] + list[len(list) // 2 - 1]) / 2
    else:
        median = list[len(list) // 2]
    return median
print(calculate_median([1, 2, 3, 4, 5, 6]))

def calculate_mode(list):
    mode = max(list, key = list.count)
    return mode
print(calculate_mode([1, 2, 3, 4, 5, 5, 6, 6, 6]))

#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.
