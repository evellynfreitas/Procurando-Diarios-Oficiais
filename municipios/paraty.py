from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

continuar = True
data_inicial = "01/04/2023"
data_final = "04/07/2023"

data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

pesquisa = "tributos"

pagina = 1
lista_links = []
lista_datas = []
cont = 0

link = "https://www.paraty.rj.gov.br/multimidia/documentos"

site = webdriver.Chrome()
site.get(link)
site.implicitly_wait(5)

entrada = site.find_elements(By.TAG_NAME, 'input')[1]
time.sleep(3)
entrada.send_keys("tributos")
time.sleep(3)
entrada.send_keys(Keys.RETURN)
time.sleep(3)
site.switch_to.window(site.window_handles[0])
time.sleep(3)

pesquisador = BeautifulSoup(site.page_source, "html.parser")
ul = pesquisador.find('ul', class_='list-documents')
links = ul.find_all('a')

for a in links:
    header = a.find('header')
    span = header.find('span', class_='date ng-binding')
    data = datetime.strptime(span.text, '%d/%m/%Y').date()

    if data_final >= data >= data_inicial:
        lista_links.insert(cont, a['href'])
        lista_datas.insert(cont, span.text)
        cont = cont + 1
    else:
        continuar = False
        break

while continuar:
    botao = site.find_element(By.CLASS_NAME, 'bt-gray')
    time.sleep(3)
    botao.click()
    time.sleep(3)
    site.switch_to.window(site.window_handles[0])
    time.sleep(3)



site.quit()
