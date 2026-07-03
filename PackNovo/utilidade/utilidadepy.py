
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

