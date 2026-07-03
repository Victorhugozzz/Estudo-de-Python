def leiaint(msg):
    while True:
        n = input(msg)
        
        if n.isnumeric():
            return int(n)
        print('\033[31mERRO!\033[m Digite um número inteiro válido.')
      
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
        