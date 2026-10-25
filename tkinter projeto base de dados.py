from tkinter import *
from tkinter import messagebox
import random
import time


janela = Tk()
janela.geometry("800x800")
janela.resizable(False,False)

#Can't use code because I lost the images originally used,but you can just replace them if u want to
#sorry, stiil happy with what came up
lista=["camelo","remada","mapear","banhado","pelado"]
imd=PhotoImage(file="C:/Users/AEPAP/Documents/Projeto base de dados/slots acabado.png")
moedin=PhotoImage(file="C:/Users/AEPAP/Documents/Projeto base de dados/a roda da roleta 1.png")
bulacha=PhotoImage(file="C:/Users/AEPAP/Documents/Projeto base de dados/bolacha.png")
bulacha2=PhotoImage(file="C:/Users/AEPAP/Documents/Projeto base de dados/bolachafter.png")
janela.config(bg="#edadd6")
labelot=Label(janela,image=imd)
n1=IntVar()
n2=IntVar()
n3=IntVar()
p1=0
carteira=1050

label1=Label(janela )
label2=Label(janela )
label3=Label(janela )

des='s'
ver1=0
ver2=0
ver3=0
conf1=0
conf2=0
conf3=0
pobreza=0
        
        
def nova_janela_ms():
    def baza():
        label_imd.destroy()
        label_euro.destroy()
        label_guito.destroy()
        label_num1.destroy()
        label_num2.destroy()
        label_num3.destroy()
        labeldesc.destroy()
        fitxa.destroy()
        
        slot_janela.destroy()
    def ms():
        n1=0
        n2=0
        n3=0
        
        global carteira,p1,slot_janela

        if carteira<50:
            messagebox.showinfo("lamento, mas você está sem dinheiro", "mais sorte para a próxima,catxing!")
            
            p1=1
            
        else:

            n1 = random.randint(1, 9)
            n2 = random.randint(1, 9)
            n3 = random.randint(1, 9)
            carteira=carteira-50
            
            label_num1.config(text=str(n1))
            label_num2.config(text=str(n2))
            label_num3.config(text=str(n3))
            carteira1.set(carteira)
            
            if n1==n2 and n2==n3 and n3==7:
                carteira=carteira+100000
                carteira1.set(carteira)
                
                messagebox.showinfo("Parabéns!", "Você ganhou um MEGAprêmio!SUUUUUUUUUUPERRRRR")
            elif n1 == n2 and n2 == n3:
                carteira=carteira+2000
                carteira1.set(carteira)
                
                messagebox.showinfo("Parabéns!", "Você ganhou um prêmio!")
                
            
            elif n1==n2 or n1==n3 or n2==n3:
                carteira=carteira+100
                carteira1.set(carteira)
            
    slot_janela = Toplevel(janela)
    slot_janela.title("Máquina de Slots")
    
    
    global label_num1, label_num2, label_num3,label_guito,carteira,p1
    carteira1=IntVar()
    carteira1.set(carteira)
    label_guito = Label(janela,textvariable=carteira1,background="#edadd6")
    label_guito.place(x=10,y=10)
    label_euro = Label(janela,text="€",background="#edadd6")
    label_euro.place(x=45,y=10)
    label_imd=Label(janela,image=imd,bg="#edadd6")
    label_imd.place(x=250,y=50)
    if p1==0:

    
        label_num1 = Label(janela, text="", font=("Arial", 47),bg="#daa520")
        label_num1.place(x=330,y=145)
        label_num2 = Label(janela, text="", font=("Arial", 47),bg="#daa520")
        label_num2.place(x=390,y=145)
        label_num3 = Label(janela, text="", font=("Arial", 47),bg="#daa520")
        label_num3.place(x=450,y=145)
        
        
        labeldesc=Label(janela,text="Bem Vindo à máquina de slots, você começa o jogo com 1000€, e custa 50€ para rodar a manivela, se tiver 3 números iguais, ganha prémios",background="orange")
        labeldesc.place(x=0,y=600)

    spin_button = Button(slot_janela, text="Girar", command=ms)
    spin_button.pack(pady=20)
    fitxa=Button(janela, text="Sair",command=baza)
    fitxa.pack()
