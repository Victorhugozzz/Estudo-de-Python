import time
print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        passo = abs(passo)
        for c in range(inicio, fim + 1, passo):
            print(c, end='  ', flush=True)
            time.sleep(0.5)
    elif inicio > fim:
        passo = -abs(passo)
        for c in range(inicio, fim - 1, passo):
            print(c, end='  ', flush=True)
            time.sleep(0.5)
    print()

def escreva(msg):
    a = len(msg) + 2
    print('-' * a)
    print(f'{msg:<6}')
    print('-' * a)


def traco():
    print('-' * 30)
    
    
escreva('BEM VINDO ao contador')
print('Contagem de 0 ate 10 de 1 em 1: ')
contador(0, 10, 1)
traco()
print('Contagem de 10 ate 0 de 2 em 2: ')
contador(10, 0, 2)
traco()

print('Agora e a sua vez -> ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-' * 20)
contador(inicio, fim, passo)
