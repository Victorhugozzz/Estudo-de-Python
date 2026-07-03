print('===== DESAFIO 14 =====')
salario = float(input('Digite seu salário:'))
aumento = 15
novo = salario * (1 + aumento/100)
print('O valor novo salario ja com o aumento R$ {:.2f}: '.format(novo))