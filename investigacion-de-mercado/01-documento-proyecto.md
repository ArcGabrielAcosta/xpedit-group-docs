# Xpedit Group

## Documento de presentación del proyecto

**Versión:** 1.0  
**Fecha:** septiembre 2026  
**Clasificación:** documento interno de presentación  
**Fuente de diseño:** archivo Figma *Branding* — Manual de Sistema Visual y Directrices de Marca  

---

## 1. Resumen ejecutivo

**Xpedit Group** es una plataforma de *digital health-tech* orientada a Argentina que conecta, de forma inteligente y en tiempo real, una emergencia médica con la infraestructura de ambulancias y clínicas autorizadas según la cobertura del afiliado (obra social o prepaga).

Su promesa institucional es:

> **Donde corresponde, cuando importa.**

El producto digitaliza y automatiza el despacho de urgencias: elimina la triangulación ineficiente entre el usuario, la línea pública de emergencias y el prestador privado, y deriva al paciente hacia el servicio que realmente le corresponde por convenio.

Este documento presenta el problema, la solución, el funcionamiento del producto, el impacto por actor del ecosistema y los fundamentos de identidad de marca definidos en la etapa inicial de branding.

---

## 2. El problema

En Argentina, el ecosistema de salud está fragmentado. Ante una emergencia médica conviven:

- la línea pública **107 / 911**;
- las **obras sociales** y **prepagas**;
- los servicios de **ambulancia privados** y centros asistenciales con convenio.

El protocolo habitual —llamar primero al 107— suele introducir demoras y desvíos cuando el paciente ya cuenta con cobertura privada. El resultado es pérdida de tiempo, fricción operativa y, en muchos casos, derivaciones incorrectas.

### 2.1. Dolores principales

| Problema | Descripción |
|---|---|
| **Triangulación ineficiente** | Llamar a un número genérico puede implicar esperas prolongadas mientras se identifica qué ambulancia de la cartilla está disponible. |
| **Rechazos por falta de convenio** | Llegar a un centro que no corresponde a la cobertura genera deudas, traslados adicionales o riesgo clínico. |
| **Ubicación imprecisa** | Explicar la ubicación en vía pública o rutas durante una crisis consume minutos críticos; la aproximación por antenas suele fallar. |
| **Congestión del sistema público** | Casos que podrían resolverse por cobertura privada terminan sobrecargando la red 107/911. |

En una emergencia, **el tiempo es vital** y **la atención correcta también**.

---

## 3. La solución: Xpedit

Xpedit actúa como **canal de conexión** entre la emergencia y el prestador que corresponde.

No reemplaza la atención médica: **ordena, acelera y precisa** el acceso a ella.

### 3.1. Propuesta de valor

- Activación rápida desde el dispositivo del usuario.
- Confirmación explícita antes de enviar cualquier alerta.
- Envío de datos clínicos esenciales y ubicación GPS.
- Derivación automática según reglas de cobertura (obra social / prepaga).
- Seguimiento del estado de la asistencia.

### 3.2. Claim de apoyo

*Conexión médica instantánea cuando cada segundo cuenta.*

### 3.3. Mensaje institucional

> Xpedit Group optimiza el tiempo de respuesta médica automatizando el triage y la derivación para garantizar que cada paciente reciba atención exacta, donde corresponde, cuando importa.

---

## 4. Cómo funciona el producto

El flujo se resume en tres pasos.

### Paso 1 — Triple pulsación y confirmación

Tres pulsaciones del botón de bloqueo abren una ventana en pantalla bloqueada. El usuario debe **deslizar para confirmar**; solo entonces se envía la alerta.

- Una pulsación adicional **cancela** la ventana.
- Sin acción, la ventana **desaparece a los 10 segundos**.
- **Sin confirmación, no se envía ninguna alerta.**

Este diseño prioriza seguridad operativa y reduce falsas alarmas.

### Paso 2 — Envío de datos y ubicación

Tras la confirmación se despacha un paquete cifrado con:

- datos biomédicos esenciales (por ejemplo grupo sanguíneo y alergias);
- información de cobertura / afiliación;
- contacto de emergencia;
- coordenadas GPS en tiempo real.

### Paso 3 — Derivación coordinada

Un motor de reglas de cobertura dirige la alerta únicamente a la flota de ambulancias y clínicas autorizadas con convenio activo. El usuario puede ver el prestador confirmado y el estado del traslado (por ejemplo, ETA).

---

## 5. Experiencia de producto (app)

El prototipo inicial de branding contempla el siguiente recorrido:

1. **Onboarding** — presentación de la marca y acceso.
2. **Alta de ficha / perfil** — datos personales, cobertura y contactos de emergencia.
3. **Home listo** — estado preparado para activación.
4. **Confirmación en pantalla bloqueada** — flujo de las 3 pulsaciones + deslizamiento.
5. **Seguimiento de asistencia** — estado de la unidad / prestador.
6. **Perfil médico** — consulta y mantenimiento de datos clínicos relevantes.

