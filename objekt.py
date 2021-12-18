from peewee import *
from datetime import date
from pprint import pprint

db = SqliteDatabase('groups.db')


class BaseModel(Model):
    class Meta:
        database = db


class Groups(BaseModel):
    groupName = CharField(unique=True)
    groupId = IntegerField(unique=True)
    groupUrl = CharField(unique=True)
    payDay = DateField()
    money = IntegerField()
    send = BooleanField()



if __name__ == '__main__':
    # pass
    # db.connect()
    # db.create_tables([Groups,])

    aa = Groups.get(Groups.groupName == Groups.select()[0].groupName)
    aa.money = 500
    aa.save()

    # for person in Groups.select():
    #      print(person.groupName)

    # grandma = Groups.create(
    #     groupName = "GroupsName2",
    #     groupId = -2,
    #     groupUrl = "url3",
    #     payDay = date(2021, 12, 18),
    #     money = 300,
    #     send = False
    # )
