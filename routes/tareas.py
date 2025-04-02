from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from crud import tareas as crud_tareas
from schemas.tarea import TareaCreate, TareaResponse
from typing import List

router = APIRouter()

# Dependencia para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear tarea
@router.post("/tareas/", response_model=TareaResponse)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crud_tareas.crear_tarea(db, tarea)

# Obtener todas las tareas
@router.get("/tareas/", response_model=List[TareaResponse])
def listar_tareas(db: Session = Depends(get_db)):
    return crud_tareas.obtener_tareas(db)

# Obtener tarea por ID
@router.get("/tareas/{id}", response_model=TareaResponse)
def obtener_tarea(id: int, db: Session = Depends(get_db)):
    tarea = crud_tareas.obtener_tarea(db, id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

# Actualizar tarea
@router.put("/tareas/{id}", response_model=TareaResponse)
def actualizar_tarea(id: int, tarea_actualizada: TareaCreate, db: Session = Depends(get_db)):
    tarea = crud_tareas.actualizar_tarea(db, id, tarea_actualizada)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

# Eliminar tarea
@router.delete("/tareas/{id}")
def eliminar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = crud_tareas.eliminar_tarea(db, id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada"}