**Nota de seguridad clínica:** en situaciones de riesgo vital inminente, el usuario debe llamar siempre primero al **107** o **911**. Xpedit optimiza la coordinación con coberturas privadas de forma inteligente; no sustituye la emergencia pública cuando corresponde.

---

## 6. Impacto por actor del ecosistema

### 6.1. Afiliados y pacientes

- Despacho directo, sin llamadas burocráticas.
- Historial médico esencial disponible para el prestador.
- Mayor certeza sobre el destino asistencial con cobertura.

### 6.2. Obras sociales y prepagas

- Control de derivación por convenio exacto.
- Monitoreo auditado de tiempos de respuesta de prestadores.
- Menor exposición a errores de derivación y costos asociados.

### 6.3. Sistema público de salud

- Descongestión potencial de la red 107/911 al redirigir casos con cobertura privada.
- Reducción de falsas alertas mediante confirmación explícita.
- Mejor coordinación interinstitucional en emergencias.

---

## 7. Identidad de marca (resumen)

La identidad visual y verbal se define en el *Manual de Sistema Visual y Directrices de Marca* (Figma).

### 7.1. Pilares de marca

| Pilar | Definición |
|---|---|
| **Velocidad serena** | Inmediatez operativa controlada, sin generar pánico. |
| **Precisión operativa** | Asignar la ambulancia / prestador correcto según cobertura. |
| **Confianza humana** | Interfaz y voz que calman y contienen de forma profesional. |

### 7.2. Eslogan oficial

**Donde corresponde, cuando importa.**

Jerarquía comunicacional:

- el **eslogan oficial** lidera la comunicación institucional y el hero de producto;
- el **claim web** (*Conexión médica instantánea…*) opera como línea de apoyo.

### 7.3. Tono de voz

- **Empatía activa** — calmar, no sobrecargar.
- **Precisión directa** — instrucciones breves y lógicas.
- **Seguridad legal** — foco en coberturas y respaldo institucional.

### 7.4. Sistema visual

**Paleta**

| Color | Hex | Rol |
|---|---|---|
| Azul Xpedit (Navy) | `#0A193F` | Primario institucional: autoridad y confianza |
| Cian Vital | `#00B4D8` | Secundario tecnológico: acción y salud digital |
| Rojo Urgencia | `#FF4D6D` | Acento de alerta: solo confirmación / estados críticos |
| Gris Clínico | `#F8FAFC` | Fondos y legibilidad |

**Tipografía**

- **Outfit** — principal (marca + app): logotipo, títulos, navegación, CTAs y UI.
- **Geist** — secundaria (lectura / datos): párrafos, tablas clínicas y notas legales.

**Versiones del identificador**

1. **Logotipo principal** — XPEDIT GROUP (corporativo; GROUP en cian light con espacio suficiente).
2. **Isotipo normalizado** — App Icon / splash / avatar (solo la X).
3. **Lockup compacto** — Isotipo + XPEDIT (headers móviles; sin GROUP).
4. **Área de protección** — 50% de la altura del imagotipo.

---

## 8. Seguridad, privacidad e integridad operativa

Principios de diseño del producto:

- confirmación explícita antes del envío;
- cifrado del paquete de datos de emergencia;
- uso restringido del rojo de urgencia a estados críticos reales;
- priorización de legibilidad y control en momentos de estrés.

La marca evita lenguajes o visuales de “pánico”: la velocidad debe sentirse **serena, precisa y confiable**.

---

## 9. Estado actual y próximos pasos

### 9.1. Estado actual

- Branding inicial definido en Figma (manual, landing, flujo app y piezas sociales).
- Narrativa de producto y valor alineada al problema argentino de urgencias + cobertura.
- Proyecto en fase de **planificación y validación de negocio**.

### 9.2. Próximos pasos sugeridos

1. Validación con encuestas / entrevistas a potenciales usuarios y actores del ecosistema.
2. Definición de hipótesis de valor y métricas de validación.
3. Especificación funcional del MVP (app + API de despacho + reglas de cobertura).
4. Conversaciones exploratorias con obras sociales, prepagas y prestadores de ambulancia.
5. Marco legal y de privacidad (tratamiento de datos de salud).

---

## 10. Cierre

Xpedit Group nace para resolver una fricción concreta del sistema de urgencias en Argentina: **llegar rápido, pero también llegar al lugar correcto**.

La tecnología habilita el canal; la marca sostiene la confianza.

> **Donde corresponde, cuando importa.**

---

### Datos del documento

| Campo | Valor |
|---|---|
| Proyecto | Xpedit Group |
| Tipo | Documento de presentación / brief de proyecto |
| Mercado inicial | Argentina |
| Categoría | Digital Health-Tech / Emergencias médicas |
| Fuente de diseño | Figma — Branding (`7AHSRaaQdAtXOSH4Xh0kTG`) |
| Formatos | Markdown + PDF |

*Documento generado a partir del branding y la narrativa de producto definidos en Figma, septiembre 2026.*
