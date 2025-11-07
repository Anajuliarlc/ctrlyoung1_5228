import random as r

def saudacoes(nome):
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá!", "Oi, tudo bem?"]
    print(frases[r.randint(0,2)]) 

def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavrasProibida = ["ódio", "aff"]
    for palavra in palavrasProibida:
        if palavra in texto:
            print("Você digitou algo proibido. Respeite as diretrizes.")
            return recebeTexto()
        return texto
    
def buscaResposta(nome, texto):
    with open("base.txt", "+a") as base: #append + read
        base.seek(0) #começa no inicio do arquivo
        while True: 
            ver = base.readline()
            if ver != "":
                if texto.replace("Cliente: ","") == "Tchau":
                    print(nome + ": volte sempre!")
                    return "fim"
                elif ver.strip() == texto.strip():
                    proximalinha = base.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                print("me desculpe, não sei o que falar")
                base.write("\n" + texto)
                resposta_cli = input("O que esperava?\n")
                base.write("\n" + "Chatbot: " + resposta_cli)
                return "Aprendendo..."
            

def exibeResp(resposta, nome):
    print(resposta.replace("Chatbot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"