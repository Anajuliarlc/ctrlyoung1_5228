import re
import unicodedata
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.letras.mus.br/red-velvet/dumb-dumb/"

def baixar_html(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    return None  # mantemos simples (escopo da apostila)

def normalizar_texto(txt):
    # minúsculas
    txt = txt.lower()
    # remover acentos
    txt = ''.join(c for c in unicodedata.normalize('NFD', txt)
                  if unicodedata.category(c) != 'Mn')
    # tratar hífens como separadores (ex.: "dumb-dumb" -> "dumb dumb")
    txt = txt.replace('-', ' ')
    # manter apenas letras e espaços
    txt = re.sub(r'[^a-z\s]', ' ', txt)
    # colapsar espaços
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def extrair_letra(html):
    """
    Sem depender de classes/ids específicos (para ficar no escopo da apostila):
    - juntar o texto de todos os <p>
    - isso geralmente cobre os versos no Letras
    """
    sopa = BeautifulSoup(html, "html.parser")
    # print(sopa.prettify())  # use para inspecionar a estrutura quando necessário
    ps = sopa.find_all("p")
    versos = []
    for p in ps:
        t = (p.get_text(separator=' ', strip=True) or "").strip()
        if len(t.split()) > 2:
            versos.append(t)
    return "\n".join(versos).strip()

def contar_alvos(texto, alvos):
    """
    Conta palavras-alvo com correspondência exata de palavra
    (após normalização). 'dumb-dumb' vira 'dumb dumb' e conta 2.
    """
    norm = normalizar_texto(texto)
    tokens = norm.split()
    cont = {alvo: 0 for alvo in alvos}
    for tok in tokens:
        if tok in cont:
            cont[tok] += 1
    return cont

def main():
    html = baixar_html(URL)
    if not html:
        print("Não foi possível acessar a página (status != 200).")
        return

    letra = extrair_letra(html)
    if not letra:
        print("Não foi possível extrair a letra (estrutura diferente/JS).")
        return

    alvos = ["dumb", "crazy", "baby"]
    contagens = contar_alvos(letra, alvos)

    # Mostrar no console
    for palavra, qtd in contagens.items():
        print(f"{palavra}: {qtd}")

    # Salvar em CSV com pandas
    df = pd.DataFrame(
        [{"palavra": k, "contagem": v} for k, v in contagens.items()]
    )
    df.to_csv("contagem_red_velvet_dumb_dumb.csv", index=False, encoding="utf-8")
    print("Arquivo salvo: contagem_red_velvet_dumb_dumb.csv")

if __name__ == "__main__":
    main()

