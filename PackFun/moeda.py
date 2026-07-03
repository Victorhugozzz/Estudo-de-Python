def formatacao(valor):
    return f'R$ {valor:.2f}'


def metade(valor, formato=False):
    res = valor / 2
    return formatacao(res) if formato else res


def dobro(valor, formato=False):
    res = valor * 2
    return formatacao(res) if formato else res


def aumento(valor, taxa, formato=False):
    res = valor + (valor * taxa / 100)
    return formatacao(res) if formato else res


def reducao(valor, taxa, formato=False):
    res = valor - (valor * taxa / 100)
    return formatacao(res) if formato else res

def resumo(valor, valorma, valorme):
     print('_' * 40)
     print('RESUMO DO VALOR'.center(40))
     print('_' * 40)

     print(f'{"Preço analisado:":<30}{formatacao(valor)}')
     print(f'{"Metade do preço:":<30}{metade(valor, True)}')
     print(f'{"Dobro do preço:":<30}{dobro(valor, True)}')
     print(f'{str(valorma) + "% de aumento:":<30}{aumento(valor, valorma, True)}')
     print(f'{str(valorme) + "% de redução:":<30}{reducao(valor, valorme, True)}')
     print('_' * 40)