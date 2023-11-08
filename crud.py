from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Resident, Ticket, Notebook
from fastapi import status, Response
from fastapi.responses import FileResponse
from datetime import datetime, timedelta

import schemas
import qr_code


def create_user(user: schemas.ResidentCreate, db: Session):
    resident = Resident(name=user.name, house_number=user.house_number, phone=user.phone)
    db.add(resident)
    db.commit()
    db.flush(resident)
    return Response(status_code=status.HTTP_201_CREATED)


def create_tickets(db: Session):
    time = datetime.now() + timedelta(hours=3)
    for i in range(1, 10):
        ticket = Ticket(date=time + timedelta(hours=i))
        db.add(ticket)
        db.commit()
        db.flush(ticket)


def get_available_tickets(db: Session) -> list or str:
    tickets = db.query(Ticket).all()[::-1][:10]
    return tickets


def mark_ticket(db: Session, ticket_id: int, resident_id):
    qr = qr_code.generate_qr_code(ticket_id)
    new_note = Notebook(resident_id=resident_id, ticket_id=ticket_id, qr_code=qr)
    db.add(new_note)
    db.commit()
    db.flush(new_note)
    return FileResponse(qr)