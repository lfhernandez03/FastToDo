# FastToDo - API REST con FastAPI

FastToDo es una API RESTful desarrollada con **FastAPI** que permite gestionar tareas a través de operaciones CRUD (Create, Read, Update, Delete). Utiliza **SQLite** como base de datos y proporciona documentación automática con **Swagger UI**.

## 🚀 Características
- 📌 Creación, lectura, actualización y eliminación de tareas.
- 🗄️ Base de datos SQLite para almacenamiento de datos.
- 🔍 Documentación automática con Swagger UI y ReDoc.
- ⚡ Rápida y optimizada gracias a FastAPI.

## 📂 Instalación y Configuración
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/FastToDo.git
cd FastToDo
```

### 2️⃣ Crear y activar entorno virtual (opcional pero recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install fastapi uvicorn sqlalchemy
```

### 4️⃣ Ejecutar la API
```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`

## 📝 Endpoints
| Método  | Endpoint         | Descripción                |
|---------|----------------|----------------------------|
| POST    | `/tareas/`     | Crear una nueva tarea      |
| GET     | `/tareas/`     | Listar todas las tareas    |
| GET     | `/tareas/{id}` | Obtener una tarea por ID   |
| PUT     | `/tareas/{id}` | Actualizar una tarea       |
| DELETE  | `/tareas/{id}` | Eliminar una tarea         |

## 📖 Documentación
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📡 Despliegue en la Nube
Puedes desplegar esta API en servicios gratuitos como:
- Render
- Railway
- Google Cloud Run
- Azure App Service

## 🔧 Mejoras Futuras
- ✅ Autenticación con JWT.
- ✅ Integración con PostgreSQL o MongoDB.
- ✅ Implementación de tests automatizados.

---
💡 **Creado con FastAPI 🚀 por Luis Fernando Hernández Solís**

