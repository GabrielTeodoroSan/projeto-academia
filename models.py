from database import Base 
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Boolean


class Resident(Base):
    __tablename__ = "resident"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    house_number = Column(Integer)
    phone = Column(String)


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    date = Column(DateTime)
    valid = Column(Integer, default=1)


class Notebook(Base):
    __tablename__ = "notebook"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    resident_id = Column(Integer, ForeignKey("resident.id", ondelete="CASCADE"), nullable=False)
    ticket_id = Column(Integer, ForeignKey("ticket.id", ondelete="CASCADE"), nullable=False)
    qr_code = Column(String)


class LastTimeBuild(Base):
    __tablename__ = "lasttimebuild"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)