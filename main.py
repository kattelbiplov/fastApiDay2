from fastapi import FastAPI, Depends
from requests import session
from sqlalchemy.orm import Session
import db
from models import Person
from models import UserTable

app = FastAPI()

@app.get("/{id}")
def get_user(id: int, db: Session = Depends(db.get_db)):
    data = db.query(models.UserTBL).filter(models.UserTBL.iduser_id == id).first()
    return {"data": data}

@app.post("/person")
def add_person(username:str, password:str, email:str, blog_id: int, db:session=Depends(db.get_db)):
    data = Person(person_username = username, person_password = password, person_email = email, blog_id = blog_id )
    db.add(data)
    db.commit()
    return {"status":201, "message":"Data Added Sucessfully", "data":data}


@app.get("/{id}")
def get_user_by_id(id: int, db: Session = Depends(db.get_db)):
    data = db.query(Person).filter(Person.person_id == id).first()
    return {"status":200, "message":"Data Found","data": data}