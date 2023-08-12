import PdfReader
from selenium.webdriver.common.by import By
from selenium import common
import time


class VarreSai:
    def __init__(self, pesquisa, data_inicial, data_final, driver):
        self.pesquisa = pesquisa
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.url = 'https://varresai.rj.gov.br/site/diarios_oficiais'
        self.driver = driver

    def retornaDiarios(self):

        diarios = []

        driver = self.driver
        driver.get(self.url)
        time.sleep(3)

        input_data_inicial = driver.find_element(By.XPATH, '//*[@id="data_pub"]')
        input_data_inicial.click()
        input_data_inicial.send_keys(self.data_inicial)

        input_data_final = driver.find_element(By.XPATH, '//*[@id="data_pub_2"]')
        input_data_final.click()
        input_data_final.send_keys(self.data_final)

        botao = driver.find_element(By.XPATH, '//*[@id="bt_lic_filtro"]')
        botao.click()

        try:
            body = driver.find_element(By.TAG_NAME, 'body')
            body.find_element(By.XPATH, '/html/body/div[6]')
        except common.exceptions.NoSuchElementException:
            div = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div[1]/div')
            lista = div.find_elements(By.TAG_NAME, 'a')
            h3 = div.find_elements(By.TAG_NAME, 'h3')

            indiceh3 = len(h3)

            for a in lista:
                if 'btn btn-default' == str(a.get_attribute('class')):
                    indiceh3 -= 1
                    link = a.get_attribute('href')
                    if PdfReader.contemPalavra(link, self.pesquisa):
                        data = h3[indiceh3].get_attribute('innerText').split()[4]
                        diarios.append([data, link])

        return diarios
