print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

x = int(input('Digite um número interiro para começar a sequência de Fibonacci: ? '))

a = 0
b = 1

for c in range(x):
    print(a, end=' ')

    soma = a + b
    a = b
    b = soma
