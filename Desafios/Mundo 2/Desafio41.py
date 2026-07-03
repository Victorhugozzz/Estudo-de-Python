import datetime
print('===== \033[31mDESAFIO\033[m =====')
data = int(input('Digite sua data de nascimento: '))
idade = datetime.date.today().year - data

if idade <= 9:
    print('\033[36mMIRIM\033[m')
elif idade <= 14:
    print('\033[32mINFANTIL\033[m')
elif idade <= 19:
    print('\033[33mJUNIOR\033[m')
elif idade <= 20:
    print('\033[34mSENIOR\033[m')
else:
    print('\033[31mMASTER\033[m')