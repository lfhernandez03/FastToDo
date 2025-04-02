from fastapi import FastAPI
from routes.tareas import router as tareas_router
from database.db import engine, Base

app = FastAPI()

# Crear la base de datos
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(tareas_router)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a FastToDo!, accede a /docs para ver la documentación de la API."}
