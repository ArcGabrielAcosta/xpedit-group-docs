# Xpedit Group — Estudio de población y contextos de urgencia / emergencia médica

**Tipo de documento:** Informe de investigación aplicada (fase de validación de producto)  
**Versión:** 1.0  
**Fecha:** septiembre 2026  
**Mercado de referencia:** Argentina  
**Objetivo del estudio:** comprender las principales causas de mortalidad de la población argentina, identificar escenarios potenciales de solicitud de ambulancia y delimitar en qué contextos de urgencia o emergencia médica encaja el uso de la aplicación Xpedit.

---

## 1. Resumen ejecutivo

Este informe sistematiza una investigación documental sobre las principales causas de muerte en Argentina y las traduce a **casos potenciales de activación de asistencia prehospitalaria** (ambulancia / urgencias). El análisis se complementa con el **efecto espectador**, fenómeno psicosocial relevante cuando una emergencia ocurre en vía pública o frente a terceros.

Hallazgos centrales:

1. En la población general, las principales causas de muerte son **enfermedades del sistema circulatorio**, **enfermedades respiratorias** y **tumores**.
2. En jóvenes de **15 a 34 años**, predominan causas externas: **accidentes de tránsito** y **suicidios**.
3. Este perfil se explica por una **transición epidemiológica** consolidada desde mediados del siglo XX.
4. No toda causa de muerte equivale a un llamado a ambulancia, pero varias de las principales sí se asocian a **eventos tiempo-dependientes** (infarto, ACV, insuficiencia respiratoria aguda, trauma).
5. En vía pública, el **efecto espectador** puede retrasar la ayuda: la difusión de responsabilidad entre presentes reduce la probabilidad o la velocidad de intervención.
6. Xpedit encaja especialmente cuando el paciente (o un allegado designado) necesita **activar al prestador correcto según cobertura**, con datos y ubicación, sin depender exclusivamente de la improvisación de terceros o de la triangulación 107 → prepaga.

---

## 2. Objetivo y preguntas de investigación

### 2.1. Objetivo general

Delimitar el campo de problema epidemiológico argentino y su vínculo con escenarios de urgencia/emergencia en los que una aplicación de despacho asistido por cobertura puede agregar valor.

### 2.2. Preguntas guía

1. ¿Cuáles son las principales causas de muerte en Argentina (población total y 15–34 años)?  
2. ¿Qué proceso histórico explica ese perfil?  
3. ¿Qué parte de ese mapa se traduce en necesidad potencial de ambulancia?  
4. ¿Qué ocurre psicológicamente cuando la emergencia es pública (efecto espectador)?  
5. ¿En qué franja de ese mapa encaja Xpedit — y en cuál no debería posicionarse como primera línea?

---

## 3. Metodología y fuentes

### 3.1. Enfoque

Investigación documental y de síntesis aplicada a producto, no un estudio clínico ni un muestreo primario de mortalidad.

### 3.2. Fuentes principales

- Compilación propia a partir de portales oficiales y estadísticas públicas (`argentina.gob.ar`, Instituto Nacional del Cáncer / Ministerio de Salud).
- Anuarios y series de defunciones de la **Dirección de Estadísticas e Información en Salud (DEIS)**.
- Análisis secundarios del Observatorio de Salud (Universidad ISALUD) sobre causas de muerte 2014–2024.
- Literatura clásica y contemporánea sobre **efecto espectador** e intervención de bystanders en emergencias (Darley & Latané; estudios de RCP / OHCA).
- Literatura sobre **transición epidemiológica** en Argentina (revistas y repositorios académicos citados en la recopilación).

### 3.3. Limitaciones

- Las causas de muerte **no son idénticas** a las causas de llamados a ambulancia.
- Parte de las cifras circulantes en medios y resúmenes redondean porcentajes; este informe prioriza órdenes de magnitud y ranking, no precisión clínica individual.
- El efecto espectador se documenta sobre todo en literatura internacional; su aplicación a Argentina es **analítica e hipotética**, útil para diseño de producto, no como medición local propia.

---

## 4. Hallazgos: mortalidad en Argentina

### 4.1. Población general — principales causas

Según la síntesis de registros oficiales y análisis basados en DEIS:

| Orden | Grupo de causas | Magnitud aproximada / evidencia | Ejemplos clínicos relevantes |
|---|---|---|---|
| 1 | Enfermedades del sistema circulatorio | ~27–28% de las muertes; en 2024 se reportaron **105.130** defunciones por esta causa | Infarto / isquemia cardíaca, insuficiencia cardíaca, ACV, hipertensivas |
| 2 | Enfermedades del sistema respiratorio | ~18–21% según series y año; fuerte peso de neumonía e influenza | Neumonía, EPOC descompensada, insuficiencia respiratoria aguda |
| 3 | Tumores (cáncer) | ~15–20% (tendencia levemente descendente en la última década; ~16% en 2024) | Entre sitios, el cáncer de pulmón concentra alta mortalidad |

