text = 'Ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'Js' in text:
    print('Elegiste bien!!')
else:
    print('Puede que hayas elegido bien')

size = len(text)
print("Tiene",size,"letras")

print(text)
print(text.upper())
print(text.lower())
print("Tiene",text.count('a'), "a")

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("398".isdigit())