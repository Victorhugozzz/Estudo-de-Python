print('===== \033[31mDESAFIO\033[m =====')
print('Digite os valores em ordem crescente !!')
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
print ('\n')
if a+b > c:
    print ('Pode ser formado um triangulo', end=' ')
    if a == b == c:
        print ('\033[31mequilatero\033[m')
    elif a == b or a == c or b == c:
        print('\033[34misoceles\033[m')
    elif a != b != c  :
        print('\033[36mescaleno\033[m')
else :
    print('Nao pode ser formado o triangulo')
