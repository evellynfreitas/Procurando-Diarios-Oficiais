import pandas as pd
from municipios import areal, arraial_do_cabo, belford_roxo, buzios, cabo_frio, casimiro_de_abreu, comendador_levy
from municipios import cordeiro, iguaba, niteroi, nova_friburgo, quatis, sao_goncalo, sao_joao_mereti
from municipios import sao_jose_do_vale, sao_pedro, sapucaia, varre_sai
import pyautogui
from tkinter.filedialog import asksaveasfilename as salvarcomo


def listarDiarios(lista_municipios, pesquisa, data_inicial, data_final):

    tabela = pd.DataFrame(columns=['Município', 'Data', 'Link'])

    for muni in lista_municipios:

        municipio = ''

        if muni == 'Areal':
            municipio = areal.Areal(pesquisa, data_inicial, data_final)
        elif muni == 'Arraial do Cabo':
            municipio = arraial_do_cabo.Arraial(pesquisa, data_inicial, data_final)
        elif muni == 'Belford Roxo':
            municipio = belford_roxo.BelfordRoxo(pesquisa, data_inicial, data_final)
        elif muni == 'Búzios':
            municipio = buzios.Buzios(pesquisa, data_inicial, data_final)
        elif muni == 'Cabo Frio':
            municipio = cabo_frio.CaboFrio(pesquisa, data_inicial, data_final)
        elif muni == 'Casimiro de Abreu':
            municipio = casimiro_de_abreu.Casimiro(pesquisa, data_inicial, data_final)
        elif muni == 'Comendador Levy':
            municipio = comendador_levy.ComendadorLevy(pesquisa, data_inicial, data_final)
        elif muni == 'Cordeiro':
            municipio = cordeiro.Cordeiro(pesquisa, data_inicial, data_final)
        elif muni == 'Iguaba Grande':
            municipio = iguaba.Iguaba(pesquisa, data_inicial, data_final)
        elif muni == 'Niteroi':
            municipio = niteroi.Niteroi(pesquisa, data_inicial, data_final)
        elif muni == 'Nova Friburgo':
            municipio = nova_friburgo.NovaFriburgo(pesquisa, data_inicial, data_final)
        elif muni == 'Quatis':
            municipio = quatis.Quatis(pesquisa, data_inicial, data_final)
        elif muni == 'São Gonçalo':
            municipio = sao_goncalo.SaoGoncalo(pesquisa, data_inicial, data_final)
        elif muni == 'São João de Mereti':
            municipio = sao_joao_mereti.SaoJoaoMereti(pesquisa, data_inicial, data_final)
        elif muni == 'São José do Vale do Rio Preto':
            municipio = sao_jose_do_vale.SaoJose(pesquisa, data_inicial, data_final)
        elif muni == 'São Pedro da Aldeia':
            municipio = sao_pedro.SaoPedro(pesquisa, data_inicial, data_final)
        elif muni == 'Sapucaia':
            municipio = sapucaia.Sapucaia(pesquisa, data_inicial, data_final)
        elif muni == 'Varre-Sai':
            municipio = varre_sai.VarreSai(pesquisa, data_inicial, data_final)

        if municipio != '':
            diarios = municipio.retornaDiarios()
            for d in diarios:
                linha = {'Município': muni, 'Data': d[0], 'Link': d[1]}
                linha = pd.DataFrame([linha])
                tabela = pd.concat([tabela, linha], axis=0, ignore_index=True)

    if len(tabela) == 0:
        pyautogui.alert(text='Nenhum diário encontrado!', title='Resultado da pesquisa', button='OK')
    else:
        caminho = salvarcomo(defaultextension=".xlsx")
        tabela.to_excel(caminho)
        texto = 'Pesquisa salva! ' + str(len(tabela)) + ' diário(s) encontrado(s)!'
        pyautogui.alert(text=texto, title='Resultado da pesquisa', button='OK')
