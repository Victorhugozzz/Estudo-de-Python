import time

print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('Bem vindo a queima de fogos ')
print('=' * 20)

opcao = int(input('1 - Iniciar\n2 - Sair\nEscolha: '))

if opcao == 1:
    print('\nIniciando contagem...\n')

    for segundo in range(10, -1, -1):
        print(f'\033[33m{segundo}\033[m')
        time.sleep(1)

    print('\n\033[32m🎆 BOOOOM 🎆\033[m')

else:
    print('Programa encerrado.')