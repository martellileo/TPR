from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

def _get_db_password():
    env_path = Path(__file__).with_name(".env")
    line = env_path.read_text(encoding="utf-8").strip()
    return line.split("=", 1)[1].strip()

DATABASE_URL = f"mysql+pymysql://root:{_get_db_password()}@localhost/frentecaixa"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)