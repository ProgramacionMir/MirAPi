import datetime as dt
from pydantic import BaseModel


class ItemBase(BaseModel):
    nombre: str
    title: str
    description: str 
    Requested_date: dt.date
    


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    Sended_date: dt.date
    _Status: str


    class Config:
        orm_mode = True
