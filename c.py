import requests, re

header_request = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    'Accept':  "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'Accept-Enconding': "gzip, deflate, br, zstd",
    'Accept-Language': "pt-PT,pt;q=0.9",
    'Connection': "keep-alive",
    }

requisicao = requests.get("https://esaj.tjsp.jus.br/cpopg/open.do", headers=header_request)

cookies = requisicao.headers['Set-Cookie']
# ERRO NA CHAVE COOKIES - ALTERAR COM REGEX PARA PEGAR O PADRÃO ADEQUADO PARA O HEDER DO .GET()
# import re (expressão regulares) - \w[letra\caractere], \s[espaço], \d[digito], .[qualquer coisa]
# 'JSESSIONID=F5164CDD83BC7ABEE0E20A553A12B83D.cpopg532; Path=/cpopg, K-JSESSIONID-knbbofpc=40AEADD550C0E6DBE3855A88F45F61EC; path=/cpopg'
#                                                        ^^^^^^^^^^  	                                                  ^^^^^^^^^^
#                                                           ERROR                                                           ERROR
# r(?P<cookie1>.*?)\spath=/cpopg, (?P<cookie2>.*?)\spath=/cpopg
# ^ INFORMA QUE É UM REGEX (r)      ^ IDENTIFICA PARA O PYTHON QUE É UM GRUPO (P)

exp_reg_cookie = re.search(r'(?P<cookie1>.*?)\spath=/cpopg,\s(?P<cookie2>.*?)\spath=/cpopg', cookies, flags=re.DOTALL|re.IGNORECASE)
novo_cookie = exp_reg_cookie.group("cookie1") + exp_reg_cookie.group("cookie2")
header_request['Cookies'] = novo_cookie
#print(header_request['Cookies'])



header_request.update(
    {
    'Host': "esaj.tjsp.jus.br", 
    "Referer": "https://esaj.tjsp.jus.br/cpopg/open.do"
    }
)

header_request.update(
    {
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"', 
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": '1',
    }
)

o_cookie = exp_reg_cookie.group("cookie1")
novo_cookie = ""
for i in range(len(o_cookie)):
    if(i < 10):
        novo_cookie += o_cookie[i].lower()
    else:
        novo_cookie += o_cookie[i]

print(requisicao)
url = f"https://esaj.tjsp.jus.br/cpopg/search.do;{novo_cookie}?conversationId=&cbPesquisa=NMPARTE&dadosConsulta.valorConsulta=Gabriel+Toledo&cdForo=-1"
requisicao = requests.get(url=url, headers=header_request)

print(requisicao.content.decode('UTF-8'))
