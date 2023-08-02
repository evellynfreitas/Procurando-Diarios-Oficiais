from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import PdfReader


class Buzios:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://buzios.aexecutivo.com.br/jornal.php#'

    def retornaDiarios(self):

        diarios = []
        cont = 0

        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(2)

        input_data_inicial = driver.find_element(By.XPATH, '//*[@id="dtini"]')
        input_data_inicial.send_keys(self.data_inicial)
        input_data_final = driver.find_element(By.XPATH, '//*[@id="dtfim"]')
        input_data_final.send_keys(self.data_final)

        botao = driver.find_element(By.XPATH, '//*[@id="ancora"]/section[3]/div/div/div[2]/form/div[3]/div[1]/button')
        botao.click()

        div = driver.find_element(By.XPATH, '//*[@id="blog"]/div/div/div[2]')

        lista_links = []

        for a in div.find_elements(By.TAG_NAME, 'a'):
            lista_links.insert(cont, a.get_attribute('href'))
            cont += 1

        cont = 0

        for link in lista_links:
            driver.get(link)
            link = driver.find_element(By.XPATH, '//*[@id="ancora"]/section[2]/div/div/div[2]/a')
            link = link.get_attribute('href')

            if PdfReader.contemPalavra(link, self.pesquisa):
                data = driver.find_element(By.XPATH, '//*[@id="ancora"]/section[2]/div/div/div[2]/strong')
                data = data.get_attribute('innerText').split(' ')[3]
                diarios.insert(cont, [data, link])
                cont += 1
        driver.quit()
        return diarios
