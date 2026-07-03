print('===== \033[31mDESAFIO\033[m =====')
print('Bem vindo a \033[33mcalculadora\033[m de produtos')
preco = float(input('Digite o valor do produto: '))

print('\n')

print('1 - \033[32mDinheiro/Cheque\033[m')
print('2 - \033[32mCartão à vista\033[m')
print('3 - \033[33mCartão 2x\033[m')
print('4 - \033[33mCartão 3x\033[m')
metodo = int(input('Escolha o metodo de pagamento: '))

if metodo == 1:
    preco = preco * 0.9
    print(f'O valor final do produto no dinheiro/cheque é: R${preco:.2f}')
if metodo == 2:
    preco = preco * 0.95
    print(f'O valor final do produto no cartão à vista é: R${preco:.2f}')
if metodo == 3:
    x2 = preco / 2
    print(f'O valor final do produto é 2x no cartão de  R${x2:.2f} e o preço final é R${preco:.2f}')
if metodo == 4:
    x3 = (preco * 1.2)/3
    preco = preco * 1.2
    print(f'O valor final do produto é 3x no cartão de R${x3:.2f} e o preço final é R${preco:.2f}')