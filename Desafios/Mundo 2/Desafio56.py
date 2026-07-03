print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

soma_idade = 0
maior_idade = 0
nome_do_homem_mais_velho = ''
mulheres_menor_de20 = 0

print('Para a seleção responda as seguintes questoes \n')

for c in range(4):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')) .strip().upper()
    soma_idade += idade

    #homen
    if sexo == 'M' and idade > maior_idade:
            maior_idade = idade
            nome_do_homem_mais_velho = nome

    #mmuler
    if sexo == 'F' and idade < 20:
        mulheres_menor_de20 += 1

#media
idade_media = soma_idade/4

print('='* 30)
print('\033[31m      DESAFIO\033[m \n')
print("Média: {}".format(idade_media))
print("Homem mais velho: {}".format(nome_do_homem_mais_velho))
print("Quantidade de mulheres com menos de 20 anos: {}".format(mulheres_menor_de20))
print('=' * 30)