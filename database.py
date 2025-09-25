# database.py
from sqlmodel import SQLModel, Session, create_engine, Field
from typing import Annotated
from fastapi import FastAPI,Depends

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

# Definición del modelo Product
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float

rds_connection_string = "postgresql+psycopg2://guillo:Guillo2006@database-api.cd428eek4eh8.us-east-2.rds.amazonaws.com:5532/postgres"
engine = create_engine(rds_connection_string, echo=True)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
