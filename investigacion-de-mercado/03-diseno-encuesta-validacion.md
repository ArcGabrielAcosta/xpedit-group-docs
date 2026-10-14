# Xpedit Group — Encuesta de validación

**Versión:** 1.0  
**Fecha:** septiembre 2026  
**Buyer persona de referencia:** Fernando Ríos (usuario afiliado · AMBA · Mar del Plata)  
**Objetivo:** validar dolor, comportamiento actual, aceptación de la solución y barreras de adopción  

---

## Texto introductorio (para el Google Form)

> Gracias por participar. Esta encuesta dura aproximadamente **4–6 minutos**.  
> Estamos validando una idea de producto de salud digital en Argentina: un canal que, ante una emergencia médica, conecta al afiliado con el servicio de ambulancia / prestador que corresponde según su obra social o prepaga.  
> No hay respuestas correctas o incorrectas. Tus datos se usan solo con fines de investigación de producto.

---

## Sección A — Preguntas filtro

Usá estas al inicio. Podés configurar lógica de salto: si no califica para la muestra primaria, agradecer y finalizar (o enviar a una rama corta).

### F1. ¿Tenés actualmente obra social o prepaga?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Sí, prepaga
  - Sí, obra social
  - No / solo sistema público
  - Prefiero no decirlo

**Criterio v1:** incluir si elige prepaga u obra social.

### F2. ¿En qué zona vivís la mayor parte del tiempo?
- Tipo: opción múltiple (una sola)
- Opciones:
  - CABA
  - GBA (Gran Buenos Aires)
  - Mar del Plata
  - Interior de Buenos Aires (otra ciudad)
  - Otra provincia
  - Prefiero no decirlo

**Criterio v1:** incluir CABA, GBA o Mar del Plata en el análisis principal.

### F3. ¿Qué edad tenés?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Menos de 18
  - 18–27
  - 28–45
  - 46–60
  - Más de 60

**Criterio v1:** excluir menores de 18. Núcleo ideal: 28–45.

### F4. ¿Usás smartphone de forma habitual (WhatsApp, apps, etc.)?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Sí
  - No

**Criterio v1:** incluir solo “Sí”.

### F5. En los últimos 24 meses, ¿vos o alguien a tu cargo necesitó una urgencia o emergencia médica?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Sí
  - No
  - No estoy seguro/a

*No excluye; segmenta experiencia real vs. hipotética.*

### F6. Si hoy hubiera una urgencia médica y tenés cobertura (obra social/prepaga), ¿qué harías primero?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Llamar al 107 / 911
  - Llamar a mi prepaga u obra social
  - Llamar a una ambulancia privada
  - Ir por mis medios a una clínica u hospital
  - Pedirle a alguien que llame por mí
  - No sabría qué hacer

### F7. ¿Quién sería el usuario principal de una app de este tipo en tu casa?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Yo
  - Yo y mi pareja
  - Un familiar a cargo (padres / hijos / otro)
  - Probablemente nadie la usaría

---

## Sección B — 10 preguntas de validación

### P1. Ante una emergencia con tu cobertura, ¿qué tan claro tenés hoy cuál es el primer paso correcto?
- Tipo: escala lineal 1–5  
  - 1 = Nada claro  
  - 5 = Totalmente claro

**Qué valida:** incertidumbre del primer contacto (dolor central).

### P2. ¿Cuál de estos problemas te preocupa más en una urgencia médica?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Que tarde en llegar la ayuda
  - Que me deriven a un lugar que no corresponde a mi cobertura
  - No saber a qué número llamar
  - No poder explicar bien mi ubicación
  - Tener que dar datos médicos / de cobertura en ese momento
  - Ninguno me preocupa especialmente

**Qué valida:** priorización del dolor (tiempo vs. precisión vs. información).

### P3. ¿Alguna vez viviste o conocés de cerca una demora, mala derivación o fricción entre el 107 y la cobertura privada?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Sí, me pasó a mí
  - Sí, le pasó a alguien cercano
  - No, pero lo veo plausible
  - No y no me parece un problema frecuente

