def notas(*valores, sit=False):
    resultado = {}
    resultado['total'] = len(valores)
    resultado['maior'] = max(valores)
    resultado['menor'] = min(valores)
    resultado['média'] = sum(valores) / len(valores)
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'BOA'
        elif resultado['média'] >= 5 and resultado['média'] < 7:
            resultado['situação'] = 'RAZOÁVEL'
        elif resultado['média'] >= 0 and resultado['média'] < 5:
            resultado['situação'] = 'RUIM'
    return resultado

lista = []

while True:
    n1 = float(input('Digite uma nota: '))

    if n1 < 0 or n1 > 10:
        print('\033[31mERRO!\033[m Digite uma nota válida entre 0 e 10.')
        continue

    lista.append(n1)

    opcao = int(input('Deseja continuar? [1] Sim [2] Não: '))
    if opcao == 2:
        break

print(notas(*lista, sit=True))