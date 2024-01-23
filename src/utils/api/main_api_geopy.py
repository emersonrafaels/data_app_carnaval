from src.utils.api import api_geocoder

def get_lat_long_unique_location(location):

	geopy = api_geocoder.API_GEOCODER()

	dict_result_locations = geopy.get_information_using_address(locations=location)

	return dict_result_locations

def get_lat_long_dataframe_locations(dataframe, column_address):

	# INICIANDO A LISTA DE ENDEREÇOS
	locations = []

	# INSTANCIANDO A CLASSE DO GEOPY
	geopy = api_geocoder.API_GEOCODER()

	# INICIANDO O DICT DE RESULT
	dict_result_locations = {}

	# VERIFICANDO SE A COLUNA CONSTA NO DATAFRAME
	if column_address in dataframe.columns:
		# REMOVENDO ENDEREÇOS DUPLICADOS
		dataframe = dataframe.drop_duplicates(subset=column_address)

	# PERCORRENDO O DATAFRAME E OBTENDO OS ENDEREÇOS
	for idx, row in dataframe.iterrows():
		locations.append(row.get(column_address))

	# OBTENDO OS RESULTADOS DE TODAS AS LOCALIZAÇÕES
	dict_result_locations = geopy.get_information_using_address(locations=locations)

	# RETORNO O RESULTADO
	return dict_result_locations