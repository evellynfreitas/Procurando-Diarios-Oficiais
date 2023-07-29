from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService

continuar = True
data_inicial = "01/06/2023"
data_final = "01/07/2023"
data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
pesquisa = "notas"
# palavras são pesquisadas separadas por +
pagina = 1
lista_links = []
lista_datas = []
cont = 0

link = "http://rj.portaldatransparencia.com.br/prefeitura/cabofrio/"

driver = webdriver.Chrome()
driver.get(link)
driver.implicitly_wait(4)
data = data_inicial.strftime('%d/%m/%Y')


while continuar:
    input_data = driver.find_elements(by=By.TAG_NAME, value='input')[1]
    input_pesquisa = driver.find_elements(by=By.TAG_NAME, value='input')[3]
    print(data)
    input_data.click()
    input_data.clear()
    input_data.send_keys(data)
    input_data.click()
    input_data.clear()
    input_pesquisa.send_keys(pesquisa)

    botao = driver.find_elements(by=By.TAG_NAME, value='button')[3]
    botao.click()
    driver.implicitly_wait(4)

    div = driver.find_elements(by=By.TAG_NAME, value='div')[20].get_attribute('innerHTML')

    if "Nenhum registro localizado" in div:
        print('não tem')
    else:
        print('tem')

    data = datetime.strptime(data, '%d/%m/%Y').date()
    data = (data + timedelta(1)).strftime('%d/%m/%Y')

    #if datetime.strptime(data, '%d/%m/%Y').date() > data_final:


driver.quit()
# problemas em acessar os elementos ion
