# run.py

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)
app.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://figobaek:dt2021@localhost/dreamteam_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


if __name__ == "__main__":
     app.run(debug = True, host='192.168.0.6')