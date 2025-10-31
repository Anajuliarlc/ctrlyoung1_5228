import pandas as pd

dados = {
    "Nome": ["Ana", "Pedro", "Daniel", "Gabriel", "Miguel", "Davi"],
    "Idade":[22, 17, 15, 14, 14, 14]}

df = pd.DataFrame(dados)
print(df)
