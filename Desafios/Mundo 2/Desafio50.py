print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

soma = 0
for c in range(1, 7):
    n1 = int(input('Digite um valor(somarei so os pares): '))
    if n1 % 2 == 0:
        soma += n1
print('\n')
print(f'A soma entre os numeros pares é igua a {soma}', end=' ')