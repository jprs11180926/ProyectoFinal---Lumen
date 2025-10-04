# Lúmen
Lúmen - Cinema Universitario UdeA

## Integrantes

### Juan Pablo Restrepo Salazar
- **Descripción**: Un narrador visual. Mi pasión por el cómic, el cine y la cultura geek se fusiona con mi habilidad para el dibujo y la pintura. En el piano encuentro la banda sonora perfecta para mi creatividad.
- **Programa académico**: Ingeniería Industrial.
- **Habilidades**: Investigación, escritura, uso de recursos académicos, diseño de material gráfico, habilidad con programas de diseño.
- **Fortalezas**: Trabajo en equipo, colaboración, comunicación, análisis y pensamiento lógico, organización y planificación.

### Yoher Alberto Castaño Morales
- **Descripción**:
- **Programa académico**: Ingeniería Industrial
- **Habilidades**: Programación básica, análisis, asertividad.
- **Fortalezas**: Resolución de conflictos, adaptabilidad, organización y planificación.

### Dair Manuel Martinez Arrieta
- **Descripción**: Profesional comprometido y resolutivo. Mi energía positiva y mi habilidad para el trabajo en equipo impulsan cada proyecto, guiado siempre por un principio de mejora continua.
- **Programa académico**: Ingeniería Industrial.
- **Habilidades**: Redacción de textos, toma de decisiones.
- **Fortalezas**: Autonomía, autodisciplina, capacidad de organización y gestión del tiempo.

## Licencia del software
<a href="https://github.com/jprs11180926/ProyectoFinal---L-men-Cinema/blob/main/README.md">Lúmen - Cinema</a> © 2025 by <a href="https://github.com/jprs11180926">Juan Pablo Restrepo</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">

## Nombre del proyecto y detalles

### Lúmen - Cinema Universitario
Lúmen - Cinema Universitario UdeA es el sistema de gestión integral para el espacio cinematográfico de la Universidad de Antioquia. El nombre "Lúmen" proviene del latín y significa "luz", haciendo referencia tanto a la luz del proyector cinematográfico como a la luz del conocimiento que caracteriza a nuestra Alma Mater. 

Desarrollado por estudiantes de Ingeniería Industrial de la UdeA, este programa de consola en Python permite administrar de manera eficiente las reservas de películas, gestionar diferentes tipos de usuarios de la comunidad universitaria y generar reportes administrativos completos. 

<div align="center">
  <img src="https://github.com/jprs11180926/ProyectoFinal---Lumen/blob/main/L%C3%BAmen%201.png?raw=true" alt="Lúmen - Cinema Universitario UdeA" style="width: 65%; max-width: 500px">
</div>

## Reporte de visión
Lúmen - Cinema Universitario UdeA nace como respuesta a la necesidad de la Universidad de Antioquia de ofrecer espacios de entretenimiento cultural accesibles para su comunidad. Este sistema de gestión busca modernizar y automatizar el proceso de reserva y administración del espacio cinematográfico universitario, llevando luz tanto a la pantalla como a la experiencia del usuario. 

### Objetivos del Software

#### Objetivo General
Desarrollar un sistema de gestión cinematográfica que permita a la comunidad universitaria de la UdeA reservar asientos de manera intuitiva, mientras proporciona a los administradores herramientas analíticas para la toma de decisiones sobre el cinema universitario.

#### Objetivos Específicos
- Implementar un sistema de registro de usuarios con validaciones robustas que garantice la integridad de los datos de la comunidad UdeA
- Crear una interfaz de consola amigable que facilite la visualización y selección de los 121 asientos disponibles
- Automatizar el proceso de facturación con precios diferenciados según el tipo de vinculación universitaria
- Generar reportes administrativos que permitan analizar el desempeño financiero y operativo del cinema universitario
- Exportar información relevante en formato CSV para análisis posteriores

### Beneficios

#### Para los Usuarios de la Comunidad UdeA
- Acceso rápido y sencillo a la cartelera del fin de semana
- Selección visual e intuitiva de asientos
- Precios preferenciales según vinculación universitaria
- Facturación instantánea y clara

#### Para los Administradores del Cinema
- Reportes en tiempo real sobre ventas e ingresos
- Estadísticas de uso y preferencias de usuarios
- Información organizada para toma de decisiones
- Exportación de datos para análisis avanzados

#### Para la Universidad de Antioquia
- Fortalecimiento de la oferta cultural institucional
- Gestión eficiente de recursos del cinema
- Mayor integración de la comunidad universitaria
- Proyecto desarrollado por estudiantes que aplica conocimientos de ingeniería

## Especificación de requisitos

### Requisitos funcionales
- El sistema es capaz de registrar usuarios de la comunidad UdeA con nombre, apellido, documento y tipo de vinculación
- Valida la entrada correcta de datos, como longitud mínima, formato alfabético y numérico en los campos correspondientes
- Consulta y muestra la cartelera de películas del fin de semana con disponibilidad de asientos
- Permite la selección visual de asientos entre los 121 disponibles y gestiona su disponibilidad
- Calcula automáticamente precios diferenciados según el tipo de vinculación universitaria
- Genera facturas detalladas con información de la reserva y datos del usuario
- Genera reportes administrativos con estadísticas de ventas, ingresos y comportamiento de usuarios
- Exporta datos relevantes a formato CSV para análisis posteriores
- Permite a los usuarios cancelar reservas activas y liberar los asientos correspondientes

### Requisitos no funcionales
- El sistema es visualmente amigable al usuario, con interfaz de consola intuitiva y opciones bien estructuradas
- Responde en menos de 2 segundos para operaciones básicas y muestra los 121 asientos de forma instantánea
- Es compatible con Python 3.8+ y funciona en Windows, Linux y macOS sin dependencias externas
- Asegura la seguridad de los datos mediante autenticación administrativa y validación robusta de entradas
- Maneja errores de forma elegante con mensajes descriptivos y previene estados inconsistentes
- Utiliza programación orientada a objetos con código modular y mantenible siguiendo estándares PEP 8
- Protege la información personal de los usuarios de la comunidad universitaria en todas las operaciones