**Lectura para producto:** el liderazgo persistente de lo cardiovascular confirma que Argentina enfrenta, de modo estructural, eventos potencialmente **tiempo-dependientes**. Eso no implica que todas esas muertes ocurran como emergencias callejeras, pero sí que el sistema de urgencias convive de forma permanente con cuadros cardíacos y cerebrovasculares.

### 4.2. Persistencia histórica (≈70 años)

Las enfermedades cardiovasculares y respiratorias se consolidaron como principales causas de muerte en Argentina desde mediados del siglo XX (aprox. décadas de 1950–1960). Ni siquiera la pandemia de COVID-19 desplazó a las cardiovasculares del primer lugar: en 2020–2021 el COVID se posicionó temporalmente como **segunda** causa de mortalidad.

### 4.3. Transición epidemiológica

El cambio de perfil responde a un proceso nacional y global llamado **transición epidemiológica**:

- mejora de higiene e infraestructura;
- urbanización;
- antibióticos y vacunas;
- caída de muertes infecciosas “clásicas”;
- ascenso de **Enfermedades No Transmisibles (ENT)** y afecciones asociadas al envejecimiento y a estilos de vida urbanos (sedentarismo, tabaquismo, etc.).

#### Etapas históricas resumidas

| Época / período | Causas principales | Contexto |
|---|---|---|
| Siglo XIX y principios del XX (hasta ~1920) | Infecciosas y parasitarias (cólera, fiebre amarilla, tuberculosis, viruela, malaria) e infecciones gastrointestinales | Alta mortalidad infantil, hacinamiento migratorio, débil infraestructura sanitaria |
| Décadas de 1930 a 1950 | Tuberculosis y neumonías, con primeros aumentos de enfermedades cardíacas | Transición: vacunación masiva y penicilina reducen brotes tradicionales |
| De 1960 en adelante | Circulatorias, tumores y respiratorias | Perfil actual: urbanización, ENT, mayor expectativa de vida |
| Excepción 2020–2021 | COVID-19 como anomalía temporal (2.ª causa) | No desplazó el liderazgo cardiovascular |

### 4.4. Población de 15 a 34 años

En este grupo etario, el registro histórico y actual muestra un patrón distinto:

- **Accidentes de tránsito**
- **Suicidios**

Es decir: en jóvenes, las principales causas no son las ENT crónicas del adulto mayor, sino **causas externas**. Esto tiene implicancias claras para trauma, vía pública y respuesta inmediata — y también límites éticos/productivos: Xpedit no es una herramienta de salud mental ni sustituye líneas especializadas de prevención del suicidio.

---

## 5. De la mortalidad a los llamados de ambulancia

### 5.1. Distinción operativa: urgencia vs. emergencia

Para el encaje de producto conviene separar:

| Concepto | Definición práctica | Implicancia |
|---|---|---|
| **Emergencia** | Riesgo vital inminente o daño irreversible si no se actúa ya | Prioridad máxima; minutos cuentan |
| **Urgencia** | Requiere atención rápida, pero no siempre con el mismo grado de inmediatez vital | Puede necesitar traslado asistido o evaluación prioritaria |

Xpedit se posiciona sobre todo en la franja donde **hay cobertura privada**, hay necesidad de **asistencia prehospitalaria / derivación correcta**, y el costo de equivocar el canal (107 genérico vs. prestador de cartilla) es alto.

### 5.2. Casos potenciales de llamado a ambulancia (mapeo analítico)

A partir del mapa epidemiológico, se proponen clusters de activación potencial:

#### A. Eventos cardiovasculares agudos
- Infarto agudo de miocardio / dolor precordial de alto riesgo  
- ACV (déficit neurológico súbito)  
- Síncope / colapso de origen cardíaco sospechado  

**Por qué importan:** alta prevalencia poblacional + ventana terapéutica crítica.

#### B. Eventos respiratorios agudos
- Dificultad respiratoria severa  
- Descompensación de EPOC / asma grave  
- Neumonía con deterioro agudo  

**Por qué importan:** segunda gran familia de mortalidad; frecuente en adultos mayores.

#### C. Trauma y vía pública (especialmente 15–34)
- Accidentes de tránsito  
- Caídas / traumatismos en espacio público  

**Por qué importan:** en jóvenes dominan las causas externas; suelen ocurrir frente a terceros.

#### D. Otros escenarios de alta incertidumbre del “primer paso”
- Emergencia en domicilio con prepaga activa  
- Emergencia de un familiar a cargo  
- Usuario que no sabe si llamar al 107, a la prepaga o a una ambulancia directa  

