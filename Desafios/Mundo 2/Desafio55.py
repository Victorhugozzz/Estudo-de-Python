
print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

pesos = []
for c in range(5):
    peso = float(input(f'Digite o peso da {c+1}ª pessoa em kg: '))
    pesos.append(peso)

print('=' * 25)
print(f'O maior peso: {max(pesos)} Kg')
print(f'O menor peso: {min(pesos)} Kg')
print('=' * 25)