from bs4 import BeautifulSoup
import requests


class Arraial:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.pesquisa = pesquisa

        data_nova = ''
        for i in list(data_inicial):
            if i == '/':
                i = '-'
            data_nova += i
        self.data_inicial = data_nova

        data_nova = ''
        for i in list(data_final):
            if i == '/':
                i = '-'
            data_nova += i
        self.data_final = data_nova

    def retornaDiarios(self):
        link = "https://www.arraial.rj.gov.br/portal/diario-oficial/1/"
        link += self.data_inicial + "/" + self.data_final + "/" + self.pesquisa + "/0/0/"
        site = requests.get(link)
        site = BeautifulSoup(site.text, "html.parser")

        diarios = []
        cont = 0

        divs = site.find_all('div', class_='dof_publicacao_diario sw_item_listagem')
        for div in divs:
            lista_a = div.find_all('a', href=True)
            span = div.find('span', class_='sw_descricao_info')

            for a in lista_a:
                data = span.find('span').text.split(' ')[0]
                href = "https://www.arraial.rj.gov.br" + a['href']

                diarios.insert(cont, [data, href])
                cont += 1
        return diarios
