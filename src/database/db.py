from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

from src.config import db_settings


engine = create_engine(
    f"{db_settings.DBMS}+{db_settings.DRIVER}:///{db_settings.PATH}",
    echo=True
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def drop_database():
    Base.metadata.drop_all(engine)


def create_database():
    Base.metadata.create_all(engine)
