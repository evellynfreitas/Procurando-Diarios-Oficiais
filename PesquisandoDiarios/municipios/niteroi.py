import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

def retornaMes(num):
    if num == 1:
        return "Janeiro"
    if num == 2:
        return "Fevereiro"
    if num == 3:
        return "Março"
    if num == 4:
        return "Abril"
    if num == 5:
        return "Maio"
    if num == 6:
        return "Junho"
    if num == 7:
        return "Julho"
    if num == 8:
        return "Agosto"
    if num == 9:
        return "Setembro"
    if num == 10:
        return "Outubro"
    if num == 11:
        return "Novembro"
    if num == 12:
        return "Dezembro"


url = 'http://www.niteroi.rj.gov.br/do.html'
driver = webdriver.Chrome()
driver.get(url)
pesquisa = 'lazer'

data_inicial = "01/07/2023"
data_final = "05/07/2023"
data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

data = data_inicial

cont = 0
lista_pdfs = []

while data_inicial <= data <= data_final:
    ano = str(data.year)
    mes = retornaMes(data.month)
    dia = datetime.strftime(data, '%d')

    input_ano = driver.find_element(By.NAME, 'Ano')
    Select(input_ano).select_by_visible_text(ano)

    input_mes = driver.find_element(By.NAME, 'Mes')
    Select(input_mes).select_by_visible_text(mes)

    input_dia = driver.find_element(By.NAME, 'Dia')
    Select(input_dia).select_by_visible_text(dia)

    botao = driver.find_element(By.TAG_NAME, 'Button')
    botao.click()

    driver.switch_to.window(driver.window_handles[1])
    resultado = PdfReader.contemPalavra(driver.current_url, pesquisa)

    if resultado:
        lista_pdfs.insert(cont, driver.current_url)
        cont += 1

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    data = (data + timedelta(1))

for i in range(0, cont, 1):
    print(lista_pdfs[i])
