import datetime
import io
import requests
import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time

url = 'https://sistemas.macae.rj.gov.br:84/diariooficial/'

data_inicial = "01/07/2023"
data_final = "20/07/2023"
#data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
#data_final = datetime.strptime(data_final, '%d/%m/%Y').date()

driver = webdriver.Chrome()
driver.get(url)

#data = data_inicial.strftime('%d/%m/%Y')

driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div[1]/div/button').click()
driver.switch_to.window(driver.window_handles[0])

driver.find_elements(By.CLASS_NAME, 'input')
for i in driver.find_elements(By.CLASS_NAME, 'input'):
    print(i.get_attribute('id'))

driver.quit()