def roleta():
    global carteira1
    nova_janela = Toplevel(janela)
    nova_janela.title("Jogo de Roleta")
    nova_janela.geometry("600x700")
    nova_janela.config(bg="#edadd6")


    def butin():
        nova_janela.destroy()
    
    def girar_roleta():
        
        global carteira,pobreza,avi
        
        
        numero_sorteado = random.randint(1, 36)
        cor_sorteada = random.choice(["Vermelho", "Preto"])
        
        
        numero_apostado = int(numero_var.get())
        cor_apostada = cor_var.get()
        aposta = aposta_var.get()
        if carteira<aposta:
            avi=Label(nova_janela, text="Você está sem dinheiro!CATXING!!!",font=("Sans",27),bg="#edadd6")
            avi.place(x=20,y=20)
            pobreza=1
        else:
            if pobreza==1:
                pobreza=0
                avi.destroy()
            resultado_numero['text'] = f"Número sorteado: {numero_sorteado}"
            resultado_cor['text'] = f"Cor sorteada: {cor_sorteada}"
            if numero_sorteado == numero_apostado and cor_sorteada == cor_apostada:
                ganho = aposta * 45
                carteira1.set(carteira)
                messagebox.showinfo("GANHOU!")
                resultado_aposta['text'] = "Parabéns! Você ganhou {ganho}!"
                carteira=carteira+ganho
            else:
                resultado_aposta['text'] = "Você perdeu. Tente novamente."
                carteira=carteira-aposta
                carteira1.set(carteira)
            

        
        
    numero_var = StringVar()
    carteira1=IntVar()
    Label(nova_janela, text="Escolha um número (1-36):", bg="#edadd6").place()
    numero_escd= Spinbox(nova_janela, textvariable=numero_var, bg="#edadd6")
    numero_escd['values'] = list(range(1, 37))
    numero_escd.pack()

    
    
    cor_var = StringVar()
    Label(nova_janela, text="Escolha uma cor:", bg="#edadd6").pack()
    cor_escolhida = Spinbox(nova_janela, textvariable=cor_var, bg="#edadd6")
    cor_escolhida['values'] = ["Vermelho", "Preto"]
    cor_escolhida.pack()

    mostrarmoe=Label(nova_janela,image=moedin,bg="#edadd6")
    mostrarmoe.pack()
    
    aposta_var = DoubleVar()
    Label(nova_janela, text="Escolha o valor da aposta:", bg="#edadd6").pack()
    aposta_sele = Scale(nova_janela, variable=aposta_var, from_=1, to_=100, orient=HORIZONTAL, bg="#edadd6")
    aposta_sele.pack()
    carteira1.set(carteira)
    mostrar_guita=Label(nova_janela,textvariable=carteira1, bg="#edadd6")
    mostrar_guita.pack()
    
    Button(nova_janela, text="Girar Roleta", command=girar_roleta, bg="#edadd6").pack()

    
    resultado_numero = Label(nova_janela, text="", bg="#edadd6")
    resultado_numero.pack()
    resultado_cor = Label(nova_janela, text="", bg="#edadd6")
    resultado_cor.pack()
    resultado_aposta = Label(nova_janela, text="", bg="#edadd6")
    resultado_aposta.pack()
    Butinho=Button(nova_janela,text="Sair",bg="#edadd6", command=butin)
    Butinho.place(x=20,y=120)
    



def bolacha():
    jogocremoso = Toplevel(janela)
    jogocremoso.title("Jogo da bolacha")
    jogocremoso.geometry("600x600")
    jogocremoso.config(bg="#46549f")
    contagem = 0
    game_duration = 30000


    def update_click_count():
        nonlocal contagem
        global finzin
        
        finzin=0
        #nota do jonhy:a nonlocal serve para indicar que a variável contagem está dentro da função"bolacha", sem ela, apenas seria criada uma nova função não definida com o mesmo nome
        contagem += 1
        mostrarcliques.config(text=f"Cliques: {contagem}", bg="#46549f")
        if contagem > 120:
            mostrarbulacha.destroy()
            clicka.destroy()
            mostrarbulacha2=Label(jogocremoso, image=bulacha2, bg="#46549f")
            mostrarbulacha2.pack()
            messagebox.showinfo("Parabéns!", "Você ganhou e não comeu a bolacha!")
            finzin=1
            
    def edgestreak():
        if finzin==0:
            messagebox.showinfo("Fim de Jogo", f"Você foi o último e teve de comer a bolacha(com creme). Tente novamente!")
            jogocremoso.destroy()
            
    
    desco = Label(jogocremoso, text="Clique no botão o máximo de vezes possível e abra-se!(tem 30 segundos!)", font=("Arial", 14), bg="#46549f")
    desco.pack()
    mostrarbulacha=Label(jogocremoso, image=bulacha, bg="#46549f")
    mostrarbulacha.pack()
    clicka = Button(jogocremoso, text="Clique Aqui!", command=update_click_count, font=("Arial", 18), bg="#46549f")
    clicka.pack()

    mostrarcliques = Label(jogocremoso, text="Cliques: 0", font=("Arial", 14), bg="#46549f")
    mostrarcliques.pack()

    jogocremoso.after(game_duration , edgestreak)




       

menumu=Menu(janela)
janela.config(menu=menumu)
meu_file=Menu(menumu,tearoff=0)

menumu.add_cascade(label="Jogos",menu=meu_file)
btnn=Button(text="Roleta de casino",command=roleta)
btnn2=Button(text="Jogo da bolacha",command=bolacha)
btnn3=Button(text="máquina de slots",command=nova_janela_ms)

btnn.place(x=20,y=50)
btnn2.place(x=120,y=50)
btnn3.place(x=55,y=80)

janela.mainloop()
