def PalindromePermutation(input): #Returns true if the input given can be arranged into a permutation
    # Creating an empty dictionary  
    freq = {}
    counter = 0
    for item in input: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    while (len(freq)>0):
        if (len(freq) % 2 == 0):
 
