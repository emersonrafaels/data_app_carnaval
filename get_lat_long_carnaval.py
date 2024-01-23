from pathlib import Path
import json

import pandas as pd

from src.utils.api import main_api_geopy

dir_root = Path(__file__).parent

def save_dict_to_json(dict, name_save):

	# SALVANDO O DICIONÁRIO EM FORMATO JSON
	with open(name_save, 'w', encoding='latin') as arquivo_json:
		json.dump(dict, arquivo_json)

	print(f'O dicionário foi salvo em {name_save}')

def load_data(dir_data):

	df = pd.read_excel(dir_data)

	return df

def get_lat_long(dataframe, column_address):

	dict_result = main_api_geopy.get_lat_long_dataframe_locations(dataframe=dataframe,
																  column_address=column_address)

	# SALVANDO O RESULTADO
	save_dict_to_json(dict_result,
					  name_save="RESULTADO_LOCATION.json")

def orchestra_get_lat_long():

	# DEFININDO A BASE A SER LIDA
	dir_data = str(Path(dir_root, "data/CARNAVAL DE PAULIXTA.xlsx"))
	column_address = "ENDEREÇO"

	# LENDO A BASE
	df = load_data(dir_data=dir_data)

	# OBTENDO AS LATITUDES E LONGITUDES
	get_lat_long(dataframe=df, column_address=column_address)

if __name__ == '__main__':
	orchestra_get_lat_long()