import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"


# Создаем движок SQLAlchemy
engine = create_engine(db_url)

# Создаем сессию
Session = sessionmaker(bind=engine)

def get_session():
    """Возвращает новую сессию SQLAlchemy."""
    return Session()