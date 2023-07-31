import datetime
import io
import requests
import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

url = 'http://www.conceicaodemacabu.rj.gov.br/pagina/14852/Di%C3%A1rios%20de%202023'

data_inicial = "05/06/2023"
data_final = "05/07/2023"
data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

driver = webdriver.Chrome()
driver.get(url)

data = data_inicial.strftime('%d/%m/%Y')

input_busca = driver.find_element(By.XPATH, '//*[@id="STR_BSC_CAD_GEN_1981"]')
input_busca.click()
input_busca.clear()
input_busca.send_keys(data)
input_busca.send_keys(Keys.ENTER)

span = driver.find_element(By.XPATH, '//*[@id="nome_arquivo_registro_generico"]')

print(span.get_attribute('innerHTML'))
