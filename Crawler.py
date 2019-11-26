import requests
from bs4 import BeautifulSoup  # biblioteca para fazer parsing de html

dominio = 'https://django-anuncios.solyd.com.br/'
url = 'https://django-anuncios.solyd.com.br/automoveis/'


def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Error ao fazer a requisição")
    except:
        print("Erro ao fazer a requisição")


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except:
        print("Erro ao fazer o parsing html")

def encontrar_links(soup):
    cards_pai = soup.find("div", class_="ui three doubling link cards")
    cards = cards_pai.find_all("a")

    links = []
    for card in cards:
        link = card['href']
        links.append(link)

    return links


resposta = buscar(url)
if resposta:
    soup = parsing(resposta)
    if soup:
        links = encontrar_links(soup)
        print(links)
