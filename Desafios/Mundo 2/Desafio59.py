import time

print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

num = float(input('Digite o numero 1: '))
num2 = float(input('Digite o numero 2: '))
opcao = 0

while opcao != 5:
    print('Bem vindo ao menu de calculo')
    print('=' * 20)

    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do menu')
    opcao = int(input('Selecione um dos numeros: '))

    if opcao == 1:
        soma = num + num2
        print('\n')
        print('{} + {} = {}'.format(num, num2, soma))
    elif opcao == 2:
        multiplicar = num * num2
        print('\n')
        print('{} * {} = {}'.format(num, num2, multiplicar))
    elif opcao == 3:
        maior = num > num2
        if maior == False:
            print('\n')
            print(f'O maior numero é {num2}')
        else:
            print('\n')
            print(f'O maior numero é {num}')
    elif opcao == 4:
        print('\n')
        num = float(input('Digite o numero 1: '))
        num2 = float(input('Digite o numero 2: '))
    elif opcao == 5:
        print('Finalizando...')
        for c in range(3, 0, -1):
            time.sleep(0.5)
            print(f'{c}')
        print('Até a proxima -_-')
    print('=' * 30)



