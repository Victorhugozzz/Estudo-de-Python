print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

frase = str(input('Digite uma frase: ')).strip().lower()

junto = frase.replace(' ', '')
inverso = junto[::-1]

print('=' * 40)
print('{}'.format(junto))
print('{}'.format(inverso))
print('=' * 40)

if junto == inverso:
    print(f'A frase/palavra {frase} é um palíndromo')
else:
    print(f'A frase/palavra {frase} NÃO é um palíndromo')