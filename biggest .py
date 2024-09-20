animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

# print(animals)
aDict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) == 0:
        return None
    elif len(aDict) == 1:
        return list(aDict.keys())[0]
    biggest = ''
    biggest_len = 0
    for i in aDict:
        print("i:",i)
        print("aDict[i]:",aDict[i])
        print("len(aDict[i]):",len(aDict[i]))
        print("biggest:",biggest)
        print("biggest_len:",biggest_len)
        if len(aDict[i]) > biggest_len:
            biggest = i
            biggest_len = len(aDict[i])
    return biggest


# biggest(animals)  'd'

# aDict = {'u': []}
# Output: 'u'

# aDict = {'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}
# Output: 'b'

aDict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}

# Your output: 'c'
# Correct output: 'b'

print(biggest(aDict))
