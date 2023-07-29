from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

continuar = True
data_inicial = "05/06/2023"
data_final = "05/07/2023"
data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

pesquisa = "municipal"
lista_links = []
lista_datas = []
cont = 0

link = "http://rj.portaldatransparencia.com.br/prefeitura/comendadorlevygasparian/"

driver = webdriver.Chrome()
driver.get(link)
driver.implicitly_wait(4)
data = data_inicial.strftime('%d/%m/%Y')

while continuar:
    input_data = driver.find_elements(by=By.TAG_NAME, value='input')[1]
    input_pesquisa = driver.find_elements(by=By.TAG_NAME, value='input')[3]
    input_data.click()
    input_data.clear()
    input_data.send_keys(data)
    input_pesquisa.click()
    input_pesquisa.clear()
    input_pesquisa.send_keys(pesquisa)

    botao = driver.find_elements(by=By.TAG_NAME, value='button')[3]
    botao.click()
    driver.implicitly_wait(4)

    div = driver.find_elements(by=By.TAG_NAME, value='div')[20].get_attribute('innerHTML')

    if "Nenhum registro localizado" not in div:
        botao = driver.find_element(by=By.XPATH, value='//*[@id="conteudo"]/div/div[2]/div[3]/div/div/button[1]')
        codigo = botao.get_attribute("href")
        codigo = codigo.split('=')[2]
        link_pdf = "http://rj.portaldatransparencia.com.br/prefeitura/comendadorlevygasparian/?pagina=abreDocumento&arquivo=" + codigo
        lista_links.insert(cont, link_pdf)
        lista_datas.insert(cont, data)
        cont = cont + 1

    data = datetime.strptime(data, '%d/%m/%Y').date()
    data = (data + timedelta(1)).strftime('%d/%m/%Y')

    if datetime.strptime(data, '%d/%m/%Y').date() > data_final:
        continuar = False

driver.quit()

i = 0
while i < cont:
    print(lista_datas[i] + " | " + lista_links[i])
    i = i+1
