# run.py

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)
app.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1/dreamteam_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == "__main__":
     app.run(debug = True )