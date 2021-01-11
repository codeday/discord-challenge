from os import getenv

from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

postgres_db = {
    "drivername": "postgres",
    "username": getenv("DB_USERNAME", "postgres"),
    "password": getenv("DB_PASSWORD"),
    "database": getenv("DB_DB", "discord-challenge"),
    "host": getenv("DB_HOST", "postgres-master-pg.service.consul"),
    "port": 5432,
}
postgres_url = URL(**postgres_db)
engine = create_engine(postgres_url)
metadata = MetaData()

Base = declarative_base(bind=engine, metadata=metadata)


class ChallengeUser(Base):
    __tablename__ = "challenge_users"

    id = Column(Integer, primary_key=True)
    member_id = Column(String, nullable=False)
    challenges_completed = Column(Integer, nullable=False)


metadata.create_all(engine)


def session_creator() -> Session:
    session = sessionmaker(bind=engine)
    return session()


global_session: Session = session_creator()
