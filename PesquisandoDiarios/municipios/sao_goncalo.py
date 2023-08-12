from bs4 import BeautifulSoup
import requests


class SaoGoncalo:
    def __init__(self, pesquisa, data_inicial, data_final):

        data_inicial = data_inicial.split('/')
        self.data_inicial = data_inicial[2] + "-" + data_inicial[1] + '-' + data_inicial[0]

        data_final = data_final.split('/')
        self.data_final = data_final[2] + "-" + data_final[1] + '-' + data_final[0]

        self.pesquisa = pesquisa.replace(' ', '+')
        self.url = "https://www.saogoncalo.rj.gov.br/diario-oficial/?"
        self.url = f"{self.url}dataInicial={self.data_inicial}&dataFinal={self.data_final}&termo={self.pesquisa}"

    def retornaDiarios(self):

        diarios = []
        continuar = True
        pagina = 1

        while continuar:
            link = f"{self.url}&btnPesquisarPorTermo=1&pagina={str(pagina)}"
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
                    diarios.append([data, link])
            pagina += 1
        return diarios
