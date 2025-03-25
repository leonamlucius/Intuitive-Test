import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


def scrape():

    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    response = requests.get(url)

    content = BeautifulSoup(response.text, 'html.parser')

    all_urls = content.findAll('a')

    for url in all_urls:

        try:
            if 'pdf' in url['href'] :

                if 'Anexo' in url['href']:
                    
                    print(url['href'])
        except:
            pass






if __name__ == "__main__":

    scrape()



    