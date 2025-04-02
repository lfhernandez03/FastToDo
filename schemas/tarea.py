from pydantic import BaseModel
from typing import Optional
from datetime import date

class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    fecha_limite: Optional[date] = None
    estado: str

class TareaCreate(TareaBase):
    pass

class TareaResponse(TareaBase):
    id: int

    class Config:
        from_attributes = True
