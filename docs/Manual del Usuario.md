# 🎬 **Manual de Usuario**
## **Sistema de Cine – Lúmen Cinema Universitario UdeA**

---

## 📖 **Descripción General**

Este sistema permite a los usuarios registrarse, reservar asientos, consultar y cancelar reservas, así como visualizar la cartelera del fin de semana del Lúmen Cinema Universitario UdeA.  
Además, incluye un módulo administrativo de uso restringido.

---

# 🧑‍💼 **1. Registro de Usuario**

Para registrarse, el usuario debe ingresar:

- **Nombre** (solo letras, mínimo 3 caracteres)
- **Apellido** (solo letras, mínimo 3 caracteres)
- **Documento** (entre 3 y 15 dígitos)
- **Tipo de vínculo**, escrito *exactamente* como aparece y con **Mayúscula inicial obligatoria**  

### Tipos válidos:
- Estudiante  
- Docente  
- Administrativo  
- Oficial interno  
- Público externo  

Si alguno de estos datos está mal digitado, el sistema mostrará un mensaje de error y no permitirá continuar.

---

# 🎟️ **2. Registrar Reserva**

Para reservar una función:

1. Debe estar previamente registrado.  
2. Debe seleccionar la función **solo digitando el número ID** que aparece en el listado.  
3. Ingresar cuántos asientos desea reservar.  
4. Ingresar cada asiento usando el formato **LetraNúmero** (ejemplo: `C7`, `A3`, `K10`).  

Si un asiento está ocupado o no existe, el sistema avisará y pedirá ingresarlo nuevamente.

### ✔ La factura muestra:
- Película  
- Fecha y hora  
- Asientos seleccionados  
- Precio total según tipo de vínculo  
- **Código único de reserva** (necesario para cancelar)

> Si ocurre un error durante la selección, el sistema realiza *rollback* y libera los asientos ya tomados.

---

# 🔍 **3. Consultar Mis Reservas**

El usuario ingresa su documento y el sistema muestra:

- Código de reserva  
- Película  
- Fecha  
- Asientos reservados  

Este código es necesario si desea cancelar la reserva.

---

# ❌ **4. Cancelar Reserva**

Para cancelar una reserva:

1. Ingrese a **“Cancelar Reserva”**  
2. Digite su documento  
3. Ingrese el **código de reserva** (consultable en “Mis Reservas”)  

El sistema liberará los asientos y eliminará la reserva del registro.

---

# 📅 **5. Consultar Funciones**

Muestra la cartelera completa con:

- Número ID de función (para seleccionar)  
- Día  
- Hora  
- Película  
- Asientos disponibles  

### 🎭 **Cartelera**

**Sábado**
1. 10:00 — *Wicked: Por Siempre*  
2. 13:00 — *Avatar: Fuego y Ceniza*  
3. 16:00 — *Midsommar*

**Domingo**
4. 10:00 — *Eterno resplandor de una mente sin recuerdos*  
5. 13:00 — *Wicked: Por Siempre*

> Para seleccionar la película debe ingresar únicamente el **número ID**.

---

# 🪑 **6. Mapa de Sala**

- Filas: **A–K**
- Columnas: **1–11**
- Total: **121 asientos**
- `O` = Disponible  
- `X` = Ocupado  

La pantalla del cine se ubica frente a la **Fila A**.

---

# 🔧 **7. Panel del Administrador (Opción 6)**

Uso restringido.  
Credenciales por defecto:

- **Usuario:** `admin`  
- **Contraseña:** `1234`  

Funciones del administrador:

- Ver lista de usuarios registrados  
- Ver reservas realizadas  
- Ver ocupación de la sala por función  

---

# ⚠️ **Solución de Problemas**

| Mensaje | Significado | Solución |
|--------|-------------|----------|
| Documento inválido | No cumple 3–15 dígitos | Ingrese un documento válido |
| Tipo de vínculo inválido | No tiene mayúscula inicial o no existe | Escríbalo exactamente como aparece |
| Función inválida | No digitó un número válido | Seleccione solo el número ID |
| Asiento inválido | Formato incorrecto | Use formato LetraNúmero (A5, C8…) |
| Usuario no encontrado | No está registrado | Complete el registro |

---

# 💡 **Recomendaciones**

- Verifique la cartelera antes de reservar.  
- Use siempre el formato correcto para asientos.  
- Conserve su **código de reserva**.  
- Si no recuerda su código, consulte “Mis Reservas”.

---

# 🎥 **¡Gracias por usar el sistema del Lúmen Cinema Universitario UdeA!**








