from datetime import datetime
from sqlalchemy import insert, select, update
from sqlalchemy.orm import Session

import Models as models
import schema as schemas



def delete_itms(db: Session, itm = schemas.ItemCreate, id = int):
    sele = select(models.Item).where(models.Item.id == id).subquery()
    stm = db.query(sele)
    db.delete(stm)
    db.commit()
    db.refresh(stm)
    return stm

def get_items(db: Session):
    sele = select(models.Item).where(models.Item._Status == "posted").order_by(models.Item.Sended_date)
    db.execute(sele)
    return sele


def create_item(db: Session, nombre = str,titulo =str,desc = str, fecha = datetime,):
    db_item = insert(models.Item).values(Nombre = nombre, title = titulo, Description = desc, Requested_date =fecha, _Status = "posted")
    db.execute(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def updatestatus(db: Session, id = int, status = str):
    db_update = update(models.Item).where(models.Item.id == id).values(_Status = status)
    db.add(db_update)
    db.commit()
    db.refresh(db_update)
    return db_update