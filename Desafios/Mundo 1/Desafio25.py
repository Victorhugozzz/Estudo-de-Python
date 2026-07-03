from gettext import find

num = str(input('Digite o nome da cidade: '))
print('\033[31m===== DESAFIO 25 =====\033[m')
if num.strip().startswith("santo" or "Santo" or "SANTO"):
    print(f'O nome da cidade "{num}" começa com a palavra Santo')
else:
    print(f'O nome da cidade "{num}" não começa com a palavra Santo')