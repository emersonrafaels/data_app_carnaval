import geocoder


def obter_lat_long(endereco):
	resultado = geocoder.osm(endereco)

	if resultado.ok:
		latitude = resultado.latlng[0]
		longitude = resultado.latlng[1]
		return latitude, longitude
	else:
		print("Endereço não encontrado.")
		return None


# Exemplo de uso
endereco = "R. SANTA BERTILA, 30 - PENHA"
endereco = "R. SANTA BERTILA, 30 - PENHA, SP"
coordenadas = obter_lat_long(endereco)

if coordenadas:
	print(f"A latitude e longitude de {endereco} são: {coordenadas}")
