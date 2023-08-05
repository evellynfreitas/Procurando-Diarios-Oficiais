from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Macae:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://sistemas.macae.rj.gov.br:840/diariooficial/'

    def retornaDiarios(self):

        diarios = []
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div[1]/div/button').click()
        # abre a aba de pesquisa
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="periodode"]').send_keys(self.data_inicial)
        driver.find_element(By.XPATH, '//*[@id="periodoate"]').send_keys(self.data_final)
        driver.find_element(By.XPATH, '//*[@id="filtro"]').send_keys(self.pesquisa)

        driver.find_element(By.XPATH, '//*[@id="modal-busca"]/div[3]/button[3]').click()  # aperta no botao de pesquisar
        time.sleep(2)
        continuar = True

        while continuar:
            div = driver.find_element(By.XPATH, '//*[@id="tb-result"]/tbody')

            for tr in div.find_elements(By.TAG_NAME, 'tr'):
                if str(tr.get_attribute('role')) != 'row':
                    break
                data = tr.find_elements(By.TAG_NAME, 'td')[2].get_attribute('innerHTML').split(' ')[0]
                link = tr.find_element(By.TAG_NAME, 'a').get_attribute('href')
                diarios.append([data, link])

            proximo = driver.find_element(By.XPATH, '//*[@id="tb-result_next"]')
            if 'disabled' in str(proximo.get_attribute('class')):
                continuar = False
            else:
                proximo.find_element(By.TAG_NAME, 'a').click()
                time.sleep(1)
        return diarios
