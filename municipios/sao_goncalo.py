from bs4 import BeautifulSoup
import requests

continuar = True
data_inicial = "2023-05-01"
data_final = "2023-06-30"
pesquisa = "poder+executivo"
# palavras são pesquisadas separadas por +
pagina = 1
lista_links = []
lista_datas = []
cont = 0

while continuar:

    link = "https://www.saogoncalo.rj.gov.br/diario-oficial/?dataInicial=" + data_inicial + "&dataFinal=" + data_final + "&termo=" + pesquisa + "&btnPesquisarPorTermo=1&pagina="+str(pagina)
    site = requests.get(link)
    site = BeautifulSoup(site.text, "html.parser")
    divs = site.find_all('div', class_='alert alert-secondary')

    if not divs:
        continuar = False
    else:
        for div in divs:
            a = div.find('a')
            lista_links.insert(cont, a['href'])
            lista_datas.insert(cont, a.text)
            # print(lista_datas[cont] + " | " + lista_links[cont])
            cont = cont + 1

    pagina = pagina + 1


i = 0
while i < cont:
    print(lista_datas[i] + " | " + lista_links[i])
    i = i + 1
