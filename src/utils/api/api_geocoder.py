from inspect import stack

import geocoder


class API_GEOCODER:

    """

    PERMITE OBTER INFORMAÇÕES
    DE LOCALIZAÇÃO
    USANDO ENDEREÇO
    OU LATITUDE E LONGITUDE.

    1. USANDO ENDEREÇO PARA
       OBTER INFORMAÇÕES: get_information_using_address
    2. USANDO LATITUDE E LONGITUDE
       PARA OBTER INFORMAÇÕES: get_information_using_lat_long

    """

    def __init__(self):
        # INIT GEOPY
        self.geolocator = geocoder

    def get_information_using_address(self, locations, verbose=False):
        """

        PERMITE OBTER INFORMAÇÕES
        DE LOCALIZAÇÃO
        USANDO ENDEREÇO

        # Arguments
            locations        - Required: Endereço ou
                                         lista de Endereços (String | Tuple | List)

        # Returns
            dict_result      - Required: Dict contendo a lista de endereços (Dict)

        """

        # INICIANDO DICT PARA ARMAZENAR RESULTADOS
        dict_result = {}

        # VERIFICANDO A TIPAGEM
        if isinstance(locations, str):
            locations = [locations]

        # PERCORRENDO CADA UM DOS ENDEREÇOS ENVIADOS
        for location in locations:

            print("BUSCANDO GEOCODE: {}".format(location))

            try:
                # CHAMANDO A API
                result_location = self.geolocator.osm(location)

                if result_location:

                    result_location = result_location.current_result

                    # SALVANDO O RESULTADO
                    dict_result[location] = {
                        "endereco": result_location.address,
                        "latitude": result_location.lat,
                        "longitude": result_location.lng,
                    }

                    if verbose:
                        raw_information = dict_result[location]
                        print(raw_information)

                else:
                    print("ENDEREÇO NÃO ENCONTRADO")

                    # ENDEREÇO NÃO ENCONTRADO
                    dict_result[location] = {}

            except Exception as ex:
                print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

                # ENDEREÇO NÃO ENCONTRADO
                dict_result[location] = {}

        return dict_result

    def get_information_using_lat_long(self, lat, long, verbose=False):
        """

        PERMITE OBTER INFORMAÇÕES
        DE LOCALIZAÇÃO
        USANDO LATITUDE E LONGITUDE

        # Arguments
            lat              - Required: Valor da latitude (Float)
            long             - Required: Valor da longitude (Float)

        # Returns
            dict_result      - Required: Dict contendo a lista de endereços (Dict)

        """

        # INICIANDO DICT PARA ARMAZENAR RESULTADOS
        dict_result = {}

        # VERIFICANDO A TIPAGEM
        if isinstance(lat, float) and isinstance(long, float):
            location = [lat, long]

        try:
            # CHAMANDO A API
            result_location = self.geolocator.reverse(location)

            # SALVANDO O RESULTADO
            dict_result[location] = result_location

            if verbose:
                raw_information = location.raw
                endereco = location.address
                print(f"{location}: Endereço {endereco}")
                print(raw_information)
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

        return dict_result
