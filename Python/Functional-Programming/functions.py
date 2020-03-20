# Reduce in Python example
from functools import reduce
num_list = [0, 1, 2, 3, 4, 5, 6, 7]
def get_sum(acc, element):
    return acc + element
sum = reduce(get_sum, num_list)
## Example of combining map, filter, and reduce to find the average gpa of my friends based on where they are going to work
friends = [{
    'name': 'Henock',
    'gpa': 4,
    'work_location': 'NYC'
},
{
    'name': 'Jack',
    'gpa': 4,
    'work_location': 'Boston'
},
{
    'name': 'Evan',
    'gpa': 3.5,
    'work_location': 'Durham'
},
{
    'name': 'Quinci',
    'gpa': 3.3,
    'work_location': 'Atlanta'
},
{
    'name': 'John',
    'gpa': 4,
    'work_location': 'Durham'
},
]

def w_location(friend):
    return friend['work_location'] == 'Durham'

durham = list(filter(w_location, friends)) #filter friends based on working in Durham

def get_gpa(friend):
    return friend['gpa']
gpas = list(map(get_gpa, durham)) 
print(gpas)

total_gpa = reduce(get_sum, gpas)
average_gpa = total_gpa / len(gpas)
print(average_gpa)

# Partial Application:
# Takes a function and fixes some of the arguements beforehand
def add(x, y, z):
    return x + y + z

def add_partial(x):
    def add_others(y, z):
        return x + y + z
    return add_others

add_10 = add_partial(10)
print(add_10(4,7))

def curry_add(x):
    def curry_add_inner(y):
        def curry_add_inner2(z):
            return x + y +z
        return curry_add_inner2
    return curry_add_inner

add_10 = curry_add(10)
add_10_and_8 = add_10(8)
#print(add_10_and_8(2))
#print(curry_add(10)(8)(2))
