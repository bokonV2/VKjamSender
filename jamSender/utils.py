import requests, json, random
from datetime import date
from bs4 import BeautifulSoup

from jamSender.vkUtils import *

def getStyle(styleBg):
    if group.styleBg == 0:
        bg = getStyle(random.randint(1, 3))
    elif styleBg == 1:
        bg = 'bg1'
    elif styleBg == 2:
        bg = 'bg2'
    elif styleBg == 3:
        bg = 'bg3'
    else:
        bg = getStyle(random.randint(1, 3))
    return bg

def getData(group):
    bg = getStyle(group.styleBg)

    data = {
        "vkId": group.group_url,
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
        print(f"JamSender getImage {e}")
        return False
    return ids


def getSendPost(group):
    try:
        if date.today() <= group.date_oplata:
            if group.period == 0:
                if group.type_send != 1:
                    # ids = getImage(group)
                    # ids = "*id236657896 (Захар Бохан), *id236657896 (Захар Бохан), *id236657896 (Захар Бохан), *id236657896 (Захар Бохан)"
                    # sendPost(ids, group.message, getId(group.group_url))
                    group.status = "Отправленно"
                else: group.status = "Ручное отправление"
            else:
                group.status = "Ручное отправление"
        else:
            group.status = "Истёк период оплаты"
    except Exception as e:
        group.status = "Ошибка отправки"
        print(f"JamSender getSendPost {group.group_url} {e}")
    finally:
        group.save()

def u_reset(Groups):
    for group in Groups.select():
        group.status = "___"
        group.save()

def u_start(Groups):
    for group in Groups.select():
        getSendPost(group)

def u_startId(Groups, group_url):
    group = Groups.get(Groups.group_url == group_url)
    getSendPost(group)

def u_addGroup(
        Groups,
        group_url,
        date_add,
        date_oplata,
        chat_url,
        money,
        type_send,
        period,
        message,
        styleBg,
        styleFr,
        time_send,
    ):

    try:
        Groups.create(
            group_url = group_url,
            date_add = date.today(),
            date_oplata = date_oplata,
            chat_url = chat_url,
            money = money,
            type_send = type_send,
            period = period,
            message = bytes(message, 'utf-8'),
            styleBg = styleBg,
            styleFr = styleFr,
            time_send = time_send,
            status = "Добавлена",
        )
    except Exception as e:
        print(f"JamSender u_create {e}")
        return "0"

def u_addPayDay(
        Groups,
        group_url,
        date_oplata,
        chat_url,
        money,
        type_send,
        period,
        message,
        styleBg,
        styleFr,
        time_send,
    ):
    try:
        edit = Groups.get(Groups.group_url == group_url)
        edit.date_oplata = date_oplata
        edit.chat_url = chat_url
        edit.money = money
        edit.type_send = type_send
        edit.period = period
        edit.message = message
        edit.styleBg = styleBg
        edit.styleFr = styleFr
        edit.time_send = time_send
        edit.status = "Изменён"
        edit.save()
    except Exception as e:
        print(f"JamSender u_addPayDay {e}")
        return "0"

def u_removeGroup(Groups, group_url):
    try:
        to_del = Groups.get(Groups.group_url == group_url)
        to_del.delete_instance()
    except Exception as e:
        print(f"JamSender u_removeGroup {e}")
        return "0"

def u_getInfGroup(Groups, group_url):
    edit = Groups.get(Groups.group_url == group_url)
    data = {
        "group_url": edit.group_url,
        "date_add": str(edit.date_add),
        "date_oplata": str(edit.date_oplata),
        "chat_url": edit.chat_url,
        "money": edit.money,
        "type_send": edit.type_send,
        "period": edit.period,
        "message": edit.message,
        "styleBg": edit.styleBg,
        "styleFr": edit.styleFr,
        "time_send": str(edit.time_send)
    }
    return data
