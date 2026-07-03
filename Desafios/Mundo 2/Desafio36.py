print('===== \033[31mDESAFIO\033[m =====')
print('Seja bem vindo ao sistema de emprestimo para compra de imoveis')
precototal = int(input('Digite o valor do imovel: '))
salario = float(input('Digite o valor do salario: '))
anos = float(input('Digite em quantos anos vai pagar: '))

prestacao = precototal / (anos * 12)

if prestacao < salario * 0.3:
    print('O seu emprestimo foi aprovado')
else:
    print('O seu emprestimo foi reprovado')

