from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean 
from config.db import meta, engine

users = Table('user', meta, Column('id', Integer, primary_key=True), Column('sha_dni', Integer), Column('voto', Boolean), Column('lugar_residencia', String(255)))

meta.create_all()