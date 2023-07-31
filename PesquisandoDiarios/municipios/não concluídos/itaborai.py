import datetime
import io
import requests
import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time

url = 'https://portal.ib.itaborai.rj.gov.br/diario-oficial/'

data_inicial = "05/06/2023"
data_final = "05/07/2023"
#data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
#data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

driver = webdriver.Chrome()
driver.get(url)

#data = data_inicial.strftime('%d/%m/%Y')

driver.find_element(By.XPATH, '//*[@id="forma"]').click()
time.sleep(2)
#driver.find_element(By.XPATH, '//*[@id="dateinicio"]').send_keys(data_inicial)
#driver.find_element(By.XPATH, '//*[@id="datefim"]').send_keys(data_final)

#div = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]')

#print(div.get_attribute('innerHTML'))
