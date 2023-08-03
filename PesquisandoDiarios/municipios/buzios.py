buzios.py
from bs4 import BeautifulSoup
import requests
import PdfReader


class Buzios:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://buzios.aexecutivo.com.br/jornal.php?Num=&Sec=&dtini=' + data_inicial + \
                   '&dtfim=' + data_final + '&pagina='

    def retornaDiarios(self):
        diarios = []
        cont = 0
        paginas = 0

        while True:
            site = requests.get(self.url+str(paginas))
            site = BeautifulSoup(site.text, "html.parser")
            lista_a = site.find_all('a', class_='btn btn-primary btn-sm')
            if len(lista_a) == 0:
                break
            for a in lista_a:
                url = 'https://buzios.aexecutivo.com.br/' + a['href']
                site = requests.get(url)
                site = BeautifulSoup(site.text, "html.parser")

                codigo = site.find('a', class_='btn btn-primary btn-sm pull-right')['href']
                link = 'https://buzios.aexecutivo.com.br/' + codigo.replace(' ', '%20')
                data = str(site.find('strong')).split(' ')[3]

                if PdfReader.contemPalavra(link, self.pesquisa):
                    diarios.insert(cont, [data, link])
                    cont += 1

            paginas += 1
        return diarios
