from selenium.webdriver.common.by import By
from datetime import datetime
import PdfReader
import time


class VoltaRedonda:
    def __init__(self, pesquisa, data_inicial, data_final, driver):
        self.pesquisa = pesquisa
        self.data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        self.data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
        self.url = 'https://www.voltaredonda.rj.gov.br/vrdestaque/index.php'
        self.driver = driver

    def retornaDiarios(self):

        diarios = []

        driver = self.driver
        driver.get(self.url)

        time.sleep(2)
        select_input = driver.find_element(By.XPATH, '//*[@id="search"]')

        for opcao in select_input.find_elements(By.TAG_NAME, 'option'):

            link = 'https://www.voltaredonda.rj.gov.br' + opcao.get_attribute('value')
            data = str(opcao.get_attribute('value')[36:46])

            if data == '2019-14-06':
                data = '2019-06-14'
            elif data == '1604_-_21_':
                data = '2020-05-20'
            elif data == '1530_-_11_':
                data = '2019-07-11'
            elif data == '':
                continue

            data = datetime.strptime(data, "%Y-%m-%d").date()
            if self.data_inicial <= data <= self.data_final:
                if PdfReader.contemPalavra(link, self.pesquisa):
                    diarios.append([data.strftime('%d/%m/%Y'), link])

        return diarios
