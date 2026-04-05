from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('mysql+pymysql://aluno:ifsp@localhost:3306/virso')

Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)