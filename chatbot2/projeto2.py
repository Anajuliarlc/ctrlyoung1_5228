import random as r

def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("Chatbot",nome)

def saudacao_GUI(nome):
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá!", "Oi, tudo bem?"]
    print(frases[r.randint(0,2)]) 

def salva_sugestao(sugestao):
        with open("base.txt","a+") as base:
                base.write("Chatbot: " + sugestao + "\n")
    
def buscaResposta(nome, texto):
    with open("base.txt", "+a") as base: #append + read
        base.seek(0) #começa no inicio do arquivo
        while True: 
            ver = base.readline()
            if ver != "":
                if jaccard(texto,ver) > 0.3:
                    proximalinha = base.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                base.write('\n' + texto)
                return "Me desculpe, não sei o que falar"
            
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/(len(textoBase.split()))
    

def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase