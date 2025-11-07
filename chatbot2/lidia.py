import projeto as p

nome_bot = "Lidia"
p.saudacoes(nome_bot)

while True:
    texto = p.recebeTexto()
    resposta = p.buscaResposta(nome_bot, texto)
    if p.exibeResp(resposta, nome_bot) == "fim":
        break 