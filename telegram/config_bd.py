from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Определите параметры подключения к базе данных
DATABASE_URL = "postgresql://user:password@host:port/database_name"  # Замените на ваши значения

# 2. Создайте движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# 3. Создайте базовый класс для моделей
Base = declarative_base()

# Создание фабрики сессий
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
