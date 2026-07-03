def ficha():
    nome = input('Nome do jogador: ')
    gols = input('Número de gols: ')
    if nome == '':
        nome = '<desconecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
ficha()