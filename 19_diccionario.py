my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Daniel',
    'last_name': 'Coello',
    'age': 29
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('asd'))

print('name' in my_dict)
print('otroqueno' in my_dict)