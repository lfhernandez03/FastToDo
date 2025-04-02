from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a SQLite
DATABASE_URL = "sqlite:///./tareas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de datos SQLAlchemy
Base = declarative_base()
