from flask import Flask
from api.databaseHandler import DatabaseHandler

db = DatabaseHandler('35.224.224.28')

db.createDB('carShareScheme')
db.createTables()

app = Flask(__name__)

import api.routes