from datetime import datetime
from peewee import *

db = SqliteDatabase('FCard.db')


class User(Model):
    user_name = CharField()
    token = IntegerField()
    count_card = IntegerField()
    level = IntegerField()
    get_today = DateField(null=True)

    class Meta:
        database = db


class Deck(Model):
    user = ForeignKeyField(User, related_name='deck')
    count = IntegerField()

    class Meta:
        database = db


class Kard(Model):
    kard_name = CharField()
    rarity = CharField()
    img = CharField()
    procent = FloatField()
    coficent = FloatField()

    class Meta:
        database = db


class User_Kard(Model):
    kard = ForeignKeyField(Kard, related_name='kard')
    deck = ForeignKeyField(Deck, related_name='deck')

    class Meta:
        database = db


Kard.create_table()
Deck.create_table()
User.create_table()
User_Kard.create_table()