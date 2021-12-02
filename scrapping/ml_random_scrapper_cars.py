import requests

from requests.structures import CaseInsensitiveDict

from multiprocessing import Pool

import json

url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1744'

token = 'SECRET_TOKEN_HERE'
headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"


resp = requests.get(url, headers=headers)

filtros_disponibles = [{x['id']:[y['id'] for y in x['values']]} for x in resp.json()['available_filters']]


estado_filtros = [{x:"incompleto"} for x in list(filtros_disponibles.keys())[0] ]

largo = len(filtros_disponibles)

def consultar(numero_proceso):
    proceso = numero_proceso
    cada_filtro = filtros_disponibles[proceso]
    
    filter_name = list(cada_filtro.keys())[0]

    for cada_valor in cada_filtro[filter_name]:
        
        basededatos = []

        URL = f'https://api.mercadolibre.com/sites/MLA/search?category=MLA1744&condition=used&limit=50&{filter_name}={cada_valor}'
        data_number = requests.get(URL, headers=headers).json()
        total = data_number['paging']['total']

        if total > 10000:
            iterations = 200
        elif total <= 10000:
            iterations = total // 50    


        for iteration in range(iterations+1):
            print(f"{'Filter:   '+ filter_name:<40}{'Value:  '+cada_valor:<40}{'Iteration:   '+str(iteration*50):<200}")
            URL = f'https://api.mercadolibre.com/sites/MLA/search?category=MLA1744&condition=used&limit=50&offset={iteration*50}&{filter_name}={cada_valor}'
            data = requests.get(URL, headers=headers).json()
            basededatos.extend(data['results'])

        with open(f'saved_files/filtro_{filter_name}_{cada_valor.replace("*","COMODIN")}.txt', 'w') as f:
            print(f"**********Saved Filter: {filter_name}, {cada_valor}***********")
            f.write(json.dumps(basededatos))
    
    # Esto es para guardar un txt con la información de los filtros listos (filtros solamente, no valores de los filtros)
    with open(f'saved_files/filtro_{filter_name}_{cada_valor.replace("*","COMODIN")}.txt', 'w') as f:
            print(f"**********Saved Filter: {filter_name}, {cada_valor}***********")
            f.write(json.dumps(basededatos))

if __name__ == '__main__':
    with Pool(processes=20) as pool:
        results = pool.map(consultar, range(largo))
