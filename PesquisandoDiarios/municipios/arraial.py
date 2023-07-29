from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

data_inicial = "20-06-2023"
data_final = "30-06-2023"
pesquisa = "Praia"
link = "https://www.arraial.rj.gov.br/portal/diario-oficial/1/" + data_inicial + "/" + data_final + "/" + pesquisa + "/0/0/"
site = requests.get(link)
site = BeautifulSoup(site.text, "html.parser")

divs = site.find_all('div', class_='dof_publicacao_diario sw_item_listagem')

lista_links = []
lista_datas = []
cont = 0

for div in divs:
    lista_a = div.find_all('a', href=True)
    span = div.find('span', class_='sw_descricao_info')

    for a in lista_a:
        lista_datas.insert(cont, span.find('span').text)
        #print(a['href'])
        href = "https://www.arraial.rj.gov.br" + a['href']
        lista_links.insert(cont, href)

        print(lista_datas[cont] + " | " + lista_links[cont])
        cont = cont+1

