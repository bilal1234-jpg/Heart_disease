from sqlalchemy import create_engine
from sqlalchemy import Text, String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DB_heart(Base):
    __tablename__ = 'heart'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable = False)
    age = Column(Integer, nullable = False)
    gender = Column(String(10), nullable = False)
    chest_pain = Column(String(50), nullable = False)
    blood_pressure = Column(Integer, nullable = False)
    cholestrol = Column(Integer, nullable = False)
    fbs = Column(Integer, nullable = False)
    restecg = Column(Integer, nullable = False)
    max_heart_rate = Column(String(50), nullable = False)
    angina = Column(String(50), nullable = False)
    oldpeak = Column(Integer, nullable = False)
    slope = Column(Integer, nullable = False)

DATABASE_URL = "sqlite:///heart.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


