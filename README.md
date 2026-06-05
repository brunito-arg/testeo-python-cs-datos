# Visualizador de Encuesta (Streamlit)

Instrucciones para ejecutar localmente:

1. Clona el repositorio y entra a la carpeta del proyecto:

```bash
git clone <tu-repo.git>
cd d:\Bruno\ciencia de datos\testeo-python-cs-datos
```

2. Crea y activa un entorno virtual:

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta la app desde la carpeta correcta:

```bash
cd "d:\Bruno\ciencia de datos\testeo-python-cs-datos"
streamlit run streamlit_app.py
```

   O ejecuta directamente con la ruta completa:

```bash
streamlit run "d:\Bruno\ciencia de datos\testeo-python-cs-datos\streamlit_app.py"
```

5. Abre en el navegador: `http://localhost:8501`

Notas:
- Requiere Python 3.8+.
- Si la URL del Google Sheet no es accesible, reemplaza `url` en `streamlit_app.py` por el CSV local.
- Para desactivar telemetría de Streamlit, crea `%USERPROFILE%/.streamlit/config.toml` con:

```toml
[browser]
gatherUsageStats = false
```
