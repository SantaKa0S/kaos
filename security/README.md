# Security Module

El modulo de seguridad, que dentro de la solución core se incorporá, es el proyecto de trivy en su version inicial de v0.59.
Toda la información de su personalización y detalles del funcionamiento dentro de Ka0s estara explicado en este documento y referenciado a los documentos pertienetes dentro de la estructura del directorio.

## La imagen: el origen de todo

En la carpeta core/config/trivy/ localizamos el fichero Dockerfile que se usa de base para la gestión interna del escaneado de código del repositorio de Ka0s. Hay que tener en cuenta que este es un runner personalizado para la solución core de Ka0s, aplicarlo en cualquier otra infraestructura empresarial necesitará de la evaluación y modificacion del mismo, bajo demanda.
