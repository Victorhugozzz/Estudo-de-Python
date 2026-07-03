from datetime import date

print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)
ano_atual = date.today().year

maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'A quantidade de pessoas que sao maiores de idade sao {maior}')
print(f'A quantidade de pessoas que sao menores de idade sao {menor}')