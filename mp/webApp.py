from mp.config import Config
from flask import Flask

app = Flask(__name__, template_folder='view/templates')
app.config.from_object(Config)

import mp.routes