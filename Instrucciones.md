# AutoBackupScript

## 📌 Descripción  
AutoBackupScript es una herramienta simple en **Python** para realizar copias de seguridad automáticas de archivos en **Google Drive** y **Dropbox**. Se ejecuta en segundo plano, subiendo archivos y eliminando versiones antiguas automáticamente.  

## 🚀 Requisitos  
- Python 3  
- Librerías: `pydrive2`, `dropbox`, `schedule`  
- Cuenta en Google Drive o Dropbox  

## 📦 Instalación  
1. Clona este repositorio:  
   ```bash
   git clone https://github.com/tuusuario/AutoBackupScript.git
   cd AutoBackupScript

2. Instala las dependencias:  
pip install pydrive2 dropbox schedule

3. Configuración:  
Edita el archivo ``config.json`` para configurar los archivos que deseas respaldar y los servicios en la nube.

4. Ejecución:  
Para ejecutar el script usa: python autobackup.py

5. Programación automática:  
Para ejecutar el script automáticamente cada cierto tiempo, puedes usar:  
* Windows: Configurar con Task Scheduler
* Linux/macOS: Agregar al crontab
