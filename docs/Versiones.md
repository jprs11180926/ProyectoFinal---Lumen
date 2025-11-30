# Plan de Versionado – Lúmen Cinema Universitario UdeA

A continuación, se describen los avances del proyecto desde su inicio hasta la entrega final, indicando las versiones desarrolladas y los cambios realizados en cada una:

---

### **Día 1 – Versión 0.1**
Se definió el alcance del sistema, se creó el archivo principal en Python y se configuraron las constantes iniciales:  
nombre del cine, precios por tipo de usuario y lista preliminar de funciones.

---

### **Día 4 – Versión 0.2**
Se implementaron las clases `Usuario` y `Reserva` utilizando `@dataclass`.  
Se creó el módulo de **registro de usuarios**, incluyendo validaciones de nombre, apellido, documento y tipo de vínculo.

---

### **Día 8 – Versión 0.3**
Se diseñó la estructura del **sistema de asientos**, definiendo filas, columnas y la matriz de disponibilidad para cada función del fin de semana.  
Se agregó la visualización completa con símbolos (O/X).

---

### **Día 12 – Versión 0.4**
Se añadieron funciones internas clave:  
- Validación del asiento ingresado  
- Verificación de disponibilidad  
- Cambio de estado (O → X)  
- Cálculo total de asientos libres  

---

### **Día 16 – Versión 0.5**
Se programó el módulo de **registro de reservas**, permitiendo:  
- Seleccionar la película  
- Elegir cantidad de asientos  
- Validar su disponibilidad  
- Registrar la reserva con fecha y hora del sistema  

---

### **Día 20 – Versión 0.6**
Se desarrolló el sistema de **generación de factura**, incluyendo:  
- Código único de reserva  
- Encabezado institucional  
- Lista de asientos seleccionados  
- Valor total según tipo de usuario  

Formato estilizado similar a una boleta real del cine.

---

### **Día 25 – Versión 0.7**
Se añadió el módulo de **consulta de funciones**, mostrando:  
- Cartelera del fin de semana  
- Número total de funciones  
- Películas únicas  
- Tabla con día, hora, película y disponibilidad  

---

### **Día 32 – Versión 0.8**
Se construyó el **menú principal** con arte ASCII, integrando todas las opciones:  
Registrar usuario, registrar reserva, cancelar reserva, consultar funciones y administrador.

---

### **Día 38 – Versión 0.9**
Se implementó el módulo de **administrador**, con validación de credenciales.  
Se inició la estructura de cancelación de reservas.  
Se mejoró la organización general del código y la legibilidad.

---

### **Día 45 – Versión 1.0**
Se realizaron pruebas completas del sistema, ajustes menores, depuración del funcionamiento interno y validación de todos los módulos.  
El sistema quedó finalizado, estable y listo para entrega.

---
