import requests

requisicao = requests.get("https://azmina.com.br/penhas-saiba-mais/")

print(requisicao)

# .status_code = retorna o codigo da solicitação
# .headers = retorna o cabeçalho
# .headers = retorna o conteudo



# tipos de códigos de estado
# Informativo (1XX) /   Sucesso(2XX)    / Redirecionamento(3XX) /   Erro do cliente(4XX)    /   Erro do servidor(5XX)
# <Response [403]> ==> servidor está se recusando a atender a requisição por falta de permissão


# requestes e bs4 