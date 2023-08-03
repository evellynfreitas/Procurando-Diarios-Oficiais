from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import selenium.common.exceptions
import PdfReader


class Queimados:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        self.data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
        self.pesquisa = pesquisa
        self.url = 'https://www.queimados.rj.gov.br/diario/portal?filter=true&data-publicacao='

    def retornaDiarios(self):

        diarios = []
        cont = 0

        driver = webdriver.Chrome()
        data = self.data_inicial

        while self.data_inicial <= data <= self.data_final:
            url = self.url + data.strftime('%d/%m/%Y')
            driver.get(url)
            time.sleep(1)
            try:
                a = driver.find_element(By.XPATH, '//*[@id="tabela-tipo"]/table/tbody/tr[1]/td[4]/a')
                link = a.get_attribute('href')
                if PdfReader.contemPalavra(link, self.pesquisa):
                    diarios.insert(cont, [data.strftime('%d/%m/%Y'), link])
                cont += 1
                data = (data + timedelta(1))
            except selenium.common.exceptions.NoSuchElementException:
                cont += 1
                data = (data + timedelta(1))

        driver.quit()
        return diarios