**Nota:** tumores/cáncer son causa mayor de muerte, pero muchas veces el final de vida no se traduce en el mismo patrón de “activación SOS de calle”. Sí pueden aparecer urgencias asociadas (complicaciones agudas), aunque no son el core narrativo inicial de Xpedit.

### 5.3. Hipótesis de encaje para Xpedit

Xpedit agrega más valor cuando coinciden estas condiciones:

1. el afiliado tiene **obra social / prepaga** con cartilla de urgencias;  
2. el evento requiere **asistencia móvil o derivación rápida**;  
3. existe riesgo de **triangulación ineficiente** (107 → búsqueda de convenio);  
4. hay datos útiles pre-cargados (cobertura, alergias, contacto, GPS);  
5. la activación puede hacerse por el propio usuario o un allegado, con **confirmación explícita**.

Xpedit **no** debería presentarse como:
- reemplazo del 107/911 en riesgo vital cuando esa sea la vía correcta o la única disponible;
- solución de prevención primaria de cáncer o de enfermedades crónicas;
- línea de crisis de salud mental / suicidio.

---

## 6. Complemento de investigación: efecto espectador

### 6.1. Qué es

El **efecto espectador** (*bystander effect*) describe la menor probabilidad —o mayor demora— de que una persona ayude en una emergencia cuando hay **otras personas presentes**. No implica necesariamente indiferencia moral: suele explicarse por mecanismos sociales de la situación.

### 6.2. Orígenes experimentales

En el trabajo clásico de **Darley y Latané (1968)**, participantes que creían estar solos ante una emergencia (simulación de crisis) reportaban ayuda con mucha más frecuencia y velocidad que quienes creían que había otros oyentes. Hallazgo clave: la presencia percibida de otros **difunde la responsabilidad**.

### 6.3. Mecanismos principales

1. **Difusión de responsabilidad:** “alguien más llamará / ayudará”.  
2. **Ignorancia pluralista:** si nadie actúa, cada uno interpreta que “no debe ser tan grave”.  
3. **Influencia social / miedo a equivocarse:** temor a intervenir mal frente a desconocidos.  
4. **Evaluación de competencia ajena:** si parece haber alguien “más capaz”, otros se retraen.

### 6.4. Relevancia en emergencias médicas reales

En paros cardíacos extrahospitalarios y escenarios de reanimación, la evidencia clínica y de encuestas muestra que:

- la intervención temprana de testigos (p. ej. RCP) mejora supervivencia y desenlace neurológico;
- aun así, la presencia de múltiples bystanders puede **reducir** la proporción de personas que ejecutan alguna acción de rescate frente a quien está solo ante la escena;
- barreras adicionales: pánico, duda diagnóstica (“¿es un paro?”), miedo a no saber RCP/DEA, y espera de que “venga alguien capacitado”.

Un estudio reciente por encuesta a laicos que enfrentaron emergencias reales reportó acciones de rescate en **95,7%** cuando no había otras personas presentes, frente a **73,8%** cuando sí las había (Circ Rep, 2025). Aunque el contexto cultural no es argentino, el patrón es consistente con el modelo del efecto espectador.

### 6.5. Aplicación al caso argentino / vía pública

En una emergencia en la calle (colapso, accidente, persona inconsciente):

- puede haber varios testigos;
- cada uno puede asumir que otro ya llamó al 107;
- se pierde tiempo en ambigüedad (“¿llamo yo?”, “¿es grave?”, “¿habrá una ambulancia cerca?”);
- si la víctima tiene prepaga, es aún menos probable que un desconocido conozca su cobertura o el número correcto de su cartilla.

### 6.6. Implicancias de diseño para Xpedit

| Problema del efecto espectador | Respuesta de producto |
|---|---|
| Nadie se siente dueño de llamar | El afiliado puede autoactivar (o un contacto designado) con protocolo claro |
| Duda sobre gravedad / qué hacer | Flujo de **confirmación explícita** (deslizar) reduce falsas alarmas sin depender del consenso social |
| Desconocimiento de la cobertura de la víctima | La ficha pre-cargada viaja con la alerta |
| Retraso por “esperar a que otro actúe” | Activación personal + GPS + reglas de cobertura acorta la cadena |
| Escena pública caótica | Menos dependencia de improvisación de terceros |

**Conclusión parcial:** el efecto espectador refuerza la tesis de que, en emergencias públicas, un canal **personal, preconfigurado y confirmable** puede ser más robusto que depender únicamente de la buena voluntad situacional de desconocidos.

---

## 7. Síntesis: dónde encaja Xpedit en el mapa

