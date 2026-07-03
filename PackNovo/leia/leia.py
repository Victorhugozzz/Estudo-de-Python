def leiavalor(msg):
   valido = False
   while not valido:
       entrada = str(input(msg)).replace(',', '.').strip()
       if entrada.isalpha() :
           print(f'\033[0;31mERRO: \"{entrada}\"\033[m e um preco ivalidado!')
       else:
           valido = True
           return float(entrada)