from datetime import date

print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

pessoa = {
    'nome': str(input('Nome: ')),
    'ano': int(input('Ano de nascimento: ')),
    'carteira': int(input('Carteira de trabalho (0 se não tiver): '))
}

pessoa['idade'] = date.today().year - pessoa['ano']

if pessoa['carteira'] != 0:
    pessoa['ano2'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano2'] + 35) - date.today().year)

print('=-=' * 20)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
print('=-=' * 20)