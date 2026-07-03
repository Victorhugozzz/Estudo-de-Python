import requests

try:
    url = "https://www.youtube.com"
    resposta = requests.get(url)
except:
    print('\033[31mO site   não pode ser acessado no momento!\033[m') 
else:
    print('\033[32mO site foi acessado com sucesso!\033[m') 