print('===== DESAFIO =====')
pay = float(input('Digite o valor do seu salario para o reajuste: '))
if pay > 1250 :
    pay1 = (1250*0.1) + pay
    print('Seu salario apos o reajuste de 10% e R$ {:.2f}'.format(pay1))
elif pay <= 1250:
    pay1 = (1250*0.15) + pay
    print('Seu salario apos o reajuste de 15% e R$ {:.2f}'.format(pay1))