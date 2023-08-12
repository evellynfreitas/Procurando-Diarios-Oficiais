from bs4 import BeautifulSoup
import requests


class NovaFriburgo:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://plenussistemas.dioenet.com.br/list/nova-friburgo?secao='
        self.url = f"{self.url}&d={self.data_inicial}+a+{self.data_final}&pesquisa={self.pesquisa}&pagina="

    def retornaDiarios(self):

        diarios = []
        paginas = 1

        while True:
            url = self.url+str(paginas)
            site = requests.get(url)
            site = BeautifulSoup(site.text, "html.parser")
            lista = site.find_all('a', class_='btn btn-default btn-sm')

            if len(lista) == 0:
                break

            for a in lista:
                link = a['href']
                data = a['title'].split(' ')[2]
                diarios.append([data, link])

            paginas += 1

        return diarios
