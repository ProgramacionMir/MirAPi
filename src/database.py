import struct

#SQLALCHEMY
from sqlalchemy import create_engine
import sqlalchemy.ext.declarative as  _declarative
import sqlalchemy.orm as _orm
import sqlalchemy as _sa
import sqlalchemy.dialects as _sad
from sqlalchemy.engine.url import URL
from sqlalchemy.dialects import mssql

#pyodb
import pyodbc as dbc


SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://SOPORTETECNICO\MIR/prueba?driver=ODBC+Driver+18+for+SQL+Server"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

SQLALCHEMY_DRIVER = 'ODBC+DRIVER+13+for+SQL+Server'
#SQLALCHEMY_DRIVER

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False,
                                            "TrustServerCertificate": "yes"}, echo = False
)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base =  _declarative.declarative_base()

