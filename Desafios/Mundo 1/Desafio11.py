print('===== DESAFIO 11 =====')
n1 = float(input('Digite a quantitadade da sua carteira em R$: '))
dolar = n1/5
euro = n1/5.85
Ienes = n1*31.92

print('1 Em dolares {:.2f}: \n'
      '2 Em euros {:.2f}: \n'
      '3 Em Ienes {:.2f}: \n'.format(dolar,euro,Ienes))