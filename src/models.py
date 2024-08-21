from sqlalchemy import create_engine, Column, String, Integer, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    stars = Column(Integer)
    forks = Column(Integer)
    open_issues = Column(Integer)

    __table_args__ = (
        UniqueConstraint('name', name='repositories_name_key'),
    )

# PostgreSQL connection string
DATABASE_URL = 'postgresql://devpulse_user:admin123@localhost/devpulse_db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
