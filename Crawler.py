import requests
from bs4 import BeautifulSoup #biblioteca para fazer parsing de html

url = 'https://django-anuncios.solyd.com.br/automoveis/'

def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Erro ao fazer a requisição")
    except:
        print("Erro ao fazer a requisição")


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta, 'html.parser')
        return soup
    except:
        print("Erro ao fazer o parsing html")
        
resposta = buscar(url)
if resposta:
    soup = parsing(resposta)
