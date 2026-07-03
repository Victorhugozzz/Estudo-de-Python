nome = str(input('Digite seu nome completo: '))
print('\033[31m===== DESAFIO 26 =====\033[m')
if  "Silva" in nome.title():
    print(f'No nome \033[36m{nome}\033[m, há palavra Silva')
else:
    print(f'No nome \033[36m{nome}\033[m, não há a palavra Silva')