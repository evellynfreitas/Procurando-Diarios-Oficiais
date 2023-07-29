from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService

continuar = True
data_inicial = "01/06/2023"
data_final = "04/07/2023"
pesquisa = "kpop"

pagina = 1
lista_links = []
lista_datas = []
cont = 0

link = "http://rj.portaldatransparencia.com.br/prefeitura/areal/index.cfm"

site = webdriver.Chrome()
site.get(link)
time.sleep(3)
entrada = site.find_element(by=By.ID, value='busca')
site.execute_script("arguments[0].value = '" + pesquisa + "'", entrada)
button = site.find_element(by=By.CSS_SELECTOR, value='btn_buscar')
button.click()

