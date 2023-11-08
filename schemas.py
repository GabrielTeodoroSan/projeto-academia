from pydantic import BaseModel, ConfigDict, validator
from datetime import datetime


class Resident(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str 
    house_number: int 
    phone: str

    @validator("phone")
    def phone_validator(cls, phone):
        if not phone.isnumeric() or len(phone) != 11:
            raise ValueError(f"O número de telefone não está correto.")
        return phone
    

class ResidentCreate(Resident):

    pwd: str

    @validator("pwd")
    def pwd_validator(cls, pwd):
        if pwd == None:
            raise ValueError("Password é inválido.")
        return pwd 


class ResidentLogin(BaseModel):

    name: str 
    pwd: str

    @validator("name")
    def name_validator(cls, name):
        if name == None:
            raise ValueError("O nome é inválido")
        return name

    @validator("pwd")
    def pwd_validator(cls, pwd):
        if pwd == None:
            raise ValueError("Password é inválido.")
        return pwd
    


class Notebook(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: datetime 
    qr_code: str 
