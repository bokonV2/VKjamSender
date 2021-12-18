from flask import Flask, render_template, request

from objekt import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', obj=Groups.select())

@app.route('/start', methods=['POST'])
def start():


    for group in Groups.select():
        group.send = True
        group.save()


    return "1"

@app.route('/startId', methods=['POST'])
def startId():
    print(request.form)
    gName = request.form.get("gName")

    try:
        this = Groups.get(Groups.groupName == gName)
        this.send = False
        this.save()
    except Exception as e:
        print(e, "\nsdfsdfsdfsd")


    return "1"

@app.route('/addGroup', methods=['POST'])
def addGroup():
    groupName = request.form.get("groupName")
    groupId = request.form.get("groupId")
    groupUrl = request.form.get("groupUrl")
    payDay = request.form.get("payDay")
    money = request.form.get("money")

    try:
        Groups.create(
            groupName = groupName,
            groupId = groupId,
            groupUrl = groupUrl,
            payDay = payDay,
            money = money,
            send = False
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