**Qué valida:** intensidad del problema percibido / experiencia real.

### P4. Si tuvieras que elegir, ¿qué valorás más en una emergencia?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Que la ayuda llegue lo más rápido posible, aunque no sea el prestador de mi cartilla
  - Que me atiendan el prestador correcto según mi cobertura, aunque tarde un poco más
  - Ambos por igual: velocidad y prestador correcto
  - No sabría elegir

**Qué valida:** si el diferencial “donde corresponde” es realmente valioso.

### P5. Te proponemos esta idea: tres pulsaciones del botón de bloqueo abren una ventana; solo si deslizás para confirmar se envía la alerta a la ambulancia/prestador de tu cobertura, con tus datos y ubicación. ¿Qué tan útil te parece?
- Tipo: escala lineal 1–5  
  - 1 = Nada útil  
  - 5 = Muy útil

**Qué valida:** aceptación del concepto central (solution/problem fit).

### P6. ¿Qué tan cómodo/a te sentirías cargando de antemano en una app datos como cobertura, alergias, grupo sanguíneo y contacto de emergencia?
- Tipo: escala lineal 1–5  
  - 1 = Nada cómodo/a  
  - 5 = Muy cómodo/a

**Qué valida:** fricción de onboarding / confianza en datos sensibles.

### P7. ¿Cuál sería tu mayor duda o freno para usar una app así?
- Tipo: opción múltiple (una sola) — o casillas si querés marcar hasta 2
- Opciones:
  - Privacidad y uso de mis datos de salud
  - Miedo a activarla por error
  - Prefiero seguir llamando al 107
  - No confío en apps nuevas de salud
  - Preferiría que me la ofrezca mi prepaga u obra social
  - Me parece complicada de configurar
  - Ningún freno importante

**Qué valida:** objeciones principales para diseñar copy, producto y partnerships.

### P8. ¿Quién debería ofrecerte o respaldar esta solución para que confíes más?
- Tipo: opción múltiple (una sola)
- Opciones:
  - Mi prepaga u obra social
  - Una empresa de ambulancias / prestador de urgencias
  - Una app independiente especializada
  - El sistema público (107 / ministerio / municipio)
  - Me da igual, si funciona bien

**Qué valida:** canal de confianza y go-to-market (B2B2C vs. B2C).

### P9. Si esta app existiera mañana y fuera gratis para vos como afiliado, ¿qué tan probable es que la instales y completes tu ficha?
- Tipo: escala lineal 1–5  
  - 1 = Nada probable  
  - 5 = Muy probable

**Qué valida:** intención de adopción (proxy de demanda).

### P10. En una frase, ¿qué tendría que cumplir esta solución para que la uses sin dudarlo?
- Tipo: respuesta corta / párrafo

**Qué valida:** requisitos espontáneos del usuario (confianza, velocidad, respaldo institucional, etc.).

---

## Lógica de muestra recomendada (análisis)

| Condición | Acción |
|---|---|
| Sin prepaga/obra social, o sin smartphone, o menor de 18 | Fuera de muestra primaria |
| CABA / GBA / Mar del Plata + cobertura + smartphone | **Muestra primaria** |
| Resto de zonas con cobertura | Muestra secundaria (comparar) |
| P5 ≥ 4 y P9 ≥ 4 | Segmento “alta intención” |
| P7 = privacidad o prepaga | Priorizar mensajes de confianza / partnership |

---

## Orden sugerido en Google Forms

1. Texto introductorio  
2. F1 → F7 (filtros)  
3. P1 → P10 (validación)  
4. (Opcional) email de contacto si quiere enterarse del avance  

### Mensaje de cierre

> Gracias por tu tiempo. Tu respuesta nos ayuda a construir una solución más segura y útil para emergencias con cobertura en Argentina.

---

*Xpedit Group · Encuesta de validación v1.0 · septiembre 2026*
