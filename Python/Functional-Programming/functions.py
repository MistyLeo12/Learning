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