from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

data_inicial = "01/06/2023"
data_final = "04/07/2023"

#data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
#data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

pesquisa = "tributos"

pagina = 1
lista_links = []
lista_datas = []
cont = 0

link = "https://www.diariomunicipal.com.br/aemerj/pesquisar"

driver = webdriver.Chrome()
driver.get(link)
driver.implicitly_wait(5)

select = Select(driver.find_element(By.NAME, 'busca_avancada[entidadeUsuaria]'))
select.select_by_value('425')

# texto da pesquisa
driver.find_element(by=By.NAME, value='busca_avancada[texto]').clear()
time.sleep(3)
driver.find_element(by=By.NAME, value='busca_avancada[texto]').send_keys(pesquisa)
time.sleep(3)

# data inicial
driver.find_element(by=By.NAME, value='busca_avancada[dataInicio]').clear()
driver.find_element(by=By.NAME, value='busca_avancada[dataInicio]').send_keys(data_inicial)
time.sleep(3)
#data final
driver.find_element(by=By.NAME, value='busca_avancada[dataFim]').clear()
driver.find_element(by=By.NAME, value='busca_avancada[dataFim]').send_keys(data_final)
time.sleep(3)

botao = driver.find_element(by=By.NAME, value='busca_avancada[Enviar]')
time.sleep(3)
botao.click()
driver.switch_to.window(driver.window_handles[0])
driver.save_screenshot('./image.png')


driver.quit()
