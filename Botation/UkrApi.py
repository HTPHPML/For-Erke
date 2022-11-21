import requests
from pprint import pprint
import os


def getDataRu(vin):
    #curl -L -X POST "https://pro.autoteka.ru/token/" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "grant_type=client_credentials" --data-urlencode "client_id=aX5imuSpmGl4xElVp8eQ" --data-urlencode "client_secret=vYTQ-AHkjq2AxKaBSxCQByEwfTW11t5Tq433RwG_"
    data = os.system('curl -L -X POST "https://pro.autoteka.ru/token/" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "grant_type=client_credentials" --data-urlencode "client_id=aX5imuSpmGl4xElVp8eQ" --data-urlencode "client_secret=vYTQ-AHkjq2AxKaBSxCQByEwfTW11t5Tq433RwG_"')
    r = requests.get('https://pro.autoteka.ru/token/', headers={"Content-Type: application/x-www-form-urlencoded"}, data={})
    r.json()
    data = data.json()
    key = data.access_token
    url = f"https://pro.autoteka.ru/autoteka/v1/previews/{vin}"
    r = requests.get(url, headers={"Accept":"application/json", "X-Api-Key": key})
    data = r.json()
    return data


def getData(vin):
    key = "cb3c3367bfef96abaf6a85645c8c8418"
    url = "https://baza-gai.com.ua/vin/" + vin
    r = requests.get(url, headers={"Accept": "application/json", "X-Api-Key": key})
    data = r.json()
    return data


def sortData(data):
    if len(data) == 1:
        return ["Информация не найдена"]
    bool = {False: "Нет ✅", True: "Да ❌", None: "Нет ✅"}
    im = data['photo_url']
    basic = "Номер - " + data['digits'] + "\nvin - " + data['vin'] + "\n"
    model = "Модель - " + data['operations'][0]['color']['ru'] + " " + data['operations'][0]['vendor'] + " "\
            + data['model'] + " " + str(data['model_year'])
    legal = "Розыск - " + bool[data['is_stolen']] + "\nАдрес - " + data['operations'][0]['address']\
            + "\nСервис центр - " + data['operations'][0]['department'] + "\nИнформация об угоне - " + bool[data['stolen_details']]
    final = data['operations'][0]['operation']['ru'] + "\nДата регистрации - " + data['operations'][0]['registered_at']
    ret = [im, basic, model, legal, final]
    return ret


def main(vin):
    #data = getData(vin)
    #pprint(data)
    pprint(getDataRu(vin))
    #ret = sortData(data)
    #return ret


if __name__ == '__main__':
    #main("WBA7U61040CG57838")
    #main("WBA7U61040CG57837")
    main("example")