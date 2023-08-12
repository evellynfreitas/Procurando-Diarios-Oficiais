from selenium.webdriver.common.by import By
import PdfReader


class SaoJose:
    def __init__(self, pesquisa, data_inicial, data_final, driver):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pesquisa = pesquisa
        self.url = 'https://sjvriopreto.rj.gov.br/diario-oficial'
        self.driver = driver

    def retornaDiarios(self):

        driver = self.driver
        driver.get(self.url)

        diarios = []

        input_data_inicial = driver.find_element(By.NAME, 'data_inicio')
        input_data_inicial.click()
        input_data_inicial.send_keys(self.data_inicial)

        input_data_final = driver.find_element(By.NAME, 'data_fim')
        input_data_final.click()
        input_data_final.send_keys(self.data_final)

        botao = driver.find_element(By.NAME, 'submit')
        botao.click()

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

                    diarios.append([data, link])

        return diarios
