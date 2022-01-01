from flask import Blueprint, request, render_template, redirect, jsonify, make_response, session
import datetime
from jamSender.objekt import *
from jamSender.utils import *


jamSender = Blueprint("jamSender", __name__, template_folder='templates', static_folder="static")
Groups = groups

@jamSender.route('/')
@jamSender.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        password = request.form.get("password")
        if password == "admin000":
            session["logged"] = True
            return redirect('/jamSender/main')
    else:
        if session.get("logged") != None:
            return redirect('/jamSender/main')
    return render_template('jamSender/login.html')

@jamSender.route('/logout')
def unlogin():
    session["logged"] = None
    return redirect('/jamSender/main')

@jamSender.route('/main')
def index():
    if session.get("logged") == None:
        return redirect("/jamSender/login")
    return render_template('/jamSender/index.html', obj=Groups.select())

@jamSender.route('/sort/<id>')
def sort(id):
    if session.get("logged") == None:
        return redirect("/jamSender/login")
    id = int(id)
    if id == 0:
        obj = Groups.select().where(groups.date_oplata >= datetime.date.today())
    elif id == 1:
        obj = Groups.select().where(groups.date_oplata <= datetime.date.today())
    elif id == 2:
        obj = Groups.select().where(groups.type_send == 1 or groups.period == 1)
    return render_template('/jamSender/index.html', obj=obj)

@jamSender.route('/search', methods=['POST'])
def search():
    if session.get("logged") == None:
        return redirect("/jamSender/login")
    obj = Groups.select().where(groups.group_url.in_([request.form.get("group_url"),]))
    return render_template('/jamSender/index.html', obj=obj)

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
    u_startId(Groups, request.form.get("gName"))
    return "1"

@jamSender.route('/addGroup', methods=['POST'])
def addGroup():
    print(f"JamSender addGroup {request.form}")
    re = request.form
    u_addGroup(Groups,
        re.get("group_url"),
        None,
        re.get("date_oplata"),
        re.get("chat_url"),
        re.get("money"),
        re.get("type_send"),
        re.get("period"),
        re.get("message"),
        re.get("styleBg"),
        re.get("styleFr"),
        re.get("time_send"),
    )
    return "1"

@jamSender.route('/addPayDay', methods=['POST'])
def addPayDay():
    print(f"JamSender addPayDay {request.form}")
    re = request.form
    u_addPayDay(Groups,
        re.get("group_url"),
        re.get("date_oplata"),
        re.get("chat_url"),
        re.get("money"),
        re.get("type_send"),
        re.get("period"),
        re.get("message"),
        re.get("styleBg"),
        re.get("styleFr"),
        re.get("time_send"),
    )
    return "1"

@jamSender.route('/removeGroup', methods=['POST'])
def removeGroup():
    print("JamSender removeGroup")
    u_removeGroup(Groups, request.form.get("gName"))
    return "1"

@jamSender.route('/getInfGroup', methods=['POST'])
def getInfGroup():
    print(f"JamSender getInfGroup {request.form}")
    response = u_getInfGroup(Groups, request.form.get("group_url"))
    return make_response(jsonify(response), 200)
