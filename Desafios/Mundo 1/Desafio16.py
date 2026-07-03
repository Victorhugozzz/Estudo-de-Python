print('===== DESAFIO 16 =====')
dias = int(input('Digite a quantidade de dias com o carro: '))
km = int(input('Digite a quantidade de km com o carro: '))
valordia = dias * 60
valorkm = km * 0.15
total = valordia + valorkm
print('\n')
print('Após usar {} dias e rodar {} km \n'
      'O valor total a ser pago é R$ {:.2f}\n'.format(dias, km, total))