```text
Causas de muerte (Argentina)
        │
        ├─ Circulatorias / respiratorias  →  eventos agudos tiempo-dependientes
        ├─ Causas externas (15–34)        →  trauma / vía pública / terceros presentes
        └─ Tumores / crónicos             →  menor core de activación SOS (salvo complicaciones)
                │
                ▼
     Necesidad de ambulancia / derivación correcta
                │
                ├─ Canal público 107/911
                ├─ Prepaga / obra social / ambulancia privada
                └─ Fricción: ¿a quién llamo? ¿quién decide? ¿quién tiene los datos?
                │
                ▼
     Xpedit: activación confirmada + ficha + cobertura + prestador correcto
                │
                └─ Mitiga también demoras por efecto espectador en vía pública
```

### 7.1. Contextos de alto encaje (prioridad de validación)

1. Emergencia cardiovascular o respiratoria en domicilio, con prepaga.  
2. Emergencia de un familiar a cargo.  
3. Colapso / evento agudo fuera del hogar, cuando el usuario puede confirmar o un allegado conoce el protocolo.  
4. Usuario que hoy dudaría entre 107 y número de prepaga.

### 7.2. Contextos de encaje parcial o condicionado

1. Accidente de tránsito con múltiples testigos (útil si hay activación personal/allegado; no resuelve sola la escena).  
2. Urgencias no vitales que igual requieren traslado coordinado.

### 7.3. Contextos fuera de foco inicial

1. Prevención primaria de ENT / cáncer.  
2. Crisis de salud mental / ideación suicida (requiere abordajes y líneas específicas).  
3. Sustitución absoluta del sistema público de emergencias.

---

## 8. Conclusiones

1. El perfil de mortalidad argentino está dominado, hace décadas, por **circulatorias, respiratorias y tumores**; en jóvenes, por **accidentes y suicidios**.  
2. Para Xpedit, el puente útil no es “todas las muertes”, sino los **eventos agudos** que disparan necesidad de ambulancia y sufren fricción de cobertura.  
3. El **efecto espectador** explica parte del retraso en emergencias públicas y fortalece el valor de una activación personal con confirmación y datos previos.  
4. La propuesta de valor “**donde corresponde, cuando importa**” es coherente con este mapa: precisión de prestador + tiempo + reducción de ambigüedad social/operativa.  
5. El siguiente paso natural de investigación empírica es contrastar este marco con la **encuesta de validación** (filtros + aceptación del flujo de 3 pulsaciones / confirmación / ficha médica).

---

## 9. Referencias y fuentes

### Mortalidad y estadísticas argentinas
1. Ministerio de Salud de la Nación — DEIS: datos de defunciones. https://www.argentina.gob.ar/salud/deis/datos/defunciones  
2. Instituto Nacional del Cáncer — estadísticas de mortalidad. https://www.argentina.gob.ar/salud/instituto-nacional-del-cancer/estadisticas/mortalidad  
3. Observatorio de Salud (ISALUD): *Principales causas de muerte en la Argentina, 2014–2024*. https://observatoriodesalud.isalud.edu.ar/posts/principales-causas-de-muerte-en-la-argentina-2014-2024  
4. Compilación documental del equipo Xpedit a partir de `argentina.gob.ar` y literatura de transición epidemiológica (RASP / RELAP / revisiones citadas en la investigación interna).  
5. *Medicina (Buenos Aires)* — trabajos sobre mortalidad y COVID-19 en Argentina (serie citada en la recopilación).

### Efecto espectador e intervención en emergencias
6. Darley, J. M., & Latané, B. (1968). *Bystander intervention in emergencies: Diffusion of responsibility.* Journal of Personality and Social Psychology.  
7. Evidencia clínica sobre RCP iniciada por bystanders en fibrilación ventricular extrahospitalaria (literatura clásica de reanimación; p. ej. series tipo Copley / Cobb).  
8. Circ Rep (2025). *Influence of the Presence of Other People on Performing Rescue Actions in Emergency Situations* — menor proporción de acciones de rescate con múltiples presentes.  
9. Estudios contemporáneos sobre disposición a usar DEA / barreras de bystanders en paro cardíaco extrahospitalario (p. ej. Heliyon, 2024).

---

## 10. Anexo — Notas para el equipo de producto

- Usar este informe como **marco de problema**, no como claim publicitario cuantitativo cerrado.  
- En comunicación externa, preferir formulaciones del tipo: “las emergencias cardiovasculares y respiratorias concentran una parte crítica de la mortalidad argentina” antes que cifras exactas no auditadas comercialmente.  
- En validación con usuarios, indagar especialmente escenarios A/B/D de la sección 5.2 y barreras del efecto espectador (“¿quién llamaría si colapsás en la calle?”).

---

*Xpedit Group · Informe de investigación aplicada v1.0 · septiembre 2026*  
*Eslogan de referencia: Donde corresponde, cuando importa.*
