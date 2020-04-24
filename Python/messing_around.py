import random 

def inplace_shuffle(deck):
    if len(deck) <= 1:
        return deck
    last_index = len(deck) - 1
    for i in range(last_index, 0, -1):
        random_i = random.randint(0, i+1)
        deck[i], deck[random_i] =  deck[random_i], deck[i]
    return deck
deck_test = [1,2,3,4,5,6,7,8,9]
deck_1 = [9]


def rever(elems):
    new_list = []
    for i in range(len(elems):
        new_list.append(elems[i])
    return new_list

print(rever(deck_test))