from sqlalchemy.orm import Session
from models.tareas import Tarea
from schemas.tarea import TareaCreate

def crear_tarea(db: Session, tarea: TareaCreate):
    nueva_tarea = Tarea(**tarea.dict())
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def obtener_tareas(db: Session):
    return db.query(Tarea).all()

def obtener_tarea(db: Session, tarea_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea_actualizada: TareaCreate):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        for key, value in tarea_actualizada.dict().items():
            setattr(tarea, key, value)
        db.commit()
        db.refresh(tarea)
    return tarea

def eliminar_tarea(db: Session, tarea_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        db.delete(tarea)
        db.commit()
    return tarea
