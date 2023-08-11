from bs4 import BeautifulSoup
import requests


class Arraial:
    def __init__(self, pesquisa, data_inicial, data_final):
        if pesquisa == '' or pesquisa == ' ':
            self.pesquisa = '0'
        else:
            self.pesquisa = pesquisa

        self.data_inicial = data_inicial.replace('/', '-')
        self.data_final = data_final.replace('/', '-')

        self.url = "https://www.arraial.rj.gov.br/portal/diario-oficial/1"
        self.url = f"{self.url}/{self.data_inicial}/{self.data_final}/{self.pesquisa}/0/0/"

    def retornaDiarios(self):
        site = requests.get(self.url)
        site = BeautifulSoup(site.text, "html.parser")

        diarios = []

        divs = site.find_all('div', class_='dof_publicacao_diario sw_item_listagem')

        for div in divs:
            lista_a = div.find_all('a', href=True)
            span = div.find('span', class_='sw_descricao_info')

            for a in lista_a:
                data = span.find('span').text.split(' ')[0]
                link = "https://www.arraial.rj.gov.br" + a['href']

                diarios.append([data, link])
        return diarios
