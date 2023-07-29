import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://sjvriopreto.rj.gov.br/diario-oficial'
driver = webdriver.Chrome()
driver.get(url)
pesquisa = 'gabriela'

data_inicial = "01/07/2023"
data_final = "20/07/2023"

cont = 0
lista_pdfs = []

input_data_inicial = driver.find_element(By.NAME, 'data_inicio')
input_data_inicial.click()
input_data_inicial.send_keys(data_inicial)

input_data_final = driver.find_element(By.NAME, 'data_fim')
input_data_final.click()
input_data_final.send_keys(data_final)

botao = driver.find_element(By.NAME, 'submit')
botao.click()
driver.implicitly_wait(3)

div = driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/div')
lista = div.find_elements(By.TAG_NAME, 'a')

for li in lista:
    if li.get_attribute('class') == 'btn btn-primary btn-lg':
        if PdfReader.contemPalavra(li.get_attribute('href'), pesquisa):
            lista_pdfs.insert(cont, li.get_attribute('href'))
            cont += 1

driver.quit()

for p in lista_pdfs:
    print(p)
