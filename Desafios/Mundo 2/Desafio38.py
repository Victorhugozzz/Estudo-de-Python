print('===== \033[31mDESAFIO\033[m =====')
num = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
if num > num2:
    print('O primeiro valor e maior')
elif num < num2:
    print('O segundo valor e maior')
else :
    print('Os valores sao iguais')
