import requests
from bs4 import BeautifulSoup

requisicao = requests.get("https://g1.globo.com/")


soup = BeautifulSoup(requisicao.content, 'html.parser')
titulo = soup.find_all('body')
print(titulo.text)

# .status_code = retorna o codigo da solicitação
# .headers = retorna o cabeçalho
# .content = retorna o conteudo



# tipos de códigos de estado
# Informativo (1XX) /   Sucesso(2XX)    / Redirecionamento(3XX) /   Erro do cliente(4XX)    /   Erro do servidor(5XX)
# <Response [403]> ==> servidor está se recusando a atender a requisição por falta de permissão


# requestes e bs4 