numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# en una tupla, solo se puede hacer la declaración.

print(strings)
print(strings.index('zule'))
print(strings.index('nico'))

my_list = list(strings)
print(type(my_list))
print(my_list)

my_list[1] = 'juli'
print(my_list)

my_tupple = tuple(my_list)
print(type(my_tupple))
print(my_tupple)