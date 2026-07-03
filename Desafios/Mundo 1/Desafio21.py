import random

nomes = ["Ana", "Pedro", "Maria","Lucas"]

random.shuffle(nomes)

print('===== DESAFIO 21 =====')
print('A ordem dos alunos escolido para apresentrar o trabalho é: ')
for nome in nomes:
    print(nome)

