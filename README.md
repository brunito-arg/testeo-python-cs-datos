# Proyecto de Análisis de Encuestas con Google Forms + FastAPI

## Descripción

Este proyecto permite obtener respuestas de encuestas realizadas mediante Google Forms, procesarlas con Python y exponer estadísticas a través de una API REST desarrollada con FastAPI.

Actualmente el backend permite:

- Leer respuestas desde Google Sheets.
- Procesar datos utilizando Pandas.
- Exponer endpoints REST.
- Consultar preguntas y estadísticas.
- Servir como base para futuros dashboards y gráficos web.

---

# Requisitos

- Python 3.14 o superior
- Git
- Acceso al repositorio

---

# Clonar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd testeo-python-cs-datos
```

---

# Crear entorno virtual

Desde la raíz del proyecto:

```bash
python -m venv .venv
```

Esto generará la siguiente estructura:

```text
testeo-python-cs-datos/
│
├── .venv/
├── backend/
└── ...
```

---

# Activar entorno virtual

## Windows CMD

```cmd
.venv\Scripts\activate
```

## Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Si todo salió correctamente debería verse algo similar a:

```text
(.venv) D:\Bruno\ciencia de datos\testeo-python-cs-datos>
```

---

# Instalar dependencias

Instalar todas las dependencias del proyecto:

```bash
python -m pip install -r requirements.txt
```

---

# Verificar instalación

```bash
python -m pip list
```

Deberían aparecer dependencias similares a:

```text
fastapi
uvicorn
pandas
matplotlib
numpy
```

---

# Ejecutar el backend

Ubicarse en la raíz del proyecto:

```bash
cd "D:\Bruno\ciencia de datos\testeo-python-cs-datos"
```

Levantar el servidor FastAPI:

```bash
uvicorn backend.main:app --reload
```

Si todo funciona correctamente se verá:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Probar la API

## Endpoint principal

Abrir en el navegador:

```text
http://127.0.0.1:8000
```

Respuesta esperada:

```json
{
    "mensaje": "Backend funcionando"
}
```

---

## Documentación automática de FastAPI

Abrir:

```text
http://127.0.0.1:8000/docs
```

Swagger permitirá probar todos los endpoints desde el navegador.

---

## Consultar preguntas disponibles

```text
http://127.0.0.1:8000/preguntas
```

Respuesta esperada:

```json
[
    "¿Estás feliz?",
    "Edad",
    "Carrera"
]
```

---

# Actualizar dependencias

Si se instala una nueva librería:

```bash
python -m pip install nombre_paquete
```

Actualizar el archivo de dependencias:

```bash
python -m pip freeze > requirements.txt
```

Subir posteriormente los cambios al repositorio.

---

# Estructura del proyecto

```text
testeo-python-cs-datos/

├── .venv/
│
├── backend/
│   ├── main.py
│   │
│   └── services/
│       ├── analisis_encuestas.py
│       └── sheets_service.py
│
├── requirements.txt
│
└── README.md
```

---

# Flujo de funcionamiento

```text
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
      ▼
API REST
      │
      ▼
Frontend (próxima etapa)
```

---

# Desarrollo futuro

- Dashboard web con React.
- Gráficos dinámicos.
- Filtros de encuestas.
- Exportación a PDF.
- Análisis estadístico avanzado.
- Actualización automática de datos desde Google Forms.
