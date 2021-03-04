# run.py

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)
app.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://b3988c11c5b010:ec7d2c99@us-cdbr-east-03.cleardb.com/heroku_7f2c85ae818dce2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


if __name__ == "__main__":
     app.run(debug = True)