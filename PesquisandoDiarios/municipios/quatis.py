from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import PdfReader

url = 'https://transparencia.quatis.rj.gov.br/diario_oficial_busca.php'
pesquisa = 'quatis'
link_pdfs = []
cont = 0

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(2)

data_inicial = "01/07/2023"
data_final = "24/07/2023"
data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

data = data_inicial

while data <= data_final:
    input_data = driver.find_element(By.XPATH, '//*[@id="pesquisaTexto"]')
    input_data.click()
    input_data.clear()
    input_data.send_keys(data.strftime('%d/%m/%Y'))

    botao = driver.find_element(By.XPATH, '//*[@id="pesquisaBtn"]')
    botao.click()
    data = (data + timedelta(1))

    try:
        a = driver.find_element(By.XPATH, '//*[@id="secP"]/li/p/a')
        link = a.get_attribute('href')
        if PdfReader.contemPalavra(link, pesquisa):
            link_pdfs.insert(cont, link)
            cont += 1
    except:
        pass

driver.quit()

for a in link_pdfs:
    print(a)
