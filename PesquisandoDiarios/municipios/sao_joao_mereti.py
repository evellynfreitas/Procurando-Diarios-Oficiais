from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import PdfReader
import time


class SaoJoaoMereti:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        self.data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
        self.pesquisa = pesquisa
        self.url = 'https://transparencia.meriti.rj.gov.br/diario_oficial_busca.php'

    def retornaDiarios(self):

        diarios = []
        cont = 0

        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(3)

        data = self.data_inicial

        while data <= self.data_final:
            input_data = driver.find_element(By.XPATH, '//*[@id="pesquisaTexto"]')
            input_data.click()
            input_data.clear()
            input_data.send_keys(data.strftime('%d/%m/%Y'))

            botao = driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div/button[1]')
            botao.click()
            time.sleep(3)

            try:
                a = driver.find_element(By.XPATH, '//*[@id="secP"]/li/div[2]/a')
                link = a.get_attribute('href')
                if PdfReader.contemPalavra(link, self.pesquisa):
                    diarios.insert(cont, [data.strftime('%d/%m/%Y'), link])
                    cont += 1
            except:
                pass

            data = (data + timedelta(1))

        driver.quit()
        return diarios
