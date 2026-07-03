import os
def buscar_mp3(pasta):
        for raiz, dirs, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if arquivo.endswith('.mp3'):
                    return os.path.join(raiz, arquivo)
        return None
pasta = os.path.expanduser('~/Music')

arquivo = buscar_mp3(pasta)
if arquivo:
    print(f'Tocando {arquivo}')
    os.startfile(arquivo)
else:
    print('nenhum MP3 encontrado')