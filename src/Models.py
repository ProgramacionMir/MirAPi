from sqlalchemy import DATE, Boolean, Column, ForeignKey, Integer, String

from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String)
    title = Column(String)
    Description = Column(String)
    Requested_date = Column(DATE)
    Sended_date =Column(DATE, index = True)
    _Status = Column(String)
