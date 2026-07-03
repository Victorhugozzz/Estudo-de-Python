print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
if sexo == 'M':
    print('O seu sexo é masculino')
elif sexo == 'F':
    print('O seu sexo é feminino')