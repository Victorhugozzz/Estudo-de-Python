print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

num_dig = 0
num = 0
soma = 0
while num != 999:
    num = int(input('Digite um valor(o programa so vai para quando digitar 999): '))
    soma += num
    num_dig += 1
    if num == 999:
        soma = soma -999
        break
print('=' * 40)

print(f'A quantidade de numeros digitados antes do break: {num_dig - 1}')
print(f'A soma entre os numeros digitados: {soma}')
