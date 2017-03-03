from tkinter import *
from index import processarProjetos


class IncluirProjeto:
    def __init__(self,toplevel):
        self.frame1=Frame(toplevel)
        self.frame1.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack()
        self.frame3 = Frame(toplevel, pady=10)
        self.frame3.pack()
        self.frame4=Frame(toplevel,pady=10)
        self.frame4.pack()
        Label(self.frame1,text='Verificador do Indicador de Efetividade', fg='darkblue',
              font=('Verdana','14','bold'), height=3).pack()

        fonte1=('Verdana','10','bold')

        Label(self.frame2,text='Projeto: ', font=fonte1, width=8).pack(side=LEFT)
        self.nome=Entry(self.frame2,width=15, font=fonte1)
        self.nome.pack(side=LEFT)


        self.confere=Button(self.frame3, font=fonte1, text='Cadastrar', command=self.conferir)
        self.confere.pack()
        self.msg=Label(self.frame3,font=fonte1,height=3)
        self.msg.pack()

        self.confere = Button(self.frame4, font=fonte1, text='Processar', command=self.validar)
        self.confere.pack()
        self.msg = Label(self.frame4, font=fonte1, height=2)
        self.msg.pack()

    def conferir(self):
        processarProjetos.processar(self.nome.get())

    def validar (self):
        processarProjetos.validarProjetos()


instancia=Tk()
IncluirProjeto(instancia)
instancia.mainloop()

