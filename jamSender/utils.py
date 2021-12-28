import requests
from datetime import date
from pprint import pprint
from bs4 import BeautifulSoup

from jamSender.vkUtils import *

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
        "VKToken": '2b319b6859e9149c9cf57bc79b8c9a1988ddf2f282f82f9418b2f044688100c68e6c23465038a740b296d',
    }
    return data

def getImage(group):
    try:
        response = requests.post("http://boostbrand.ru/ind", data=getData(group))
        print(f"JamSender getImage {response}")
        soup = BeautifulSoup(response.content, 'lxml')
        ids = soup.find("p", class_="u-align-left u-text u-text-2").text
        ids = ids.replace("\n", " ")
        p = requests.get("http://boostbrand.ru/get_image")
        with open("jamSender/static/img.jpg", "wb") as f:
            f.write(p.content)
    except Exception as e:
        print(e)
        return False

    return ids


def getSendPost(group):
    try:
        if date.today() <= group.payDay:
            ids = getImage(group)
            # ids = "*id236657896 (Захар Бохан), *id236657896 (Захар Бохан), *id236657896 (Захар Бохан), *id236657896 (Захар Бохан)"
            sendPost(ids, group.message, getId(group.groupUrl))
            group.send = "Отправленно"
        else:
            group.send = "Истёк период"
    except Exception as e:
        print(e)
        group.send = "ошибка отправления"
    finally:
        group.save()

def u_reset(Groups):
    for group in Groups.select():
        group.send = "Сброс"
        group.save()

def u_start(Groups):
    for group in Groups.select():
        getSendPost(group)

def u_startId(Groups, gName):
    group = Groups.get(Groups.groupName == gName)
    getSendPost(group)

def u_addGroup(Groups, groupName, groupUrl, style, payDay, money, message):
    try:
        Groups.create(
            groupName = groupName,
            groupUrl = groupUrl,
            style = style,
            payDay = payDay,
            money = money,
            send = "Добавлена",
            message = message
        )
    except Exception as e:
        print(e)
        return "0"

def u_addPayDay(Groups, gName, money, payDay):
    try:
        edit = Groups.get(Groups.groupName == gName)
        edit.money = money
        edit.payDay = payDay
        edit.save()
    except Exception as e:
        print(e)
        return "0"

def u_removeGroup(Groups, gName):
    try:
        to_del = Groups.get(Groups.groupName == gName)
        to_del.delete_instance()
    except Exception as e:
        print(e)
        return "0"
