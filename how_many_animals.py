# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

# print(animals)

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

# how_many_animals_?  6

# print(animals['a'] + animals['b'] + animals['c'] + animals['d'])  what i need the length of it

key_list = list(animals.keys())
print(key_list)
value_list = list(animals.values())


def total(alist):
    result = []
    for el in alist:
        result.extend(el)
    return len(result)

# print(list(map(total, value_list)))

print(total(value_list))
