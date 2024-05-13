#pip install sqlalchemy
#pip install pymysql

from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://usuario:contraseña@localhost:3306/")

meta = MetaData()

conn = engine.connect()    