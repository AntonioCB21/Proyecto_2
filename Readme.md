# Proyecto: AutoBackupScript

## 1. Descripción General
**AutoBackupScript** es un software sencillo en **Python** que permite realizar copias de seguridad automáticas de archivos y carpetas en la nube. Se enfoca en ser una herramienta fácil de usar y de bajo mantenimiento, ideal para usuarios que necesitan hacer respaldos sin complicaciones.

El usuario solo debe definir una carpeta o archivos específicos, y el script se encargará de:

- Subir los archivos a **Google Drive** o **Dropbox**.
- **Evitar duplicados** al comprobar si un archivo ya existe en la nube.
- **Eliminar versiones antiguas** para evitar ocupar espacio innecesario.
- **Ejecutarse de forma automática** a intervalos definidos.

---

## 2. Objetivos del Proyecto
- **Diseñar y desarrollar un software funcional y operativo** que realice copias de seguridad en la nube.
- **Aplicar conceptos clave** como:
  - **Ciclo de vida del dato:** Creación, almacenamiento y eliminación de archivos antiguos.
  - **Seguridad:** Uso de credenciales OAuth2 para autenticación en la nube.
  - **Almacenamiento en la nube:** Uso de API de Google Drive y Dropbox para gestionar archivos.
- **Reflexionar sobre el impacto de las tecnologías habilitadoras digitales (THD)**, en especial en la gestión de datos en la nube.

---

## 3. Funcionalidades del Software
- **Copia de seguridad automática:** Se ejecuta de manera programada (por ejemplo, cada día o semana).
- **Compatibilidad con múltiples servicios en la nube:** Inicialmente, **Google Drive y Dropbox**.
- **Gestión inteligente de archivos:**
  - Evita subir **archivos duplicados**.
  - Permite configurar qué **archivos o carpetas** respaldar.
  - **Borra copias antiguas** después de cierto tiempo (configurable).
- **Interfaz sencilla:**
  - Configuración fácil a través de un archivo `.ini` o `.json`.
  - Puede ejecutarse desde la **línea de comandos** con un simple comando.

---

## 4. Implementación Técnica
- **Lenguaje:** Python
- **Librerías:**
  - `pydrive2` → Para interactuar con **Google Drive**.
  - `dropbox` → Para interactuar con **Dropbox**.
  - `schedule` → Para programar la ejecución automática.
  - `os` y `shutil` → Para manejar archivos y carpetas.
- **Funcionamiento:**
  1. El usuario ejecuta el script y **configura las credenciales de acceso**.
  2. Define las carpetas y archivos a respaldar en un **archivo de configuración**.
  3. El script escanea los archivos y **los sube si no están en la nube**.
  4. Se programa para ejecutarse automáticamente según la configuración del usuario.

---

## 5. Beneficios y Diferenciación
✔ **Simple y ligero** → No requiere instalación compleja ni interfaces gráficas.  
✔ **Automático** → Funciona en segundo plano sin intervención manual.  
✔ **Seguro** → Usa autenticación oficial de Google y Dropbox (**OAuth2**).  
✔ **Open Source** → Puede ser modificado y mejorado por la comunidad.  

---

## 6. Ejemplo de Uso
1. **Descargas** el script.  
2. **Configuras** qué archivos o carpetas quieres respaldar en un archivo **JSON**.  
3. **Ejecutas** el script o lo programas con `cron` (Linux) o **Task Scheduler** (Windows).  
4. El script **sube los archivos** y **borra versiones antiguas** si es necesario.

---

## ¿Por qué AutoBackupScript es diferente?

- **No requiere instalación complicada ni interfaces gráficas.**  
- **Se ejecuta desde un simple script en Python**, pensado para usuarios que solo quieren respaldar archivos con el menor esfuerzo posible.  
- **Elimina archivos antiguos automáticamente**, cosa que la mayoría de herramientas no hacen sin configuraciones avanzadas.  
- **Es un proyecto Open Source minimalista**, pensado para ser modificado fácilmente.  
