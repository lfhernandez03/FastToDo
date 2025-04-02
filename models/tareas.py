from sqlalchemy import Column, Integer, String, Date
from database.db import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    fecha_limite = Column(Date, nullable=True)
    estado = Column(String, default="pendiente")