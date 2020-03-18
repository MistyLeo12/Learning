# Reduce in Python example
from functools import reduce
num_list = [0, 1, 2, 3, 4, 5, 6, 7]
def get_sum(acc, element):
    print(f'acc is {acc}, element is {element}')
    return acc + element

sum = reduce(get_sum, num_list)
print(sum)