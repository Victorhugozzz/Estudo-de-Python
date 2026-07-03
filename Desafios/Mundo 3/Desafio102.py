def fatorial(num = 1, show_process = False):
    """ Calcula o fatorial de um numero inteiro sem ser negativo 
    :param num: = O numero a ser calculado
    :param show_process: = (opicional) mostra o processo de calculo ou nao
    :return f: = O valor do fatorial de um numero
    """
    if num < 0:
        return 'Não existe fatorial de número negativo.'
    elif num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        if show_process == False:
            print(f'{num}! = ', end='')
        else:
            print(f'{num}! = ', end='')
            for i in range(num, 0, -1):
                print(f'{i}', end='')
                if i > 1:
                    print(' x ', end='')
                else:
                    print(' = ', end='')
        f = 1
        for i in range(num, 0, -1):
            f *= i
        return f
num = int(input('Digite um número para calcular seu fatorial: '))
m = input('Deseja mostrar o processo? [S/N] ').strip().upper()[0]
if m == 'S':
    show_process = True
else:    show_process = False
fat = fatorial(num, show_process)
print(fat)
help(fatorial)