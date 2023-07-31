import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class VarreSai:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.pesquisa = pesquisa
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.url = 'https://varresai.rj.gov.br/site/diarios_oficiais'

    def retornaDiarios(self):

        diarios = []
        cont = 0

        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(2)

        input_data_inicial = driver.find_element(By.XPATH, '//*[@id="data_pub"]')
        input_data_inicial.click()
        input_data_inicial.send_keys(self.data_inicial)

        input_data_final = driver.find_element(By.XPATH, '//*[@id="data_pub_2"]')
        input_data_final.click()
        input_data_final.send_keys(self.data_final)

        botao = driver.find_element(By.XPATH, '//*[@id="bt_lic_filtro"]')
        botao.click()

        div = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div[1]/div')
        lista = div.find_elements(By.TAG_NAME, 'a')
        h3 = div.find_elements(By.TAG_NAME, 'h3')

        indiceh3 = len(h3)

        for a in lista:

            try:
                if 'btn btn-default' == str(a.get_attribute('class')):
                    indiceh3 -= 1
                    link = a.get_attribute('href')
                    if PdfReader.contemPalavra(link, self.pesquisa):
                        data = h3[indiceh3].get_attribute('innerText').split()[4]
                        diarios.insert(cont, [data, link])
                        cont += 1
            except:
                continue

        driver.quit()
        return diarios
