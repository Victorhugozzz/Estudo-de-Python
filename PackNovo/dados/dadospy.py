from PackNovo.utilidade.utilidadepy import (
    formatacao,
    metade,
    dobro,
    aumento,
    reducao,
)

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