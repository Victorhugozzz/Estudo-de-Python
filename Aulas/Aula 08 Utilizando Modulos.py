from math import sqrt, ceil
import random
num = int(input('Digite um numero: '))
raiz = sqrt(num)
num1 = random.randint(1,10)
print('A raiz de {} e igual a {}'.format(num, ceil(raiz)))
print(num1)