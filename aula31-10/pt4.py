import requests
from bs4 import BeautifulSoup

# URL da música específica
url = "https://www.letras.mus.br/the-warning/six-feet-deep/"

# Faz o download do conteúdo da página
resposta = requests.get(url)

# Cria o objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# Tenta encontrar a letra (verificando os padrões mais usados no Letras)
letra = soup.find("div", id="lyrics") or soup.find("div", class_="lyric-original")

# Verifica se encontrou e exibe o texto
if letra:
    texto_letra = letra.get_text(strip=True)
    print(texto_letra[:300])  # Mostra os 300 primeiros caracteres
else:
    print("Letra não encontrada.")