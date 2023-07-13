import database as _database
import Models as _mod
import schema as _sch

import sqlalchemy.orm as _orm
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import delete

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# dev only------------------------------------------------------------
def getuser(db: _orm.Session, name:str):
    return db.query(_mod.User).filter((_mod.User.Name == name)).first
#---------------------------------------------------------------------

def crear_usuario(db:_orm.Session, user: _sch.usuario):
    db_user = insert(_mod.User).values(Name= "", hashed_password = "")
    db.add(db_user)
    db.commit()    
    return db_user

def borrar_servicio( db: _orm.Session, ID: int):
    db.query(delete(_mod.service).where(_mod.service.id == ID))
    return 

def Mostrar_servicios(  db: _orm.Session):
    stm = db.query(select(_mod.service.title, _mod.service.description, _mod.service.Date))
    return stm

def post_services(db: _orm.Session,  title: str, sender: str):
    stm = db.query(insert(_mod.service).values(title = title, Sender = sender))
    db.add(stm)
    db.commit()
    return stm
