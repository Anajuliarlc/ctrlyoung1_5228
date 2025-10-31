import requests
from bs4 import BeautifulSoup as bs

url = "https://www.letras.mus.br/red-velvet/dumb-dumb/"
resposta = requests.get(url)
sopa = bs(resposta.text, "html.parser")

letra = sopa.find("div", class_="lyric-original")

if letra:
    texto = letra.get_text(strip=True).lower()
    palavras = ["dumb", "crazy", "baby"]

    for palavra in palavras:
        total = texto.count(palavra)
        print(f"{palavra}: {total}")
else:
    print("Letra não encontrada.")