# database.py
from sqlmodel import SQLModel, Session, create_engine, Field
from typing import Annotated
from fastapi import FastAPI,Depends

rds_connection_string = "postgresql+psycopg2://postgres:Uide.asu.123@database-api.cd428eek4eh8.us-east-2.rds.amazonaws.com:5532/database-api"
engine = create_engine(rds_connection_string, echo=True)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
