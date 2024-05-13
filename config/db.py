#pip install sqlalchemy
#pip install pymysql

from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgres+pyscopg2://dvote_user:aD7nniFvRBRiCc4rkSTBWcypCQh18yka@dpg-cp0nkta1hbls73edkjc0-a.ohio-postgres.render.com/dvote"

engine = create_engine(DATABASE_URL)

meta = MetaData()

conn = engine.connect()    