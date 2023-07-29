import io
import requests
import PyPDF2


def contemPalavra(link, palavra):
    try:
        r = requests.get(link)
        f = io.BytesIO(r.content)
        reader = PyPDF2.PdfReader(f)
        paginas = reader.pages
        for pagina in paginas:
            texto = pagina.extract_text()
            if palavra.lower() in texto.lower():
                return True

        return False
    except PyPDF2.errors.PdfReadError:
        return False


class PdfReader:
    def PdfReader(self):
        pass
