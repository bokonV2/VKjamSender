from flask import Blueprint, request, render_template, redirect

from jamSender.objekt import *
from jamSender.utils import *


jamSender = Blueprint("jamSender", __name__, template_folder='templates', static_folder="static")


@jamSender.route('/')
def index():
    try:
        return render_template('/jamSender/index.html', obj=Groups.select())
    except:
        return redirect("/jamSender/create")
@jamSender.route('/reset', methods=['POST'])
def reset():
    u_reset(Groups)
    return "1"

@jamSender.route('/start', methods=['POST'])
def start():
    print("JamSender start")
    u_reset(Groups)
    u_start(Groups)
    return "1"

@jamSender.route('/startId', methods=['POST'])
def startId():
    print(f"JamSender startID {request.form}")
    gName = request.form.get("gName")
    u_startId(Groups, gName)
    return "1"

@jamSender.route('/addGroup', methods=['POST'])
def addGroup():
    print(f"JamSender addGroup {request.form}")
    groupName = request.form.get("groupName")
    groupUrl = request.form.get("groupUrl")
    style = request.form.get("style")
    payDay = request.form.get("payDay")
    money = request.form.get("money")
    message = request.form.get("message")
    u_addGroup(Groups, groupName, groupUrl, style, payDay, money, message)
    return "1"

@jamSender.route('/addPayDay', methods=['POST'])
def addPayDay():
    print(f"JamSender addPayDay {request.form}")
    gName = request.form.get("gName")
    money = request.form.get("money")
    payDay = request.form.get("payDay")
    u_addPayDay(Groups, gName, money, payDay)
    return "1"

@jamSender.route('/removeGroup', methods=['POST'])
def removeGroup():
    print("JamSender removeGroup")
    gName = request.form.get("gName")
    u_removeGroup(Groups, gName)
    return "1"

@jamSender.route('/create')
def create():
    db.connect()
    db.create_tables([Groups,])
    return redirect("/jamSender/")
