def titulo(msg):
    print('-'*40)
    print(msg.center(40))
    print('-'*40)

def leiaint(msg):
    while True:
        idade = input(msg)
        
        if idade.isnumeric():
            return int(idade)
        print('\033[31mERRO!\033[m Digite um número inteiro válido.')


# Programa Principal

titulo('MENU PRINCIPAL ')

while True:
    print('\033[32m1\033[m -\033[31m Ver pessoas cadastradas\033[m')
    print('\033[32m2\033[m -\033[31m Cadastrar nova pessoa\033[m')
    print('\033[32m3\033[m -\033[31m Sair do Sistema\033[m')
    print('-'*40)
    
    escolha = int(input('Escolha uma opção: '))
    
    if escolha == 1:
        try:
            with open("arquivo.txt", "x", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
        except:
            with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
        print('-'*40)
         
    elif escolha == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        print(f'Novo cadastro de {nome} com {idade} anos cadastrado com sucesso!')
        print('-'*40)
        with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f'{nome:<20}{idade} anos\n')
        
    elif escolha == 3:
        titulo('SAINDO DO SISTEMA... ATE LOGO!')
        break
    
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
        print('-'*40)
        continue
