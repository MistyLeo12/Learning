""" 
Since  all of my classs are focused on OOP, we never have learned functional
programming. In order to become a better programmer I want to learn about functional programming.
I feel like it will help my code logic, writing less buggy code, provide a new way of thinking how to approach problems,
and create interesting challenges.

For the purpose of this I will be learning through Python even though it doesn't have Immutiability built into the langauge,
it is easy to read, write quickly, and test. At the end of this I will create a larger project coded in a functional programmimng way 
or a hybrid with OOP. 
 """

#Passes in functions as data based on what the current enviornment is:
import math

# 1. 
def say_hello(name):
    print(f'Hello {name}')

say_hello_output = say_hello
say_hello_output('Gabriel')

ENVIRONMENT = 'dev'

def fetch_data_real():
    print('Doing something important')
def fetch_data_fake():
    print('Returning fake data while waiting for real data')
    return {
        'name': 'Gabriel Crowell',
        'age': 21
    }

fetch_data = fetch_data_real if ENVIRONMENT == 'prod' else fetch_data_fake
data = fetch_data()

# 2. 
#Uses different functions to modify a number
def double(x):
    return 2 * x
def minus_one(x):
    return x-1
def squared(x):
    return x * x

function_list = [
    double,
    minus_one,
    squared,
    math.sqrt #Can use functions that we don't define ourselves as well
]

my_num = 10

for func in function_list:
    my_num = func(my_num)
print(my_num)

# 3. 
#Passes function as an arguement to do arithmetic 
def add(x, y):
    return x+y
def subtract(x,y):
    return x-y
def combine(func):
    return func(2,3)
#print(combine(max)) gives the max between the two numbers
print(combine(add))
#print(combine(min)) returns the min between the two numbers

#Passes functions as arguemnts to do string manipulation 
def name_combine(func):
    return func('Gabriel', 'Crowell')
def append_with_space(str1, str2):
    return f'{str1} {str2}' #appendss two names with a space
def get_government_name(first,last): #Returns LAST NAME, FIRST NAME 
    return f'{last.upper()},{first.upper()}'
print(name_combine(get_government_name))
print(name_combine(append_with_space))

# 4. 
# Arithmetic done again based on first class functions 
def create_multiplier(a):
        return lambda x: x * a 

#Could replace this with a dictionary 
double = create_multiplier(2)
triple = create_multiplier(3)
ten_times = create_multiplier(10)

print(double(5))
print(triple(5))
print(ten_times(5))


# 5. 
# Creates a counter and increments it based on a defined number
# Shows how closure works in functional programming
# only increment() and get_coun() can access the count variable now

def create_counter():
    count = 0 
    def get_count():
        return count
    def increment():
        nonlocal count #tells python this count is the same as above
        count += 1 
    return (get_count, increment)

get_count, increment = create_counter()
print(get_count())
[increment() for _ in range(3)] # calls increment 3 times 
print(get_count())
[increment() for _ in range(3)]
print(get_count())

# 6.
#Uses Single Responsibility Principle and FP to divide to numbers and chekc no divide by zero
def divide(x, y):
    return x / y
def denominator_not_zero(func):
    def safe_division(*args):
        if args[1] == 0:
            print('Warning: Denominator is zero')
            return
        return func(*args)
    return safe_division
divide_safe = denominator_not_zero(divide)

print(divide_safe(10, 3))