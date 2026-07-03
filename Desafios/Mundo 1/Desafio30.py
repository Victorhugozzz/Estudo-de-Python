print('===== DESAFIO =====')
speed = int(input('Digite qual a velocidade que estava o carro: '))
fine = float((speed-80)*7)
if speed > 80:
    print ('O carro foi multado o valor da multa e R${:.2f}'.format(fine))
else:
    print ('O carro nao foi multado')