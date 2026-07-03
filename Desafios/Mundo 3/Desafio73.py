print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

tabela = ("Palmeiras",
    "Flamengo",
    "Fluminense",
    "São Paulo",
    "Athletico-PR",
    "Bragantino",
    "Coritiba",
    "Bahia",
    "Botafogo",
    "Atlético-MG",
    "Internacional",
    "Vasco da Gama",
    "Cruzeiro",
    "EC Vitória",
    "Grêmio",
    "Santos",
    "Corinthians",
    "Remo",
    "Mirassol",
    "Chapecoense"
)
print('Resultado'.center(30, " "))
print('Os 5 Primeiros colocados do Campionato Brasileiro de Futibol sao: ')

for c in tabela[0:5]:
    print(f'{c} -> ', end='')

print('\n')
print('Os 4 Últimos colocados do Campionato Brasileiro de Futibol sao: ')

for c in tabela[-4:]:
    print(f'{c} -> ', end='')

print('\n')
print('Os nomes dos times em ordem alfabetica ')
print(sorted(tabela))
print('\n')

print(f'O  {tabela[-1]} esta na 20 posição')


