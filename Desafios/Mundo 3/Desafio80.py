print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

valores = []

for c in range(1, 6):
    a = int(input('Digite um valor inteiro: '))

    if not valores:
        valores.append(a)

    elif a > valores[-1]:
        valores.append(a)

    else:
        pos = 0

        while pos < len(valores):

            if a <= valores[pos]:
                valores.insert(pos, a)
                break

            pos += 1
print('-=-' *10)
print(f'Os valores digitados em ordem sao {valores}')