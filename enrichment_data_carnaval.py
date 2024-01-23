import json
import chardet
from pathlib import Path

import pandas as pd

from get_lat_long_carnaval import load_data

dir_root = Path(__file__).parent

def load_json_with_encoding(filename):

    # DETECTAR A CODIFICAÇÃO DO ARQUIVO
    with open(filename, 'rb') as file_bin:
        result_read = chardet.detect(file_bin.read())
        detected_encoding = result_read['encoding']

    # CARREGAR O ARQUIVO USANDO A CODIFICAÇÃO DETECTADA
    with open(filename, 'r',
			  encoding=detected_encoding) as file:
        json_data = json.load(file)

    return json_data

def merge_data(dataframe,
               dict_lat_long,
               column_address,
               name_new_column):

    # REALIZANDO O MERGE USANDO O MÉTODO MAP
    dataframe[name_new_column] = dataframe[column_address].map(dict_lat_long)

    # ABRINDO O RESULTADO EM COLUNAS BASEADAS NA KEY DO DICT


    return dataframe

def orchestra_enrichment_data():

    # DEFININDO O ARQUIVO JSON A SER LIDO
    nome_arquivo = str(Path(dir_root,
                            'data/RESULTADO_LOCATION.json'))

    # REALIZANDO A LEITURA DO ARQUIVO JSON
    dados = load_json_with_encoding(nome_arquivo)

    # DEFININDO A BASE A SER LIDA
    dir_data = str(Path(dir_root,
                        "data/CARNAVAL DE PAULIXTA.xlsx"))
    column_address = "ENDEREÇO"

    # LENDO A BASE
    df = load_data(dir_data=dir_data)

    # REALIZANDO O MERGE DOS DADOS
    df_lag_long = merge_data(dataframe=df,
                             dict_lat_long=dados,
                             column_address=column_address,
                             name_new_column="LATITUDE/LONGITUDE")

    print(df_lag_long)

if __name__ == '__main__':
	orchestra_enrichment_data()



