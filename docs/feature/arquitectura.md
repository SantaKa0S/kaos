# Arquitectura

## Diagrama de la infraestructura

La arquitectura se compone de los siguientes componentes:
- Servidor web: Utiliza Apache como servidor web y MySQL como base de datos.
- Base de datos: Utiliza MySQL como base de datos para almacenar la información del sistema.
- Servicio de correo electrónico: Utiliza Postfix como servicio de correo electrónico.

La relación entre estos componentes se establece a través de los siguientes servicios:
- Servicio de API: Permite la comunicación entre los diferentes componentes y servicios.
- Servicio de autenticación: Permite la autenticación de los usuarios y la autorización de las acciones.

**Diagrama de la infraestructura**

[Insertar diagrama de la infraestructura]

## Documentación funcional

La documentación funcional se divide en dos partes:
- **Flujos de Trabajo**: Describen el flujo de trabajo para cada servicio y componente.
- **Transformaciones de Datos**: Describen las transformaciones de datos que se realizan entre los diferentes componentes y servicios.

**Flujo de Trabajo**

1. El usuario envía una solicitud al servicio de API.
2. El servicio de API verifica la autenticación del usuario y autoriza la acción.
3. El servicio de API llama a los servicios de base de datos para obtener la información necesaria.
4. El servicio de base de datos devuelve la información solicitada.
5. El servicio de API procesa la información y devuelve el resultado al usuario.

**Transformaciones de Datos**

1. La solicitud del usuario se convierte en un formato de datos que puede ser procesado por el servicio de API.
2. El servicio de API convierte los datos en un formato que pueda ser utilizado por los servicios de base de datos.
3. Los servicios de base de datos convierten los datos en un formato que pueda ser utilizado por el usuario.

**Configuracion Redes**

La configuración de redes se divide en tres partes:
- **Red de Servidores**: Describen la configuración de la red de servidores.
- **Red de Base de Datos**: Describen la configuración de la red de base de datos.
- **Red de Correo Electrónico**: Describen la configuración de la red de correo electrónico.

**Red de Servidores**

| Protocolo | Tecnología | IP |
| --- | --- | --- |
| HTTP | Apache | 192.168.1.100 |
| FTP | vsftpd | 192.168.1.101 |

**Red de Base de Datos**

| Protocolo | Tecnología | IP |
| --- | --- | --- |
| MySQL | MariaDB | 192.168.1.102 |

**Red de Correo Electrónico**

| Protocolo | Tecnología | IP |
| --- | --- | --- |
| SMTP | Postfix | 192.168.1.103 |

## Información de Contacto

La información de contacto se divide en tres partes:
- **Contactos Técnicos**: Describen los contactos técnicos del equipo.
- **Servicio al Cliente**: Describen el servicio al cliente y cómo obtener ayuda adicional.

**Contactos Técnicos**

| Nombre | Correo electrónico | Teléfono |
| --- | --- | --- |
| Juan Pérez | juan.perez@example.com | 555-1234 |
| María García | maria.garcia@example.com | 555-5678 |

**Servicio al Cliente**

* Horario de atención: Lunes a viernes, 9am - 5pm
* Formas de comunicación:
	+ Correo electrónico: [info@example.com](mailto:info@example.com)
	+ Teléfono: 555-9012

Revisión y Actualización:

La documentación se revisa y actualiza periódicamente para garantizar su relevancia y eficacia. La fecha de la próxima revisión es: [Insertar fecha].

Versión del documento: [Insertar versión]
Fecha de creación: [Insertar fecha]