from datetime import datetime, timedelta
from selenium.webdriver.common.by import By


class Areal:
    def __init__(self, pesquisa, data_inicial, data_final, driver):
        self.data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        self.data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
        self.pesquisa = pesquisa
        self.url = 'http://rj.portaldatransparencia.com.br/prefeitura/areal/'
        self.driver = driver

    def retornaDiarios(self):

        driver = self.driver
        driver.get(self.url)

        diarios = []
        data = self.data_inicial

        while data <= self.data_final:
            input_data = driver.find_elements(by=By.TAG_NAME, value='input')[1]
            input_data.click()
            input_data.clear()
            input_data.send_keys(data.strftime('%d/%m/%Y'))

            input_pesquisa = driver.find_elements(by=By.TAG_NAME, value='input')[3]
            input_pesquisa.click()
            input_pesquisa.clear()
            input_pesquisa.send_keys(self.pesquisa)

            botao = driver.find_elements(by=By.TAG_NAME, value='button')[3]
            botao.click()
            edicoes = driver.find_elements(by=By.CLASS_NAME, value='edicoes')

            for div in edicoes:
                link = div.find_element(By.TAG_NAME, 'a')
                link = link.get_attribute('href')
                diarios.append([data.strftime('%d/%m/%Y'), link])

            data = (data + timedelta(1))

        return diarios
