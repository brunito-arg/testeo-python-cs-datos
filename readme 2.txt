Ejecutar el backend
1. Abrir una terminal

Ubicarse en la raíz del proyecto:

cd "D:\Bruno\ciencia de datos\testeo-python-cs-datos"
2. Activar el entorno virtual
Windows CMD
.venv\Scripts\activate
Windows PowerShell
.\.venv\Scripts\Activate.ps1

La terminal debería mostrar algo similar a:

(.venv) D:\Bruno\ciencia de datos\testeo-python-cs-datos>
3. Verificar el entorno (opcional)
where python

La primera ruta debe ser:

D:\Bruno\ciencia de datos\testeo-python-cs-datos\.venv\Scripts\python.exe
4. Ejecutar FastAPI
python -m uvicorn backend.main:app --reload

Si todo funciona correctamente se verá:

INFO:     Uvicorn running on http://127.0.0.1:8000
Verificar funcionamiento
API principal

Abrir:

http://127.0.0.1:8000

Respuesta esperada:

{
    "mensaje": "Backend funcionando"
}
Listar preguntas de la encuesta

Abrir:

http://127.0.0.1:8000/preguntas

Respuesta esperada:

[
    "¿Estás feliz?",
    "Edad",
    "Carrera"
]
Obtener estadísticas de una pregunta

Desde Swagger:

http://127.0.0.1:8000/docs

Seleccionar:

GET /estadisticas/{pregunta}

Ejemplo de respuesta:

{
    "SI": 3,
    "NO": 1
}
Flujo actual del sistema
Google Forms
      │
      ▼
Google Sheets
      │
      ▼
Pandas
      │
      ▼
FastAPI
      │
      ├── GET /preguntas
      │
      └── GET /estadisticas/{pregunta}