# Buyer Persona B2B — Cliente white-label (obra social / prepaga)

**Versión:** 1.0  
**Fecha:** octubre 2026  
**Estado:** basado en encuesta de afiliados (N=384) + pivote de modelo de negocio  
**Rol en el funnel:** *Economic buyer / Champion digital* — quien compra o impulsa la compra del SaaS  
**Documento hermano:** [08-usuario-final-actualizado.md](08-usuario-final-actualizado.md)  
**Evidencia:** [06-analisis-encuesta-validacion.md](06-analisis-encuesta-validacion.md)

---

## BUYER PERSONA

| Campo | Detalle |
|---|---|
| **Nombre** | Mariana Soler |
| **Edad** | 42 años |
| **Cargo** | Gerenta de Prestaciones / Producto Digital (o subgerencia de Urgencias + Canales Digitales) |
| **Organización** | Obra social de alcance nacional o prepaga mediana/grande con app móvil propia |
| **Ubicación** | AMBA (oficina central) · operación en varias provincias |
| **Reporta a** | Dirección Médica / COO / Gerencia General |
| **Influencia de compra** | Alta: arma el business case; necesita aliados en legal, IT, call center y prestadores |

### Descripción

Mariana lidera la mejora de la experiencia del afiliado y la eficiencia de urgencias. Su organización ya tiene app móvil (trámites, cartilla, autorización), pero el momento de emergencia sigue resolviéndose por teléfono, 107 o “como pueda el afiliado”. Ve saturación de líneas, poca trazabilidad del primer contacto y reclamos por demoras. No busca “otra app más” para el afiliado: busca **capacidades** que se integren a la app y a los sistemas que ya controlan.

### Objetivo

Incorporar un **módulo de activación de emergencias de bandera blanca** (SDK/API) dentro de la app de la cobertura, que:

1. reduzca el tiempo hasta el despacho correcto,  
2. envíe ficha + ubicación al prestador de la red,  
3. baje la fricción “¿llamo al 107 o a ustedes?”,  
4. mejore percepción de valor de la cobertura en el momento crítico,  
5. genere datos auditables de tiempos y destinos.

### Frustraciones

- Los afiliados, ante una urgencia, llaman al **107** o van por sus medios en lugar de activar la red de la cobertura (encuesta: 42% 107, 36% por medios propios, solo 20% llaman primero a OS/prepaga).  
- El call center se satura con consultas que no son código rojo (efecto pirámide del sector).  
- Poca visibilidad del journey de emergencia del afiliado.  
- Presión comercial/reputacional: “pago la prepaga y en una urgencia no me sirve”.  
- Proyectos digitales que fracasan si piden instalar una app nueva de un tercero.  
- Riesgo legal y de marca si un partner B2C maneja mal datos de salud.

### Necesidades

- Solución **white-label** (marca de la OS/prepaga, no marca startup frente al afiliado).  
- Integración con app existente (SDK nativo / WebView controlado / API de despacho).  
- Confirmación anti-falsas alarmas.  
- Gobierno de datos: custodia alineada a la política del financiador.  
- Motor de reglas de cobertura → prestador / flota autorizada.  
- Panel de métricas: activaciones, tiempos, destinos, cancelaciones.  
- Implementación con IT y legal sin rehacer toda la app.  
- Argumentos de valor basados en evidencia de afiliados (confianza, intención, dolor de demora).

### Comportamiento de compra

- Evalúa vendors con demo + seguridad + casos de uso.  
- Exige referencias, SLA, DPA / tratamiento de datos.  
- Compra por **piloto** (una región / un segmento) antes de rollout nacional.  
- Involucra: Prestaciones, Digital/IT, Legal, Comunicación al afiliado, Operador de ambulancias/red.  
- Sensible a costo por afiliado activo / por despacho / licencia SaaS.

### Motivaciones

- Diferenciar la app y la cobertura en un momento de alta emoción.  
- Reducir demoras percibidas y reclamos.  
- Capturar emergencias que hoy se “escapan” al 107 o a la calle.  
- Mostrar innovación responsable (salud + digital) a directorio y afiliados.  
- Controlar que el afiliado caiga en la red contratada.

### Objeciones típicas

