# ✅ Pasos para probar que funciona correctamente

## 1. Instalar Python (si no lo tienes)
* Descarga e instala Python 3 desde [python.org](https://www.python.org). Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

## 2. Instalar dependencias necesarias
* Abre una terminal o línea de comandos en la carpeta del proyecto y ejecuta:
```bash
pip install pydrive2 dropbox schedule
```

## 3. Configurar credenciales en `config.json`
* Modifica el archivo `config.json` y agrega las rutas de los archivos/carpetas que deseas respaldar.  
* Si usas **Google Drive**: Debes configurar [Google Drive API](https://developers.google.com/drive) y descargar las credenciales JSON. Guía de configuración.  
* Si usas **Dropbox**: Obtén un [Access Token](https://www.dropbox.com/developers/apps/create) desde Dropbox App Console y agrégalo al archivo `config.json`.

## 4. Ejecutar el script de copia de seguridad
* Una vez configurado `config.json`, ejecuta el script:
```bash
python auto_backup_script.py
```
* Se subirán los archivos y se eliminarán las versiones antiguas según la configuración.

## 5. Automatizar la ejecución

### En Windows:
1. Abre el "Programador de tareas".
2. Crea una nueva tarea.
3. Configura el programa `python` y el archivo `auto_backup_script.py` como script a ejecutar.
4. Programa la tarea para que se ejecute a la frecuencia deseada.

### En Linux/macOS:
1. Abre la terminal y ejecuta `crontab -e`.
2. Agrega esta línea para ejecutarlo cada día a las 2 AM:

```bash
0 2 * * * /usr/bin/python3 /ruta-completa/auto_backup_script.py
```

## 🚨 Notas importantes

### ✔ Google Drive:
* Debes habilitar la **Google Drive API** y generar credenciales JSON desde [Google Cloud Console](https://console.cloud.google.com/). Luego, descarga el JSON y reemplázalo en tu carpeta del proyecto.

### ✔ Dropbox:
* Si usas **Dropbox**, debes generar un **Access Token** desde [Dropbox Developer](https://www.dropbox.com/developers/apps/create).

### ✔ Verifica las credenciales:
* Si usas **Google Drive**, asegúrate de configurar correctamente la autenticación **OAuth**.

