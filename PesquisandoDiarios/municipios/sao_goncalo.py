from bs4 import BeautifulSoup
import requests


class SaoGoncalo:
    def __init__(self, pesquisa, data_inicial, data_final):

        data_inicial = data_inicial.split('/')
        self.data_inicial = data_inicial[2] + "-" + data_inicial[1] + '-' + data_inicial[0]

        data_final = data_final.split('/')
        self.data_final = data_final[2] + "-" + data_final[1] + '-' + data_final[0]

        self.pesquisa = ''
        pesquisa = pesquisa.split(' ')
        for palavra in pesquisa:
            self.pesquisa += (palavra + "+")

    def retornaDiarios(self):

        diarios = []
        continuar = True
        pagina = 1
        cont = 0

        while continuar:

            link = "https://www.saogoncalo.rj.gov.br/diario-oficial/?dataInicial=" + self.data_inicial + "&dataFinal="\
                   + self.data_final + "&termo=" + self.pesquisa + "&btnPesquisarPorTermo=1&pagina="+str(pagina)
            site = requests.get(link)
            site = BeautifulSoup(site.text, "html.parser")
            divs = site.find_all('div', class_='alert alert-secondary')

            if not divs:
                continuar = False
            else:
                for div in divs:
                    a = div.find('a')
                    data = a.text
                    link = a['href']
                    diarios.insert(cont, [data, link])
                    cont += 1
            pagina += 1
        return diarios
