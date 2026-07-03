from PackFun import moeda

valor = float(input('Digite um valor: R$ '))

print(f'A metade de {moeda.formatacao(valor)} é {moeda.formatacao(moeda.metade(valor))}')
print(f'O dobro de {moeda.formatacao(valor)} é {moeda.formatacao(moeda.dobro(valor))}')
print(f'Aumentando 10% de {moeda.formatacao(valor)} temos {moeda.formatacao(moeda.aumento(valor, 10))}')
print(f'Reduzindo 13% de {moeda.formatacao(valor)} temos {moeda.formatacao(moeda.reducao(valor, 13))}')