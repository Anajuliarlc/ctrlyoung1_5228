try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Encerrando operação...")
    if 'arquivo' in locals():
        arquivo.close()