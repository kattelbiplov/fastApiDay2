from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import db
import models


app = FastAPI()


@app.get("/{id}")
def get_user(id: int, db: Session = Depends(db.get_db)):
    data = db.query(models.UserTBL).filter(models.UserTBL.iduser_id == id).first()
    return {"data": data}