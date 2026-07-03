print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

def escreva(msg):
    a = len(msg) + 2
    print('-' * a)
    print(f'{msg:<6}')
    print('-' * a)
    
    
escreva('Central de comando')
            