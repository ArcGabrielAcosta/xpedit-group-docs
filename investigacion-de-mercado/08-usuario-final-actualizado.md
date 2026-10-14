# Usuario final actualizado — Afiliado (post-encuesta)

**Versión:** 2.0  
**Fecha:** octubre 2026  
**Estado:** actualizado con encuesta N=384  
**Rol en el funnel:** usuario del módulo de emergencias **dentro de la app de su obra social / prepaga**  
**Reemplaza / actualiza:** persona provisional Fernando Ríos (v1 pre-encuesta)  
**Evidencia:** [06-analisis-encuesta-validacion.md](06-analisis-encuesta-validacion.md)  
**Cliente que compra la solución:** [07-buyer-persona-b2b-white-label.md](07-buyer-persona-b2b-white-label.md)

---

## BUYER PERSONA (usuario final)

| Campo | Detalle |
|---|---|
| **Nombre** | Ricardo Fernández |
| **Edad** | 52 años *(rango empírico dominante: 46–60)* |
| **Ocupación** | Empleado en relación de dependencia / comercio o servicios |
| **Ubicación** | GBA o Mar del Plata (también representativo de CABA) |
| **Cobertura** | Obra social o prepaga con cartilla de urgencias |
| **Dispositivo** | Smartphone diario (WhatsApp, homebanking, app de la cobertura) |

### Descripción

Ricardo tiene cobertura hace años. En el día a día casi no piensa en emergencias. Si algo pasa, su reflejo más frecuente es llamar al **107** o ir por sus medios a una guardia — no abrir un trámite digital de su obra social. Valora sobre todo que **la ayuda llegue rápido**. Desconfía de apps de salud “nuevas” o desconocidas, pero usaría sin tanto roce una función **dentro de la app de su cobertura**, si es simple, segura y no se activa sola.

Convive en pareja; a veces también es quien coordina urgencias de padres. No quiere configurar sistemas complejos en un momento de pánico: quiere confirmar y que el sistema haga el resto.

### Cambios vs. persona provisional (v1)

| Aspecto | v1 (hipótesis) | v2 (datos) |
|---|---|---|
| Edad núcleo | 28–45 | **46–60** (también 28–45 relevante) |
| Dolor principal | Derivación incorrecta / “dónde corresponde” | **Demora** (60% lo eligió como mayor preocupación) |
| Canal de confianza | Marca Xpedit / app propia | **App y marca de su OS/prepaga** |
| Primer paso actual | Dudaba entre 107 y prepaga | Empíricamente: **107** o **ir por medios**; pocos llaman primero a la cobertura |
| Producto percibido | App Xpedit standalone | **Módulo dentro de la app de la cobertura** |

### Objetivo

En una emergencia (propia o de un familiar), **activar ayuda rápido**, con la tranquilidad de que:

- no tiene que explicar todo de cero,  
- sus datos básicos ya están,  
- y la respuesta llega por el canal de **su cobertura**, sin instalar ni aprender otra app.

### Frustraciones

- No tener claro el primer paso (claridad media ≈ 3/5, muy polarizada).  
- Que la ambulancia o la ayuda **tarde**.  
- Tener que dar datos médicos o de cobertura bajo estrés.  
- Haber oído (o vivido de cerca) demoras / mala coordinación 107 ↔ privada (muy frecuente como percepción).  
- Miedo a apps que filtren datos o se activen por error.  
- Sensación de “pago la cobertura y cuando más la necesito, improvisamos”.

### Necesidades

- Botón / flujo de emergencia **visible en la app que ya tiene**.  
- Confirmación explícita antes de enviar (deslizar / confirmar).  
- Ficha previa: cobertura, alergias, grupo sanguíneo, contactos.  
- Señal de que “está en camino” / fue tomado el pedido.  
- Privacidad garantizada por la institución de salud.  
- Uso simple (pocos pasos, letra clara, sirve también a +60).

### Comportamiento digital

