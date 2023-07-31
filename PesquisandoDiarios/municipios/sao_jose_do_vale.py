import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By


class SaoJose:
    def __init__(self, pesquisa, data_inicial, data_final):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://sjvriopreto.rj.gov.br/diario-oficial'

    def retornaDiarios(self):

        driver = webdriver.Chrome()
        driver.get(self.url)

        diarios = []
        cont = 0

        input_data_inicial = driver.find_element(By.NAME, 'data_inicio')
        input_data_inicial.click()
        input_data_inicial.send_keys(self.data_inicial)

        input_data_final = driver.find_element(By.NAME, 'data_fim')
        input_data_final.click()
        input_data_final.send_keys(self.data_final)

        botao = driver.find_element(By.NAME, 'submit')
        botao.click()
        driver.implicitly_wait(3)

        div = driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/div')
        lista = div.find_elements(By.TAG_NAME, 'a')

        for a in lista:
            if a.get_attribute('class') == 'btn btn-primary btn-lg':
                link = a.get_attribute('href')
                if PdfReader.contemPalavra(link, self.pesquisa):
                    data = ''
                    for c in a.get_attribute('title'):
                        if c == '_':
                            data += '/'
                        elif c == '.':
                            data += '/2023'
                            break
                        else:
                            data += c

                    diarios.insert(cont, [data, link])
                    cont += 1

        driver.quit()
        return diarios
