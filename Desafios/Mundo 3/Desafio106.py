import time
def tracoVermelho(msg):
    print('\033[0:30:41m' + '~' * len(msg))
    print(msg)
    print('\033[0:30:41m' + '~' * len(msg))

def tracoAzul(msg):
    print('\033[0:30:44m' + '~' * len(msg))
    print(msg)
    print('\033[0:30:44m' + '~' * len(msg))



def main():
    while True:
        tracoVermelho('Sistema de ajuda PyHelp')
        print('\033[m')

        string = input('Função ou Biblioteca (Digite fim para encerrar) > '.strip())

        if string.upper() == 'FIM':
            break
        else:
            tracoAzul(f'Acessando o manual do comando {string}')
            print('\033[m')
            time.sleep(1)
            help(string)
    tracoVermelho('Até logo!')
main()