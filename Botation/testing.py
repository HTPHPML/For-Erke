from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup


def getData(browser, service):
    services = {0: "Введен неправильный VIN или машина не зарегестрирована в РФ", 1: "Информации о ДТП не найдено",
                2: "Не находится в розыске", 3: "Ограничений не найдено",
                4: "Данные о прохождении ТО не найдены, либо сайт ГИБДД не доступен",
                5: "Инфорамации об использовании в качестве такси не найдено",
                6: "По данному запросу результатов не найдено! Автомобиль не находится в залоге!",
                7: "Информация не найдена", 8: "Информация не найдена", 9: "Информация не найдена"}
    data = []

    soup = BeautifulSoup(browser.page_source, features="html.parser")
    table = soup.find('table', attrs={'class': 'table table-striped'})
    table_body = table.find("tbody")

    if table_body is None:
        return services[service]

    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('th')
        ols = [ele.text.strip() for ele in cols]
        cols = row.find_all("td")
        roe = [ele.text.strip() for ele in cols]
        if len(ols) != 0:
            data.append(ols)
        if len(roe) != 0:
            data.append(roe)

    return data


def managestr(text):
    if type(text) == str():
        return text
    ret = ""
    for double in text:
        if len(double) == 2:
            stra = double[0] + ": " + double[1]
        else:
            stra = double[0]
        ret += stra + "\n"
    return ret


def findService(num, service):
    services = {0: "history", 1: "dtp", 2: "wanted", 3: "restrict",
                4: "diagnostic", 5: "taxi", 6: "zalog",
                7: "probeg", 8: "osago1", 9: "sud"}

    # create webdriver, open url
    browser = webdriver.Chrome('assets/chromedriver.exe')
    browser.get('https://vin01.ru')
    # toggle Vin option
    vin = browser.find_element(By.ID, "vinToggleButton")
    vin.click()
    time.sleep(1)
    # enter vin num
    elem = browser.find_element(By.ID, "vinNumber")
    elem.send_keys(num)
    # search
    search = browser.find_element(By.ID, "searchByVinNumberButton")
    search.click()
    time.sleep(1)
    # choose option
    select = Select(browser.find_element(By.ID, "checkType"))
    select.select_by_value(services[service])
    # search
    search = browser.find_element(By.ID, "getCheckButton")
    search.click()
    time.sleep(5)
    ret = managestr(getData(browser, service))
    return ret


if __name__ == '__main__':
    f = open("assets/dat.txt", "w", encoding='utf-8')
    f.write(findService("VSSZZZ6JZ9R045789", 0))