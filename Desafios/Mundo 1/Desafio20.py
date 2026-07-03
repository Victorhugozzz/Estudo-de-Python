import random

n1 = random.randint(1,4)

alunos = {
    1: "Ana",
    2: "Pedro",
    3: "Maria",
    4: "Lucas"
}


print('===== DESAFIO 20 =====')
print(f'O aluno escolhido foi {alunos.get(n1, "invalido")}')