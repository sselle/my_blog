__author__ = "sven"
import pymongo

# hier wird eine statische Klasse angelegt --> kein Konstruktor
# static properties werden direkt über die Klasse angesprochen, nicht über self --> Es gibt hier keine Instanzen der Klasse
class Database(object):
    URI = "mongodb://54.93.59.226:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(host=Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    # Gibt cursor auf den Anfang der Collection zurück
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # Gibt das erste JSON Objekt aus der DB zurück
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)