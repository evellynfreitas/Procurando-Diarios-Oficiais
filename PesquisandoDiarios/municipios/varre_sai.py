import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://varresai.rj.gov.br/site/diarios_oficiais'
driver = webdriver.Chrome()
driver.get(url)
pesquisa = 'EXECUTIVO'

data_inicial = "01/07/2023"
data_final = "10/07/2023"

cont = 0
lista_pdfs = []
driver.implicitly_wait(5)

input_data_inicial = driver.find_element(By.XPATH, '//*[@id="data_pub"]')
input_data_inicial.click()
input_data_inicial.send_keys(data_inicial)

input_data_final = driver.find_element(By.XPATH, '//*[@id="data_pub_2"]')
input_data_final.click()
input_data_final.send_keys(data_final)

botao = driver.find_element(By.XPATH, '//*[@id="bt_lic_filtro"]')
botao.click()

div = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div[1]/div')
lista = div.find_elements(By.TAG_NAME, 'a')

for a in lista:
    try:
        if 'btn btn-default' == str(a.get_attribute('class')):
            if PdfReader.contemPalavra(a.get_attribute('href'), pesquisa):
                lista_pdfs.insert(cont, a.get_attribute('href'))
                cont += 1
    except:
        continue

driver.quit()

for link in lista_pdfs:
    print(link)
