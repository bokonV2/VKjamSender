import requests
from flask import Flask, render_template, request
from datetime import date

from objekt import *
from utils import *
from vkUtils import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', obj=Groups.select())

@app.route('/reset', methods=['POST'])
def reset():
    for group in Groups.select():
        group.send = "Сброс"
        group.save()
    return "1"

@app.route('/start', methods=['POST'])
def start():
    for group in Groups.select():
        if date.today() <= group.payDay:
            getImage(group)
            ids = getImage(group)
            sendPost(ids, getId(group.groupUrl))
            group.send = "Отправленно"
        else:
            group.send = "Истёк период"
        group.save()

    return "1"

@app.route('/startId', methods=['POST'])
def startId():
    print(request.form)
    gName = request.form.get("gName")

    group = Groups.get(Groups.groupName == gName)
    ids = getImage(group)
    sendPost(ids, getId(group.groupUrl))
    group.send = "Отправленно"
    group.save()

    return "1"

@app.route('/addGroup', methods=['POST'])
def addGroup():
    print(request.form)
    groupName = request.form.get("groupName")
    groupUrl = request.form.get("groupUrl")
    style = request.form.get("style")
    payDay = request.form.get("payDay")
    money = request.form.get("money")

    try:
        Groups.create(
            groupName = groupName,
            groupUrl = groupUrl,
            style = style,
            payDay = payDay,
            money = money,
            send = "Добавлен",
            message = "0"
        )
    except Exception as e:
        print(e)
        return "0"
    return "1"

@app.route('/addPayDay', methods=['POST'])
def addPayDay():
    print(request.form)
    gName = request.form.get("gName")
    money = request.form.get("money")
    payDay = request.form.get("payDay")

    try:
        edit = Groups.get(Groups.groupName == gName)
        edit.money = money
        edit.payDay = payDay
        edit.save()
    except Exception as e:
        print(e)
        return "0"
    return "1"

@app.route('/removeGroup', methods=['POST'])
def removeGroup():
    gName = request.form.get("gName")

    try:
        to_del = Groups.get(Groups.groupName == gName)
        to_del.delete_instance()
    except Exception as e:
        print(e)
        return "0"
    return "1"





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
