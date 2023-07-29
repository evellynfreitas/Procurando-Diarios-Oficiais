from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

link = "https://buzios.aexecutivo.com.br/jornal.php"
site = requests.get(link)
site = BeautifulSoup(site.text, "html.parser")
#print(site.prettify())

#datas = site.find_all("td", attrs={"data-tittle": "Publicação"})

#print(datas.__sizeof__())

h = site.find_all('h2')[0]
print(h.get_text())

