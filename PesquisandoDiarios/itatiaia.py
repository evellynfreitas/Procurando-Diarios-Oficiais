import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time


class Itaiaia:
    def __init__(self, pesquisa, data_inicial, data_final):

        data_inicial = data_inicial.split('/')
        self.data_inicial = data_inicial[2] + '.' + data_inicial[1] + '.' + data_inicial[0]

        data_final = data_final.split('/')
        self.data_final = data_final[2] + '.' + data_final[1] + '.' + data_final[0]

        self.pesquisa = pesquisa
        self.url = 'http://itatiaia.rj.gov.br/boletim-oficial/?jsf=jet-engine'
        self.url = f'{self.url}&date={self.data_inicial}-{self.data_final}'

    def retornaDiarios(self):

        diarios = []
        driver = webdriver.Chrome()
        driver.get(self.url)

        while True:
            xpath = '//*[@id="content"]/div/div[1]/section[2]/div/div/div/div[1]/div/div/div'
            div = driver.find_element(By.XPATH, xpath)
            links = div.find_elements(By.TAG_NAME, 'a')
            datas = div.find_elements(By.TAG_NAME, 'h6')

            for i in range(len(links)):
                data = datas[i].text
                link = links[i].get_attribute('href')
                if PdfReader.contemPalavra(link, self.pesquisa):
                    diarios.append([data, link])

            try:
                paginas = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/section[2]/div/div/div/div[2]'
                                                        '/div/div/div')
                paginas = paginas.find_elements(By.CLASS_NAME, 'jet-filters-pagination__link')

                cookies = driver.find_element(By.XPATH, '//*[@id="cn-accept-cookie"]')
                if cookies.is_displayed():
                    cookies.click()

                if paginas[-1].text == 'Próximo':
                    paginas[-1].click()
                    time.sleep(8)
                else:
                    break
            except selenium.common.exceptions.NoSuchElementException:
                break

        return diarios
