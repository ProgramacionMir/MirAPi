# ---------------------------------------------------------------------------------------------------------

#produccion--Calificaciones -------------------------------------------------------------------------------
@app.get("/calificaciones/{Curso},{materia}", response_model=schemas.Item)
def Read_calificaciones(curso : int, materia: str, db: Session = Depends(get_db)):
    users = crud.obtener_calificaciones(db)
    return users

@app.post("/add_calificaciones/{nombre},{titulo},{desc},{fecha}", response_model=schemas.ItemBase)
def create_calificaciones(nombre = str,titulo =str,desc = str, fecha = datetime, db: Session = Depends(get_db)):
    response = crud.create_nota(db=db, nombre=nombre, titulo= titulo, desc= desc, fecha = fecha )
    return response

@app.post("/items/update_nota/{id},{status}")
def update(id :int, st: str, db: Session = Depends(get_db)):
    upd = crud.update_nota(db, id=id, status=st)
    return upd

@app.delete("/del_nota/{item_id}", response_model=schemas.ItemBase)
def delete_items(item_id: int, db: Session = Depends(get_db)):
    users = crud.delete_nota(db =db, id=item_id)
    return users
# --------------------------------------------------------------------------------------------------------- 

#produccion-Ususarios -------------------------------------------------------------------------------------
@app.get("/Ususarios/", response_model=schemas.Item)
def Read_users(curso : int, materia: str, db: Session = Depends(get_db)):
    users = crud.obtener_calificaciones(db)
    return users

@app.get("/Ususarios/materias/{materia}", response_model=schemas.Item)
def Read_users_by_materia(curso : int, materia: str, db: Session = Depends(get_db)):
    users = crud.obtener_calificaciones(db)
    return users

@app.get("/Ususarios/centro/{centro}", response_model=schemas.Item)
def Read_users_by_center(curso : int, materia: str, db: Session = Depends(get_db)):
    users = crud.obtener_calificaciones(db)
    return users

@app.get("/Ususarios/materias/centro/{centro},{materia}", response_model=schemas.Item)
def Read_users_by_center_and_materia(curso : int, materia: str, db: Session = Depends(get_db)):
    users = crud.obtener_calificaciones(db)
    return users

# --------------------------------------------------------------------------------------------------------- 


@app.post("/usuario/{nombre},{apellido},{materia},{centro},{}", response_model=schemas.ItemBase)
def create_user(nombre = str,titulo =str,desc = str, fecha = datetime, db: Session = Depends(get_db)):
    response = crud.create_item(db=db, nombre=nombre, titulo= titulo, desc= desc, fecha = fecha )
    return response

# --------------------------------------------------------------------------------------------------------- 

@app.post("/items/update_usr/{id},{status}")
def update_user(id :int, st: str, db: Session = Depends(get_db)):
    upd = crud.updatestatus(db, id=id, status=st)
    return upd

@app.delete("/del_usr/{item_id}", response_model=schemas.ItemBase)
def delete_user(item_id: int, db: Session = Depends(get_db)):
    users = crud.delete_itms(db =db, id=item_id)
    return users
# --------------------------------------------------------------------------------------------------------- 