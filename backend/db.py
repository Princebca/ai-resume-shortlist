# db.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///resumes.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Candidate(Base):
__tablename__ = 'candidates'
id = Column(Integer, primary_key=True, index=True)
name = Column(String, index=True)
email = Column(String, index=True)
filename = Column(String)
text = Column(Text)
embedding = Column(Text) # store as JSON string


Base.metadata.create_all(bind=engine)
