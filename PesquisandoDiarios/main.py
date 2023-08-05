import customtkinter as ctk
from pagina_diarios import listarDiarios


def click():
    pes = pesquisa.get()
    data_ini = dataInicial.get()
    data_fim = dataFinal.get()

    municipios_escolhidos = []
    indice = 0

    for check in lista_checkbox:
        if check.get() == 1:
            municipios_escolhidos.insert(indice, check.cget('text'))

    listarDiarios(municipios_escolhidos, pes, data_ini, data_fim)


janela = ctk.CTk()
janela.geometry('550x600')
janela.title('CAD-RECEITA')

# janela.iconbitmap('recursos/lupa.ico')
janela.resizable(False, False)

label1 = ctk.CTkLabel(janela, text="Procurar nos Diários Oficiais")
label1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

pesquisa = ctk.CTkEntry(janela, placeholder_text="Digite a palavra chave")
pesquisa.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

dataInicial = ctk.CTkEntry(janela, placeholder_text="Digite a data inicial")
dataInicial.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

dataFinal = ctk.CTkEntry(janela, placeholder_text="Digite a data final")
dataFinal.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

label2 = ctk.CTkLabel(janela, text="Escolha os municípios:")
label2.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

municipios = ['Areal', 'Arraial do Cabo', 'Belford Roxo', 'Búzios', 'Cabo Frio', 'Casimiro de Abreu',
              'Comendador Levy', 'Cordeiro', 'Iguaba Grande', 'Itaboraí', 'Macaé', 'Niteroi', 'Nova Friburgo',
              'Nova Iguaçu', 'Quatis', 'Queimados', 'Quissamã', 'São Gonçalo', 'São João de Mereti',
              'São José do Vale do Rio Preto', 'São Pedro da Aldeia', 'Sapucaia', 'Sumidouro', 'Varre-Sai']

coluna = 0
linha = 5
cont = 0

lista_checkbox = []

for m in municipios:
    checkbox = ctk.CTkCheckBox(janela, text=m, onvalue=1, offvalue=0)
    checkbox.grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")
    lista_checkbox.insert(cont, checkbox)
    cont += 1
    coluna += 1
    if coluna == 3:
        coluna = 0
        linha += 1

botao = ctk.CTkButton(janela, text='Pesquisar', command=click)

botao.grid(row=linha+1, column=1, padx=10, pady=10, sticky="ew")

janela.mainloop()
# pyinstaller --onefile --icon=recursos/lupa.ico main.py
