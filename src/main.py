from datetime import datetime
import os
import sys

from fastapi import Depends, FastAPI, HTTPException#
#import fastapi as _fast
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger

from typing import List

#import services as _serv
from sqlalchemy.orm import Session

from database import SessionLocal, engine

import crud
import Models as models
import schema as schemas

from pydantic import BaseSettings


#ngrook 
class Settings(BaseSettings):
    # our fast api settings

    Base_url = " "
    USE_NGROK = os.environ.get("USE_NGROK", "FALSE") == "True"

settings = Settings()

def Init_Webhooks(Base_url):
    #update inbound Traffic Via API to use the public -facing ngrook URL
    pass

#fastApi
app = FastAPI()

#ngrok ini
if settings.USE_NGROK:
    #pyngrok should only ever be initialize in dev enviroment
    from pyngrok import ngrok

    #get dev server port (defaullt to 8000 in uvicorn but can be override when starting a server)
    port = sys.argv[sys.argv.index("--port")+1] if "--port" in sys.argv else 8000


    #open the ngrook tunel for the dev server
    public_url = ngrok.connect(port).public_url
    logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

    #update any base url or webhooks to use ngrok url
    settings.Base_url = public_url
    Init_Webhooks(public_url)

#implementing cors to avoid restriccion 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#_serv.create_database()
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#dev-------------------------------------------------------------------------------------------------------
@app.get("/prueba")
def prueba():
    return {"saludos": "hola mundo"}

#----------------------------------------------------------------------------------------------------------



#Produccion--Solicitudes -----------------------------------------------------------------------------------

@app.get("/items/", response_model=schemas.Item)
def read_item(db: Session = Depends(get_db)):
    users = crud.get_items(db)
    return users

@app.post("/add_items/{nombre},{titulo},{desc},{fecha}", response_model=schemas.ItemBase)
def create_item(nombre = str,titulo =str,desc = str, fecha = datetime, db: Session = Depends(get_db)):
    response = crud.create_item(db=db, nombre=nombre, titulo= titulo, desc= desc, fecha = fecha )
    return response

@app.post("/items/update/{id},{status}")
def update(id :int, st: str, db: Session = Depends(get_db)):
    upd = crud.updatestatus(db, id=id, status=st)
    return upd

@app.delete("/del_items/{item_id}", response_model=schemas.ItemBase)
def delete_items(item_id: int, db: Session = Depends(get_db)):
    users = crud.delete_itms(db =db, id=item_id)
    return users

