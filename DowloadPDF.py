import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


def scrape():

    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    response = requests.get(url)

    content = BeautifulSoup(response.text, 'html.parser')

    all_urls = content.find_all('a')

    for url_tag in all_urls:

        try:
            if 'pdf' in url_tag['href'] :

                if 'Anexo' in url_tag['href']:

                    print(url_tag['href'])

                    pdf_url = urljoin(url, url_tag['href'])

                    pdf_reponse = requests.get(pdf_url)

                    filename = pdf_url.split('/')[-1]

                    cwd = os.getcwd()

                    with open(os.path.join(cwd, filename), 'wb') as f:

                        f.write(pdf_reponse.content)


        except Exception as e:
            print('ERRO:', e)

if __name__ == "__main__":

    scrape()



    