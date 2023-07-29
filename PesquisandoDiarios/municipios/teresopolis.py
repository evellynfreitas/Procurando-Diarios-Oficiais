from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService


continuar = True
data_inicial = "01/06/2023"
data_final = "01/07/2023"
pesquisa = "tributos"
# palavras são pesquisadas separadas por +
pagina = 1
lista_links = []
lista_datas = []
cont = 0

link = "https://atos.teresopolis.rj.gov.br/diario/#/diarios"

driver = webdriver.Chrome()
driver.get(link)
driver.implicitly_wait(4)

# input data inicial
#driver.find_element(by=By.NAME, value='dataInicial').send_keys(data_inicial)
# input data final
#print(driver.find_element(by=By.NAME, value='dataFinal').text)
# input pesquisa
#driver.find_element(by=By.NAME, value='texto').send_keys(pesquisa)
#driver.implicitly_wait(10)
#driver.save_screenshot('./image.png')

driver.quit()
# problemas em acessar os elementos ion
