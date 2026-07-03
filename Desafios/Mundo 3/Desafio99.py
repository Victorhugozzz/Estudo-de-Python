import random
import time
print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)
lista = []
    
def analise(qtd):
    lista.clear()
    
    print('Valores sorteados: ', end='', flush=True)
    
    for c in range(qtd):
        n = random.randint(1, 9)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        time.sleep(0.5)
    print()
    if qtd == 0:
        
        print('Analisando valores aleatorios...')
        time.sleep(1)
        print('Nenhum numero foi sorteado')
        time.sleep(0.5)
        print('O maior valor sorteado foi: 0')
    else:
        print('Analisando valores aleatorios...')
        time.sleep(1)
        print('A quantidade de numeros sorteados foi: ', len(lista))
        time.sleep(0.5)
        print('O maior valor sorteado foi: ', max(lista))
    

def msgdaAnalise():
    print('-=-'* 8)
    analise(6)
    print('-=-'* 8)
    analise(3)
    print('-=-'* 8)
    analise(2)
    print('-=-'* 8)
    analise(0)
    print('-=-'* 8)
    
    
msgdaAnalise()