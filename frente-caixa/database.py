from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:senha@localhost/frentecaixa"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)