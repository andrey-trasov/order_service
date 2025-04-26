from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

Base = declarative_base()

metadata = MetaData()

class User(Base):
    __tablename__ = 'user_user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50), unique=True, nullable=True)
    token = Column(String(100), nullable=True)
    tg_id = Column(Integer, unique=True, nullable=True)
    # Добавьте другие поля из вашей модели User
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    last_login = Column(DateTime)
    password = Column(String(128))

    def __repr__(self):
        return f"<User(email='{self.email}')>"
