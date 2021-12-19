import requests
from bs4 import BeautifulSoup

def getData(group):
    if group.style == 0:
        bg = 'bg1'
    elif group.style == 1:
        bg = 'bg2'
    elif group.style == 2:
        bg = 'bg3'

    data = {
        "vkId": group.groupUrl,
        "BGDef": bg,
        "STDef": 'st1',
        "dayPromej": '365',
        "MalePos": '0',
        "IDCountry": '',
        "VKToken": '',
        "NoAva": 'On',
    }
    return data

def getImage(group):
    try:
        response = requests.post("http://boostbrand.ru/ind", data=getData(group))
        print(response)
        soup = BeautifulSoup(response.content, 'lxml')
        ids = soup.find("p", class_="u-align-left u-text u-text-2").text
        ids = ids.replace("\n", " ")
        p = requests.get("http://boostbrand.ru/get_image")
        with open("static/img.jpg", "wb") as f:
            f.write(p.content)


    except Exception as e:
        print(e)
        return False

    return ids
