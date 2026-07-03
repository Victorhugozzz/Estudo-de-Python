print('===== \033[31mDESAFIO\033[m =====')
num = int(input('\033[37;mDigite um numero inteiro para a convercao: \033[m'))

print('1- \033[32mConverter para binario\033[m')
print('2- \033[34mConverter para octal\033[m')
print('3- \033[33mConverter para hexadecimal\033[m')
conv = int(input('Digite para qual numero deseja converter: '))
if conv == 1 :
    num = bin(num)[2:]
    print(f'{num} em binario')
elif conv == 2:
    num = oct(num)[2:]
    print(f'{num} em octal')
elif conv == 3:
    num = hex(num)[2:]
    print(f'{num} em hexadecimal')
else:
    print('Opicao invalida')
