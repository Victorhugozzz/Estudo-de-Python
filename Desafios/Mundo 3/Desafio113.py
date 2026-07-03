def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO!\033[m Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('\033[31m O usuario nao iformou o valor!\033[m')
            return 0 
        else:
            return n

def leiafloat(msg):
    while True:
       try:
           m = float(input(msg))
       except (ValueError,TypeError):
           print('\033[31mERRO!\033[m Digite um número real válido.')
           continue
       except (KeyboardInterrupt):
           print('\033[31m O usuario nao iformou o valor!\033[m')
           return 0
       else:
           return m

n = leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar os números \nInteiro: {n} \nReal: {m}')