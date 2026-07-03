print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

boletim = []
aluno = {'nome' : str(input('Nome: ')), 'media' : float(input('Media: '))}
boletim.append(aluno)

if boletim[0]['media'] >= 7:
    for k,v in boletim:
        print(f'A media do(a) {boletim[0]['nome']} foi igual a {boletim[0]['media']}')
        print('Parabens voce foi aprovado')
else:
    for k,v in boletim:
        print(f'A media do(a) {boletim[0]['nome']} foi igual a {boletim[0]['media']}')
        print('Ixii voce foi reprovado')