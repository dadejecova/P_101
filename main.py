import random
options = ('piedra', 'papel', 'tijera')

user_option = input('Eliga la opción: Piedra, papel o tijera ->')
computer_option = random.choice(options)
user_option  = user_option.lower()

if not user_option in options:
    print('Esa opción no es válida')

print('Opción de usuario =', user_option)
print('Opción del computador', computer_option)

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra le gana a tijera, ganó!')
    else:
        print('Papel le gana a piedra, perdiste.')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel le gana a piedra, ganó!')
    else:
        print('Papel no le gana a tijera, perdiste.')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera le gana a papel, ganó!')
    else:
        print('tijera no le gana a piedra, perdiste.')