print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)
soma = 0
opcao = ''
num_total = 0
while opcao != 'N':
    num = int(input('Digite um numero inteiro: '))
    soma += num
    num_total += 1

    if num_total == 1:
        maior = num
        menor = num

    if num>maior:
        maior = num

    if num<menor:
        menor = num


    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        media = soma/num_total
        print('=' * 30)
        print('Informações dos numeros:')
        print(f'Média = {media:.2f}')
        print(f'Maior numero = {maior}')
        print(f'Menor numero = {menor}')


