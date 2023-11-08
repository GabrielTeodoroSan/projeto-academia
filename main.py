from models import Base
from database import engine, SessionLocal
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from scheduler_task import generate_tickets

import schemas
import crud


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


scheduler = BackgroundScheduler()
trigger = CronTrigger(hour=11, minute=46)
scheduler.add_job(generate_tickets, trigger=trigger)
scheduler.start()


app = FastAPI()


@app.post("/user/create/")
def create_user(user: schemas.ResidentCreate, db: Session = Depends(get_db)):
    return crud.create_user(user=user, db=db)


@app.get("/tickets/show/")
def show_avaiable_tickets(db: Session = Depends(get_db)):
    return crud.get_available_tickets(db=db)


@app.get("/tickets/mark/{ticket_id}/{resident_id}")
def mark_ticket(ticket_id: int, resident_id: int, db: Session = Depends(get_db)):
    return crud.mark_ticket(ticket_id=ticket_id, resident_id=resident_id, db=db)