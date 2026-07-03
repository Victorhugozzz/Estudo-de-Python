from PackFun import moeda

valor = float(input('Digite um valor: R$ '))

print(f'A metade de {moeda.formatacao(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.formatacao(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 10% de {moeda.formatacao(valor)} temos {moeda.aumento(valor, 10, True)}')
print(f'Reduzindo 13% de {moeda.formatacao(valor)} temos {moeda.reducao(valor, 13, True)}')