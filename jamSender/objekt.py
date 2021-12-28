from peewee import *
from datetime import date
from pprint import pprint

db = SqliteDatabase('jamSender/static/groups.db')


class BaseModel(Model):
    class Meta:
        database = db


class Groups(BaseModel):
    groupName = CharField(unique=True)
    groupUrl = CharField(unique=True)
    style = IntegerField()
    payDay = DateField()
    money = IntegerField()
    send = CharField()
    message = CharField()



if __name__ == '__main__':
    # pass
    db.connect()
    db.create_tables([Groups,])

    # aa = Groups.get(Groups.groupName == Groups.select()[0].groupName)
    # aa.money = 500
    # aa.save()

    # for person in Groups.select():
    #      print(person.groupName)

    # grandma = Groups.create(
    #     groupName = "GroupsName2",
    #     style = 2,
    #     groupUrl = "url3",
    #     payDay = date(2021, 12, 18),
    #     money = 300,
    #     send = False
    # )