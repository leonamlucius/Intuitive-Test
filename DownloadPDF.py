import requests
from requests.auth import HTTPBasicAuth # Lib não built-in no python. Download: pip install requests
from bs4 import BeautifulSoup # Lib não built-in no python.  Download: pip install beautifulsoup4
import os
from urllib.parse import urljoin
import zipfile
import pathlib 

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
            print('ERROR:', e)

    directory = pathlib.Path(os.getcwd())


    with zipfile.ZipFile('anexos.zip', 'w') as my_zip:

        for file_path in directory.iterdir():
            
            if file_path.name == "DownloadPDF.py" or file_path.name == ".git" or file_path.name == "anexos.zip":
                pass
            else:
                print(file_path.name)
                my_zip.write(file_path, arcname= file_path.name)
                

if __name__ == "__main__":

    try: 
        scrape()
    except Exception as e:
        print('Scaping ERROR:', e)



    