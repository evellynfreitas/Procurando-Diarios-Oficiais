from bs4 import BeautifulSoup
import requests
import PdfReader
from datetime import datetime, timedelta


class NovaIguacu:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        self.data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
        self.pesquisa = pesquisa
        self.url = 'https://www.novaiguacu.rj.gov.br/diario-oficial/?data='

    def retornaDiarios(self):

        diarios = []
        data = self.data_inicial

        while self.data_inicial <= data <= self.data_final:
            data_formatada = data.strftime('%Y-%m-%d')
            url = 'https://www.novaiguacu.rj.gov.br/diario-oficial/?data=' + data_formatada

            site = requests.get(url)
            site = BeautifulSoup(site.text, "html.parser")
            div = site.find('div', class_='clearfix')

            if '<div class="thumbnail">' in str(div):  # possui um diario
                link = div.find('a')['href']
                if PdfReader.contemPalavra(link, self.pesquisa):
                    diarios.append([data.strftime('%d/%m/%Y'), link])

            data = data + timedelta(1)
        return diarios


obj = NovaIguacu('grade', '01/07/2023', '31/07/2023')
for d in obj.retornaDiarios():
    print(d)
