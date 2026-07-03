
palavras = (
    'APRENDER',
    'PROGRAMAR',
    'LINGUAGEM',
    'PYTHON',
    'CURSO',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMADOR',
    'FUTURO'
)
for c in palavras:
    vogais = [letra for letra in c if letra.lower() in 'aeiou']
    print(f'\nNa palavra {c} temos {vogais}', end='')