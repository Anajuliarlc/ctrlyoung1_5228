import requests
from bs4 import BeautifulSoup

url = "https://www.letras.mus.br/the-warning/hell-you-call-a-dream/"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, "html.parser")

titulo = sopa.find("title")
print("Título da página:", titulo.text)
