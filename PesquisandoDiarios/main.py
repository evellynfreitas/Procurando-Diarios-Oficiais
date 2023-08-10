import customtkinter as ctk
from pagina_diarios import listarDiarios


def click():
    pes = pesquisa.get()
    data_ini = dataInicial.get()
    data_fim = dataFinal.get()

    municipios_escolhidos = []
    if checkbox_todos.get() == 1:
        municipios_escolhidos = municipios
    else:
        for check in lista_checkbox:
            if check.get() == 1:
                municipios_escolhidos.append(check.cget('text'))

    listarDiarios(municipios_escolhidos, pes, data_ini, data_fim)


janela = ctk.CTk()
janela.geometry('830x450')
janela.title('CAD-RECEITA')
janela.configure(fg_color='white')

# janela.iconbitmap('recursos/lupa.ico')
janela.resizable(False, False)

label1 = ctk.CTkLabel(janela, text="Procurar nos Diários Oficiais")
label1.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

pesquisa = ctk.CTkEntry(janela, placeholder_text="Digite a palavra chave")
pesquisa.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

dataInicial = ctk.CTkEntry(janela, placeholder_text="Digite a data inicial")
dataInicial.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

dataFinal = ctk.CTkEntry(janela, placeholder_text="Digite a data final")
dataFinal.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

label2 = ctk.CTkLabel(janela, text="Escolha os municípios:")
label2.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

municipios = ['Areal', 'Arraial do Cabo', 'Belford Roxo', 'Búzios', 'Cabo Frio', 'Casimiro de Abreu',
              'Comendador Levy', 'Cordeiro', 'Iguaba Grande', 'Itaboraí', 'Macaé', 'Niteroi', 'Nova Friburgo',
              'Nova Iguaçu', 'Quatis', 'Queimados', 'Quissamã', 'São Gonçalo', 'São João de Meriti',
              'São José do Vale do Rio Preto', 'São Pedro da Aldeia', 'Sapucaia', 'Sumidouro', 'Varre-Sai',
              'Volta Redonda']

lista_checkbox = []

checkbox_todos = ctk.CTkCheckBox(janela, text='Pesquisar em Todos', onvalue=1, offvalue=0,
                                 hover_color="#D69706", fg_color="#D69706")

checkbox_todos.grid(row=5, column=2, padx=5, pady=5, sticky="ew")
lista_checkbox.append(checkbox_todos)

coluna = 0
linha = 6

for m in municipios:
    checkbox = ctk.CTkCheckBox(janela, text=m, onvalue=1, offvalue=0, hover_color="#D69706", fg_color="#D69706")
    checkbox.grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")
    lista_checkbox.append(checkbox)
    coluna += 1
    if coluna == 5:
        coluna = 0
        linha += 1

# my_font = ctk.CTkFont(family="<family name>", size=<size in px>, <optional keyword arguments>)

botao = ctk.CTkButton(janela, text='Pesquisar', command=click,  fg_color=("#D69706", "white"))

botao.grid(row=linha+1, column=2, padx=10, pady=10, sticky="ew")

janela.mainloop()
# pyinstaller --onefile --icon=recursos/lupa.ico main.py
