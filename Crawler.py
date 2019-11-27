import requests
import re #expressão regular
from bs4 import BeautifulSoup  # biblioteca para fazer parsing de html

dominio = "https://django-anuncios.solyd.com.br"
url = "https://django-anuncios.solyd.com.br/automoveis/"


def requisicao(url):
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
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)


def encontrar_links(soup):
    try:
        cards_pai = soup.find("div", class_="ui three doubling link cards")
        cards = cards_pai.find_all("a")
    except:
        print("Erro ao encontrar links")
        return None

    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            pass

    return links

def encontrar_telefone(soup):
    try:
        descricao = soup.find_all("div", class_="sixteen wide column")[2].p.get_text().strip()
    #olhando o site vemos que a parte inde se encontra o telefone está na class "sixteen wide column"
    #mas existe 3 sixteen wide column e o telefone está na terceira "[2]"
    #Além disso, ela está dentro de uma tag <p>
    except:
        print("erro ao encontrar descrição")

    regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", descricao)
    if regex:
        return regex

resposta_busca = requisicao(url)
if resposta_busca:
    soup_busca = parsing(resposta_busca)
    if soup_busca:
        links = encontrar_links(soup_busca)
        resposta_anuncio = requisicao(dominio + links[11])
        if resposta_anuncio:
            soup_anuncio = parsing(resposta_anuncio)
            print(soup_anuncio.prettify())
