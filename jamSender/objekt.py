from peewee import *
import datetime

user = 'root'
password = 'root'
db_name = 'vk'
#
db = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost',
    port=3306,
    charset='utf8mb4'
)

class BaseModel(Model):
    class Meta:
        database = db

class tmp(Model):
    id = IntegerField(null=False)
    text = CharField(max_length=100)

class groups(BaseModel):
    id = IntegerField(null=False, primary_key=True)
    group_url = TextField()
    date_add = DateField()
    date_oplata = DateField()
    chat_url = TextField()
    money = IntegerField()
    type_send = IntegerField()
    period = IntegerField()
    message = TextField()
    styleBg = IntegerField()
    styleFr = IntegerField()
    time_send = TimeField()
    status = TextField()

    class Meta:
        db_table = 'groups'



class vk(BaseModel):
    id = IntegerField(primary_key=True)
    group = TextField()
    date_add = DateField()
    date_oplata = DateField()
    link_dialog = TextField()
    tarif = TextField()
    tipe = TextField()
    period = TextField()
    text = TextField()
    dizajn = TextField()
    ramki = TextField()
    time = CharField()


if __name__ == '__main__':
    pass
    # db.connect()
    # db.create_tables([groups, vk])
    # groups.create_table()

    # groups.save()
    # print(groups.select().where(groups.id == 1))

    # for group in groups.select():
    #     group.message = str(group.message).strip()
    #     group.save()

    # for group in vk.select():
    #     tipe = group.tipe
    #     if tipe == "Ручной":
    #         tipe = 0
    #     elif tipe == "Авто":
    #         tipe = 1
    #     elif tipe == "Предложка":
    #         tipe = 2
    #
    #     period = group.period
    #     if period == "Ежедневно":
    #         period = 0
    #     elif period == "Авто":
    #         period = 1
    #
    #     if group.dizajn == "Рандом":
    #         dizajn = 0
    #     else:
    #         try:
    #             dizajn = int(group.dizajn)
    #         except Exception as e:
    #             print(group.dizajn)
    #             dizajn = int(input())
    #
    #     if group.ramki == "Рандом":
    #         ramki = 0
    #     else:
    #         try:
    #             ramki = int(group.ramki)
    #         except Exception as e:
    #             print(group.ramki)
    #             ramki = int(input())
    #
    #     groups.create(
    #         group_url = group.group,
    #         date_add = group.date_add,
    #         date_oplata = group.date_oplata,
    #         chat_url = group.link_dialog,
    #         money = int(group.tarif),
    #         type_send = tipe,
    #         period = period,
    #         message = bytes(group.text, 'utf-8'),
    #         styleBg = dizajn,
    #         styleFr = ramki,
    #         time_send = datetime.time.fromisoformat(group.time),
    #         status = "Перенесена",
    #     )
    #
    #     print()
