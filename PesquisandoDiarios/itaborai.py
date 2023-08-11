from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import PdfReader


class Itaborai:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://portal.ib.itaborai.rj.gov.br/diario-oficial/'

    def retornaDiarios(self):

        diarios = []
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(3)

        driver.find_elements(By.XPATH, '//*[@id="forma"]')[1].click()  # abrir a pesquisa por período
        driver.find_element(By.XPATH, '//*[@id="dateinicio"]').send_keys(self.data_inicial)  # enviar data inicial
        driver.find_element(By.XPATH, '//*[@id="datefim"]').send_keys(self.data_final)  # enviar data final
        driver.find_element(By.XPATH, '//*[@id="buscar"]').click()  # clicar no botão

        div = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]')
        lista = div.find_elements(By.ID, 'info')

        for div in lista:
            link = div.get_attribute('outerHTML').split("'")[1]
            data = div.get_attribute('textContent').split(' ')[6]
            if PdfReader.contemPalavra(link, self.pesquisa):
                diarios.append([data, link])

        driver.quit()
        return diarios