- Smartphone habitual.  
- Usa WhatsApp y apps de trámites; la app de la OS/prepaga la tiene, aunque no todos los días.  
- No busca “apps de emergencia” en la tienda por iniciativa propia.  
- Si su cobertura se lo promociona (push, mail, onboarding), la probabilidad de adopción sube fuerte.  
- En abiertas pide: simpleza, que no falle, privacidad, respaldo oficial.

### Motivaciones

- Protegerse y proteger a la familia.  
- Ganar minutos.  
- Reducir improvisación.  
- Sentir que **su cobertura cumple** en el momento crítico.  
- Evitar pánico por no saber a quién llamar.

---

## MAPA DE EMPATÍA

### ¿Qué ve?

- Números de emergencia, cartillas, apps de la prepaga/OS.  
- Colas en guardia, demoras, historias de “esperé mucho”.  
- Publicidad o mails de su cobertura sobre beneficios digitales.

### ¿Qué escucha?

- “Llamá al 107.”  
- “Usá el número de la prepaga.”  
- Recomendaciones contradictorias de familiares.  
- Dudas sobre privacidad de datos de salud en apps.

### ¿Qué piensa y siente?

- “Que venga ya.”  
- “¿Y si no llega?”  
- “No quiero cargar la tarjeta ni que me roben los datos.”  
- “Si lo dice mi obra social, me animo más.”  
- En emergencia: poca paciencia para menús largos.

### ¿Qué dice y hace?

- Llama al 107 o se maneja a una clínica.  
- A veces llama a la OS/prepaga.  
- Pregunta a la pareja o a un hijo más digital.  
- Evita instalar apps dudosas; acepta mejor funciones “oficiales”.

### Dolores (Pains)

- Demora.  
- Incertidumbre del primer paso.  
- Estrés al dar datos.  
- Desconfianza en apps nuevas.  
- Miedo a activación accidental.

### Ganancias (Gains)

- Activación en segundos, con confirmación.  
- Respuesta de la red de su cobertura.  
- Menos explicación en crisis.  
- Confirmación de que el pedido fue tomado.  
- Sensación de control y respaldo institucional.

---

## Jobs-to-be-Done

> Cuando hay una urgencia médica mía o de alguien a cargo, quiero activar ayuda **rápida y confiable desde la app de mi cobertura**, para no perder tiempo improvisando entre el 107, un número olvidado y una guardia al azar.

---

## Implicancias de UX (módulo white-label)

1. La marca visible es la de la **obra social / prepaga**; Xpedit puede ser “powered by” discreto o invisible.  
2. CTA de emergencia siempre accesible (home / widget / atajo).  
3. Mantener **confirmación** (anti-error).  
4. Onboarding de ficha en momento de calma, no en crisis.  
5. Feedback claro: “Solicitud enviada · Prestador notificado · ETA…”.  
6. Diseño usable para 46–60 y +60 (contraste, tamaños, pocas decisiones).  
7. Opción de notificar contacto de emergencia (pedido espontáneo en abiertas).

---

## Segmentos de usuario final (para diseño y comunicación)

| Segmento | Señal en encuesta | Prioridad UX |
|---|---|---|
| Adulto 46–60 con OS/prepaga | Mayor volumen etario | Alta |
| Pareja que gestiona juntos | “Yo y mi pareja” frecuente | Alta |
| Cuidador de familiar | 18 respuestas | Media-alta |
| Joven 18–27 / 28–45 | Menor volumen pero digital nativo | Media |
| Solo sistema público | Fuera del ICP white-label fase 1 | Baja (fase 1) |

---

## Relación con el buyer B2B

Ricardo **no paga** Xpedit.  
Mariana (OS/prepaga) compra el SaaS para que Ricardo tenga el módulo en *su* app.  
La encuesta valida a Ricardo como usuario y, al mismo tiempo, le da a Mariana la evidencia de que sus afiliados **exigen su respaldo** para confiar.

---

## Nota metodológica

- Persona v2 derivado de frecuencias de la encuesta (N=384) y muestra primaria (n=224).  
- No implica que todos los afiliados tengan 52 años; es el arquetipo del núcleo empírico.  
- Actualizar tras entrevistas cualitativas y tras el primer piloto white-label.

---

*Xpedit Group · Usuario final actualizado v2.0 · octubre 2026*
