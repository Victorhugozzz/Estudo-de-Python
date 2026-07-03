print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

num0a20 = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    opcao = int(input('Digite um numero inteiro entre 0 e 20: '))

    if opcao < 0 or opcao > 20:
        print('Tente novamente. digite um numero entre 0 e 20')
    elif opcao != num0a20:
        print(f'Voce digitou o número {num0a20[opcao]}')
        break
