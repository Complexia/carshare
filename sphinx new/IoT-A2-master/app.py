from api import DatabaseHandler
from api import app

# import routes after initialising a flask app to not create a circular import
from api.routes import *

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)