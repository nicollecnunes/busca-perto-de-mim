from pprint import pprint
import json
import requests
import googlemaps

API_KEY = input('Digite a sua API KEY do Google Places ')
map_client = googlemaps.Client(API_KEY)

busca = input('O que você deseja buscar?\n> ')

msg = input('Digite a mensagem que você quer enviar:\n> ')
msg = msg.replace(" ", "%20")

def get_place_info(location_name):
    try:
        response = map_client.places(query=location_name)
        results = response.get('results')
        return results
    except Exception as e:
        print(e)
        return None

place_info = get_place_info(busca)
aux = 0

lista_ids = []
while (0<1):
    try:
        lista_ids.append(place_info[aux]['place_id'])
        aux = aux + 1
    except Exception as e:
        break

payload = {}
headers = {}

lista_infos = []

print("Buscando telefones de " + str(len(lista_ids)) + " resultados...")
for i in range(len(lista_ids)):
    idAtual = lista_ids[i]
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + idAtual + "&fields=name%2Cformatted_phone_number&key=" + API_KEY
    response = requests.request("GET", url, headers=headers, data=payload)
    lista_infos.append(response.text)


print("Obtidos " + str(len(lista_infos)) + " resultados com telefone:")
for i in range(len(lista_infos)):
    y = json.loads(lista_infos[i])
    if(len(y['result']) == 2):
        print('-------------------------------------------------------------------------------------------------------')
        print(y['result']['name'])
        print(y['result']['formatted_phone_number'])
        tel = y['result']['formatted_phone_number'].replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
        
        if (msg != ""):
            print("Link do whatsapp: " + "wa.me/55" + tel + "?text=" + str(msg))
        else:
            print("Link do whatsapp: " + "wa.me/55" + tel)




