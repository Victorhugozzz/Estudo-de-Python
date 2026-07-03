print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

def area(a, b):
  s = a * b
  print(f'A area do terreno com as dimencoes de {a} m largura e {b}m comprimento e {s} metros quadrados')
  

def traco(msg):
  print('-'*20)
  print(msg)
  print('-'*20)
  
  
traco('Controle de terreno')
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))