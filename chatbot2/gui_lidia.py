import projeto2 as p2
from tkinter import *

main_w = Tk()

main_w.title("Lidia")
main_w.geometry("500x500")
main_w.grid()

frame = Frame(main_w)
frame.grid()

l_identif = Label(frame, text="Insira uma mensagem aqui: ")
l_identif.grid(row=0, column=0)

e_mensagem = Entry(frame)
e_mensagem.grid(row=0, column=1)

frame2 = Frame(main_w)
frame2.grid(row=1,column=0)
v = StringVar()
Label(frame2, textvariable=v).grid()

nome_bot = "Lidia"
v.set("Qual seu nome?")
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ""

def roda_Chatbot():      
    global entrada_sugestao
    global entrada_nome_usuario
    global historico_conversa
    global nome_usuario
    global nome_bot
    
    if entrada_nome_usuario:
        nome_usuario = e_mensagem.get()
        saudacao = p2.saudacao_GUI(nome_bot)
        historico_conversa = nome_bot+": "+saudacao+"\n"
        v.set(historico_conversa)
        entrada_nome_usuario = False
    else:
        texto = e_mensagem.get()
        historico_conversa+="\n "+nome_usuario+": "+texto
        v.set(historico_conversa)
        
        if entrada_sugestao:
            p2.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa+="\n Agora aprendi! Vamos continuar nossa conversa...\n"
            v.set(historico_conversa)

        else:
            resposta = p2.buscaResposta_GUI("Cliente: "+texto+"\n")
            
            if resposta == "Me desculpe, não sei o que falar":
                historico_conversa += "\n Me desculpe, não sei o que falar. O que você esperava? \n"
                v.set(historico_conversa)
                entrada_sugestao = True
            else:               
                historico_conversa += "\n"+p2.exibeResposta_GUI(texto,resposta, nome_bot)
                v.set(historico_conversa)

Button(frame, text="Clique", command=roda_Chatbot).grid(row=0, column=2)
main_w.mainloop()