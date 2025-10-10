import http.client, json, pandas as pd


def obter_endereco(cep):
    conexao = http.client.HTTPSConnection("viacep.com.br")

    conexao.request("GET", f'/ws/{cep}/json/')

    resposta = conexao.getresponse()

    if resposta .status != 200:
        conexao.close()

        return None

    dados = resposta.read()

    endereco = json.loads(dados.decode('utf-8'))

    conexao.close()

    return endereco if "erro" not in endereco else None


def salvar_endereco(endereco, nome_arquivo="endereco.xlsx"):
    if "erro" not in endereco:
        df = pd.DataFrame([endereco])

        df.to_excel(nome_arquivo, index=False)

        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}")

    else:
        print(f"Não foi possível salvar os dados")


if __name__ == "__main__":
    planilha = 'CEP.xlsx'

    planilha_ceps = pd.read_excel(planilha, sheet_name='CEP')

    ceps = planilha_ceps['CEP'].dropna()

    resultados = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF'])

    for cep in ceps:
        endereco = obter_endereco(str(cep).replace('-', ''))

        if endereco:
            nova_linha = pd.DataFrame([{
                'CEP': cep, 
                'Logradouro': endereco.get('logradouro', ''), 
                'Bairro': endereco.get('bairro', ''), 
                'Localidade': endereco.get('localidade', ''), 
                'UF': endereco.get('uf', '')
            }])

            # ignore_index=True faz com que os indices sejam renumerados de forma contínua, evitando duplicidade ou lacunas
            resultados = pd.concat([resultados, nova_linha], ignore_index=True)

    # if_sheet_exists='replace' ==> instruir à substituir a aba, caso exista, evitando duplicidade
    with pd.ExcelWriter(planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # index=False impede que os indices do df sejam salvos no excel
        resultados.to_excel(writer, sheet_name='Dados', index=False)