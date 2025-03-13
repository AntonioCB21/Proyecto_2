# Ciclo de vida del dato

## ¿Cómo maneja el software el ciclo de vida del dato?

El ciclo de vida del dato en AutoBackupScript se gestiona de la siguiente manera:

- **Creación**: El usuario define las carpetas y archivos a respaldar en el archivo de configuración.
- **Almacenamiento**: Los archivos son subidos automáticamente a Google Drive o Dropbox.
- **Uso y mantenimiento**: Se revisa periódicamente la existencia de archivos para evitar duplicados.
- **Retención y Eliminación**: Se pueden eliminar versiones antiguas de archivos tras un tiempo predefinido para optimizar el almacenamiento.

## ¿Qué estrategias se emplean para garantizar la consistencia e integridad de los datos?

- **Estrategia de versiones**: Se evita la sobreescritura de archivos y se mantiene un historial limitado de versiones.
- **Verificación de integridad**: Se usa hashing para comparar archivos antes de ser subidos, evitando corrupción de datos.
- **Sincronización programada**: La automatización reduce la posibilidad de errores humanos y asegura copias de seguridad consistentes.

## ¿Cómo podría incluirse una funcionalidad adicional de gestión de datos?

Se podría implementar una opción de **cifrado local** antes de subir los archivos a la nube, lo que aumentaría la seguridad de los datos. Además, podría agregarse una opción de **compresión** para optimizar el espacio de almacenamiento.

---

# Almacenamiento en la nube

## ¿Cómo garantiza el software la seguridad y disponibilidad de los datos en la nube?

- **Autenticación segura con OAuth2**: Solo el usuario con las credenciales correctas puede acceder a los archivos en la nube.
- **Subida automática a la nube**: Asegura la disponibilidad de los datos ante fallos o pérdidas.
- **Eliminación de versiones antiguas**: Permite gestionar el espacio de almacenamiento eficientemente.
- **Cifrado en la nube**: Aprovecha las medidas de seguridad de Google Drive y Dropbox.

## ¿Qué otras alternativas se consideraron para almacenar los datos?

- **Almacenamiento local**: Menos seguro ante fallos del hardware, por lo que se descartó.
- **Uso de servidores FTP/SFTP**: Descartado por la falta de integración sencilla con mecanismos de autenticación modernos y cifrado.
- **Amazon S3 o Google Cloud Storage**: Se considera para futuras versiones con mayor personalización y almacenamiento en la nube.

## ¿Cómo podría integrarse más con la nube en el futuro?

- **Sincronización** con otros servicios en la nube como OneDrive, AWS S3 o Azure Blob Storage.
- **Soporte para almacenamiento** en servidores FTP o NAS locales.
- **Cifrado extremo a extremo** antes de la carga en la nube para una mayor seguridad.

---

# Seguridad y regulación

## ¿Cómo garantiza el software la seguridad de los datos?

- **Autenticación con OAuth2**: Previene accesos no autorizados a Google Drive y Dropbox.
- **Manejo seguro de credenciales**: Configuración de credenciales en archivos locales protegidos.
- **Evita duplicaciones** para reducir el riesgo de inconsistencias en los datos almacenados.
- **Borrado seguro** de versiones antiguas para liberar espacio sin comprometer la seguridad de la información.

## ¿Cómo afecta la regulación de datos al proyecto?

- **Cumplimiento con GDPR**: Garantiza que los datos puedan eliminarse de manera permanente si el usuario lo solicita.
- **Reglamentos de seguridad en la nube**: Uso de autenticación y encriptación según los estándares de Google y Dropbox.
- **Evita el almacenamiento de datos sensibles** en servidores públicos sin protección.

## ¿Qué riesgos podrían surgir si no se considera la seguridad de los datos?

- **Acceso no autorizado**: Si no se protege adecuadamente, terceros podrían acceder a la información privada.
- **Exposición de datos sensibles** debido a vulnerabilidades en la autenticación.
- **Pérdida de datos** por una mala gestión de eliminaciones y versiones anteriores.

---

# Aplicación en IT y OT

## ¿Cómo mejora la integración entre IT y OT?

- **Automatización** de respaldos de datos operativos y administrativos.
- **Monitoreo en tiempo real**: Se podrían añadir alertas en caso de errores en la copia de seguridad.
- **Centralización del almacenamiento**: Mejora la interoperabilidad entre los sistemas de IT y OT mediante la sincronización de datos clave en la nube.

## ¿Qué procesos podrían mejorar con esta solución?

- **Gestores de redes y sistemas**: Automatización de respaldos, evitando la intervención manual constante.
- **Empresas de manufactura**: Respaldo automático de parámetros de máquinas y datos de sensores.
- **Profesionales remotos y freelancers**: Respaldo sencillo de documentos importantes en la nube sin depender de servicios complejos.

---

# Tecnologías Habilitadoras Digitales (THD)

## ¿Qué THD se han utilizado o se podrían incluir en el futuro?

- **Cloud Computing**: Se almacena la información de forma segura en la nube con Google Drive y Dropbox.
- **Automatización de procesos**: Uso de Schedule en Python para programar las copias de seguridad automáticas.
- **Ciberseguridad**: Protección de datos mediante protocolos seguros de autenticación (OAuth2) y cifrado en la nube.

## ¿Cómo podrían estas tecnologías mejorar el proyecto?

- **Machine Learning** para analizar los patrones de respaldo y predecir archivos importantes.
- **Blockchain** para garantizar la inmutabilidad de los archivos almacenados.
- **Computación en la Nube** para aumentar la escalabilidad y disponibilidad del servicio.
- **Automatización Avanzada** para optimizar el uso de recursos y mejorar la eficiencia del respaldo.
