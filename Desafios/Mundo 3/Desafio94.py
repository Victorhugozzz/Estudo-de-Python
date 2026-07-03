print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

todasasPessoas = list()
pessoa = dict()
opcao = ''

while opcao != 'N':
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').upper().strip()
    
    while pessoa['sexo'] not in 'MF':
        print('Opção inválida!')
        pessoa['sexo'] = input('Sexo [M/F]: ').upper().strip()
        
    pessoa['idade'] = int(input('Idade: '))
    
    todasasPessoas.append(pessoa.copy())
    pessoa.clear()
    
    opcao = input('Quer continuar? [S/N] ').upper().strip()
    while opcao not in 'SN':
        print('Opção inválida!')
        opcao = input('Quer continuar? [S/N] ').upper().strip()
print('=' * 20)
print(f'- Total de pessoas cadastradas: {len(todasasPessoas)}')

media = sum(p['idade'] for p in todasasPessoas) / len(todasasPessoas)
print(f'- Média de idade: {media:.2f}')

mulheres = [p['nome'] for p in todasasPessoas if p['sexo'] == 'F']
print(f'- Mulheres cadastradas: {", ".join(mulheres)}')

print('- Lista das pessoas que estao acima da media: \n')
for p in todasasPessoas:
    if p['idade'] > media:
        print(f'Nome: {p["nome"]} | Idade: {p["idade"]} | Sexo: {p["sexo"]}')
