import customtkinter as ctk


class PaginaDiarios:
    def __init__(self, lista_municipios, pesquisa, data_inicial, data_final):

        self.lista_municipios = lista_municipios
        self.pesquisa = pesquisa
        self.data_inicial = data_inicial
        self.data_final = data_final

        self.janela = ctk.CTk()
        self.janela.geometry('600x500')
        self.janela.title('CAD-RECEITA')
        self.janela.resizable(False, False)

        label1 = ctk.CTkLabel(self.janela, text="Municípios:")
        label1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.listar_diarios()
        self.janela.mainloop()

    def listar_diarios(self):
        texto = ''
        for municipio in self.lista_municipios:
            texto += municipio + " \n "

        texto2 = self.pesquisa + ' | ' + self.data_inicial + ' | ' + self.data_final
        label2 = ctk.CTkLabel(self.janela, text=texto2)
        label2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        label3 = ctk.CTkLabel(self.janela, text=texto)
        label3.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        textbox = ctk.CTkTextbox(self.janela)
        textbox.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0

