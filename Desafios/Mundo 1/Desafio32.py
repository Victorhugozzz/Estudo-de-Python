print('===== \033[31mDESAFIO\033[m =====')
dist = float(input('Digite a distancia em km: '))

if dist <= 200:
    dist200 = dist * 0.5
    print('O valor da passagem para a distancia {} km é R${:.2f}'.format(dist,dist200))
else:
    dist201 = dist * 0.45
    print('O valor da passagem para a distancia {} km é R${:.2f}'.format(dist,dist201))