| Objeción | Respuesta de Xpedit |
|---|---|
| “No queremos otra app” | No es otra app: es módulo dentro de la suya. |
| “Datos de salud / privacidad” | Custodia bajo políticas del financiador; cifrado; mínimo dato necesario. |
| “Falsas alarmas” | Confirmación explícita + timeout + cancelación. |
| “Ya tenemos call center” | El módulo alimenta al mismo ecosistema; no lo reemplaza a ciegas. |
| “El afiliado prefiere el 107” | El 107 sigue para lo público; esto activa *su* red cuando hay cobertura. |
| “¿Y si falla?” | SLA, fallback a llamada, monitoreo, modo degradado. |

---

## MAPA DE EMPATÍA (buyer B2B)

### ¿Qué ve?

- Dashboards de reclamos y tiempos de atención.  
- App propia con baja adopción en el use case “emergencia”.  
- Competencia digitalizando canales.  
- Reportes sectoriales: pocas consultas son código rojo, pero saturan el sistema.  
- Afiliados que en redes cuentan demoras o “no sabía a quién llamar”.

### ¿Qué escucha?

- “En una urgencia llamá al 107.”  
- Del directorio: “mejoren la experiencia digital”.  
- De legal: “cuidado con datos sensibles y partners”.  
- De IT: “no podemos integrar cualquier cosa”.  
- De afiliados (vía encuesta/NPS): quieren que **la cobertura** respalde la solución (50% en la encuesta).

### ¿Qué piensa y siente?

- “Si no estamos en el primer minuto de la emergencia, perdemos la relación.”  
- Miedo a un incidente de datos o a una activación errónea viralizada.  
- Esperanza de un quick win medible (piloto).  
- Necesita un partner que hable de **operación + producto**, no solo de UI.

### ¿Qué dice y hace?

- Pide RFP / demo / arquitectura de integración.  
- Consulta a su operador de ambulancias y a sistemas.  
- Prioriza proyectos con ROI en 6–12 meses.  
- Comunica al afiliado solo lo que está “aprobado” por la marca.

### Dolores (Pains)

- Fuga de activaciones hacia 107 / medios propios.  
- Demora percibida (dolor #1 del afiliado en encuesta: 60%).  
- Baja confianza en apps de salud de terceros.  
- Complejidad de integración y compliance.  
- Saturación operativa por demanda no crítica.

### Ganancias (Gains)

- Módulo propio de emergencias en la app.  
- Más activaciones en red contratada.  
- Mejor NPS / menos reclamos por “no me atendieron”.  
- Datos para gestionar prestadores.  
- Narrativa: “tu cobertura te responde cuando importa”.

---

## Propuesta de valor hacia Mariana (pitch B2B)

> Xpedit le vende a su obra social/prepaga un **SaaS de bandera blanca** para activar emergencias desde *su* app: confirmación segura, ficha y GPS, despacho al prestador de su red.  
> Sus afiliados ya dijeron que confían más si lo ofrece **usted** — no una app independiente.

### Evidencia de afiliados a usar en la venta

- 50% quiere respaldo de prepaga/obra social vs 5% app independiente.  
- 60% prioriza que no tarde la ayuda.  
- 70% ve útil la idea de activación + confirmación (puntaje ≥ 4).  
- 73% con alta probabilidad de completar ficha si la solución existe (bajo el paraguas correcto).  

---

## Criterios de éxito del piloto (sugeridos)

1. Tiempo medio desde confirmación hasta aceptación del prestador.  
2. % de activaciones que terminan en prestador de cartilla.  
3. % de cancelaciones / falsas alarmas.  
4. CSAT post-evento (muestra).  
5. Adopción: % afiliados con ficha completa en la app.

---

## Segmentación de cuentas objetivo (hipótesis)

| Prioridad | Tipo de cuenta | Por qué |
|---|---|---|
| Alta | Prepagas / OS con app móvil madura y red de urgencias propia o contratada | Encaje técnico + dolor de fuga al 107 |
| Media | OS provinciales / sindicales digitalizando app | Menos madurez, ciclo más largo |
| Baja (fase 1) | Financiadores sin app | Requiere canal alternativo; no es white-label puro |

---

## Nota metodológica

Este persona es el **cliente que paga**. El afiliado es usuario final, no buyer.  
Se construyó a partir del pivote a white-label y de la evidencia de confianza/canal de la encuesta N=384.  
Validación pendiente: 5–8 entrevistas a roles de Prestaciones / Digital en OS y prepagas.

---

*Xpedit Group · Buyer persona B2B white-label v1.0 · octubre 2026*
