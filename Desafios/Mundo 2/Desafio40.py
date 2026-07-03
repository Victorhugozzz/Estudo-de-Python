print('===== \033[31mDESAFIO\033[m =====')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = float((nota1 + nota2)/2)

if media < 5:
    print('\033[1;31mREPROVADO\033[m')
elif (media >= 5) and (media <= 6.9):
    print('\033[1;33mRECUPERACAO\033[m')
elif media >= 7:
    print('\033[1;32mAPROVADO\033[m')