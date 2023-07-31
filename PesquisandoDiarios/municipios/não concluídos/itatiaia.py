from bs4 import BeautifulSoup
import requests
import io
import requests
import PyPDF2


def verificaPdf(link, pesquisa):
    r = requests.get(link)
    f = io.BytesIO(r.content)

    reader = PyPDF2.PdfReader(f)
    paginas = reader.pages

    for pagina in paginas:
        p = pagina.extract_text()

        if pesquisa.lower() in p.lower():
            return True

    return False


data_inicial = "2023.01.01"
data_final = "2023.07.21"
pes = "SINE DIE"

url = "https://itatiaia.rj.gov.br/boletim-oficial/?jsf=jet-engine&date=" + data_inicial + "-" + data_final
site = requests.get(url)
site = BeautifulSoup(site.text, "html.parser")

print(url)
div = site.find('div', class_='jet-listing-grid jet-listing')
links = div.find_all('a')

aux = site.find('div', class_='class="jet-smart-filters-pagination jet-filter"')

print(aux)

if 'class="jet-filters-pagination__link"' in site:
    print('tem mais pagina')

#for a in links:
    #if verificaPdf(a['href'], pes):
        #print(a['href'])
