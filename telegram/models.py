from config_bd import Base
from sqlalchemy import Column, Integer, Date, String, ForeignKey


class User(Base):
    __tablename__ = "users"  # Имя таблицы

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"