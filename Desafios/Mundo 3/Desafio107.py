from PackFun import moeda

valor = float(input('Digite um valor: R$ '))

print(f'A metade de {moeda(valor)} é {moeda.metade(valor)}')
print(f'O dobro de {moeda(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando 10% de {moeda(valor)} temos {moeda.aumento(valor, 10)}')
print(f'Reduzindo 13% de {moeda(valor)} temos {moeda.formatacao(valor, 13)}')