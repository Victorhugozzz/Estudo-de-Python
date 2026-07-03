print('===== \033[31mDESAFIO\033[m =====')
print('Bem vindo ao calculo de IMC')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu peso esta abaixo do ideal')
elif (imc >= 18.5) and (imc <= 25):
    print('Seu peso esta no valor ideal')
elif (imc >= 25) and (imc <= 30):
    print('Seu peso esta na faixa de sobrepeso')
elif (imc >= 30) and (imc <= 40):
    print('Seu peso esta na faixa de obesidade')
else:
    print('Seu peso esta na faixa de obesidade morbita')