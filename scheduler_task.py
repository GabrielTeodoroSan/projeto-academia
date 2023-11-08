from database import SessionLocal

import crud


def generate_tickets():
    db = SessionLocal()
    crud.create_tickets(db=db)
    db.close()