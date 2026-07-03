import datetime
print('===== \033[31mDESAFIO\033[m =====')
ano = int(input('Qual o ano em que voce nasceu? : '))
idade = datetime.date.today().year - ano
if idade < 18:
    tempo = 18 - idade
    print(f'Falta {tempo} anos ainda para se alistar ')
elif idade == 18:
    print('Esta na hora de se alistar')
elif idade > 18:
    tempo = idade - 18
    print(f'Ja passou {tempo} anos de se alistar')