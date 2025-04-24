import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# 1. Определите параметры подключения к базе данных
DATABASE_URL = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
# 2. Создайте движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# 3. Создайте базовый класс для моделей
Base = declarative_base()

# Создание фабрики сессий
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DATABASE_URL = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
