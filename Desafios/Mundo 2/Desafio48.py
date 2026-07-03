
print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c

print(f'A soma entre os números ímpares e multiplos de 3: {soma}')