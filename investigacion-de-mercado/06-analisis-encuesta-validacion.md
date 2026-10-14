# Análisis de encuesta de validación

**Proyecto:** Xpedit Group  
**Fecha de análisis:** octubre 2026  
**N:** 384 respuestas  
**Fuente:** Google Forms — *Encuesta de validación*  
**Archivo:** [dashboard-encuesta/Encuesta de validación.csv](dashboard-encuesta/Encuesta%20de%20Validación.csv)    
**Modelo de negocio de referencia:** SaaS bandera blanca para obras sociales / prepagas  

**Dashboard interactivo:** [dashboard-encuesta/dashboard-encuesta.html](dashboard-encuesta/dashboard-encuesta.html)  
Lee el CSV en vivo con [`dashboard.js`](dashboard-encuesta/dashboard.js) (sin datos hardcodeados).

---

## KPIs y gráficos

> Vista estilo Power BI: abrí el [dashboard](dashboard-encuesta/dashboard-encuesta.html) con un servidor local para ver KPIs y Chart.js calculados desde el CSV.

| KPI | Valor |
|---|---:|
| Respuestas (N) | **384** |
| Alta intención (utilidad ≥ 4 y intención ≥ 4) | **60%** |
| Quiere respaldo de OS / prepaga | **50%** |
| Dolor principal = demora | **60%** |
| Cobertura OS + prepaga | **82%** |
| Media utilidad de la idea (1–5) | **3,96** |
| Media intención de uso (1–5) | **4,01** |
| Utilidad ≥ 4 | **70%** |

```bash
cd investigacion-de-mercado/dashboard-encuesta
node server.js
# http://localhost:8080/dashboard-encuesta.html
```

---

## 1. Objetivo del análisis

Contrastar las hipótesis de validación (dolor, utilidad del flujo, confianza, intención de uso y canal de respaldo) con datos reales de afiliados y potenciales usuarios, para orientar:

1. el **buyer persona B2B** (quién compra el SaaS), y  
2. el **usuario final** (quién usa el módulo dentro de la app de su cobertura).

---

## 2. Metodología

- Encuesta estructurada: 7 filtros + 10 preguntas de validación (+ abierta).  
- Análisis de frecuencias, medias en escalas 1–5 y lectura de respuestas abiertas.  
- **Muestra primaria (v1):** tiene prepaga u obra social + vive en CABA / GBA / Mar del Plata + usa smartphone → **n = 224**.  
- El resto se usa como contraste (público puro, otras provincias).

---

## 3. Perfil de la muestra (N = 384)

### 3.1. Cobertura

| Respuesta | n | % |
|---|---:|---:|
| Sí, obra social | 192 | 50% |
| Sí, prepaga | 124 | 32% |
| No, solo sistema público | 64 | 17% |
| Prefiero no decirlo | 4 | 1% |

**Lectura:** 82% tiene cobertura privada/institucional (OS o prepaga). Buena base para un producto B2B2C vía financiadores.

### 3.2. Zona

| Zona | n |
|---|---:|
| Mar del Plata | 116 |
| Otra provincia | 100 |
| GBA | 92 |
| CABA | 56 |
| Interior PBA (otra ciudad) | 16 |
| Prefiere no decirlo | 4 |

### 3.3. Edad

| Rango | n |
|---|---:|
| 46–60 | **176** |
| 28–45 | 112 |
| Más de 60 | 56 |
| 18–27 | 40 |

**Hallazgo:** la muestra es **más adulta** de lo esperado en el persona provisional (28–45). El núcleo empírico se acerca a **46–60**.

### 3.4. Smartphone y urgencia reciente

- Usa smartphone habitualmente: **372 / 384**  
- Urgencia/emergencia en últimos 24 meses (propia o a cargo): Sí 132 · No 220 · No seguro/a 32  

---

## 4. Comportamiento actual ante una urgencia

### 4.1. Primer paso

| Acción | n | % |
|---|---:|---:|
| Llamar al 107 / 911 | 160 | 42% |
| Ir por medios propios a clínica/hospital | 140 | 36% |
| Llamar a prepaga / obra social | 76 | 20% |
| Llamar ambulancia privada | 8 | 2% |

**Lectura:** aunque tengan cobertura, **pocos activan primero a su OS/prepaga**. Dominan 107 y “arreglárselas”. Eso es fricción comercial para el financiador y oportunidad para un módulo embebido en *su* app.

### 4.2. Claridad del primer paso (1–5)

- Media: **3,01** · Mediana: 3  
- Distribución polarizada (muchos en 1 y en 5)

Hay incertidumbre real, no consenso de que “todos saben qué hacer”.

### 4.3. Usuario principal percibido de una solución así

| Quién | n |
|---|---:|
| Yo | 168 |
| Yo y mi pareja | 140 |
| Familiar a cargo | 72 |
| Nadie | 4 |

Uso individual y de pareja; también relevante el rol de cuidador.

---

## 5. Dolores y valor percibido

### 5.1. Problema que más preocupa

| Problema | n | % |
|---|---:|---:|
| Que tarde en llegar la ayuda | **232** | **60%** |
| Tener que dar datos médicos/cobertura en el momento | 44 | 11% |
| Ninguno me preocupa especialmente | 40 | 10% |
| No saber a qué número llamar | 32 | 8% |
| No poder explicar bien la ubicación | 20 | 5% |
| Derivación a lugar que no corresponde a cobertura | **16** | **4%** |

**Hallazgo crítico:** el dolor #1 es **demora / velocidad**, no la derivación incorrecta.  
El claim “solo prestador correcto” **no alcanza** como mensaje principal. Debe integrarse a: *más rápido, dentro de la red correcta*.

### 5.2. Experiencia de fricción 107 ↔ cobertura privada

| Respuesta | n |
|---|---:|
| No, pero lo veo plausible | 172 |
| Sí, le pasó a alguien cercano | 140 |
| No y no me parece un problema frecuente | 40 |
| Sí, me pasó a mí | 32 |

**344 / 384** lo vivieron, lo vieron de cerca o lo consideran plausible.

### 5.3. Qué valoran más

| Preferencia | n |
|---|---:|
| Velocidad aunque no sea prestador de cartilla | **192** |
| Ambos por igual (velocidad + prestador correcto) | **172** |
| No sabría elegir | 16 |
| Prestador correcto aunque tarde un poco más | **4** |

Velocidad gana, pero “ambos” está muy cerca. El sweet spot de producto/comunicación es **ambos**: rapidez *en* la red de cobertura.

---

## 6. Validación de la solución

### 6.1. Escalas (1–5)

| Pregunta | Media | Mediana | n con ≥ 4 | n con = 5 |
|---|---:|---:|---:|---:|
| Utilidad de la idea (3 pulsaciones + confirmación) | 3,96 | 5 | 268 (70%) | 220 (57%) |
| Comodidad cargando ficha médica anticipada | 4,03 | 5 | 284 (74%) | 232 (60%) |
| Intención de instalar / completar ficha (si fuera gratis) | 4,01 | 5 | 280 (73%) | 216 (56%) |

**Alta intención combinada** (utilidad ≥ 4 **y** intención ≥ 4): **232 / 384 (60%)**.

### 6.2. Frenos (respuestas múltiples explotadas)

| Freno | menciones (aprox.) |
|---|---:|
| Ningún freno importante | 136 |
| Privacidad / uso de datos de salud | 132 |
| Preferiría que la ofrezca mi prepaga/obra social | 64 |
| Miedo a activarla por error | 64 |
| No confío en apps nuevas de salud | 20 |
| Prefiero seguir con el 107 | 16 |
| Parece complicada de configurar | 8 |

Privacidad + “que la ofrezca mi cobertura” + miedo a falsa activación son los frenos accionables. El flujo de **confirmación** ya ataca el tercero; el modelo **white-label** ataca los dos primeros.

### 6.3. Quién debería respaldar la solución

| Respaldo | n | % |
|---|---:|---:|
| Mi prepaga u obra social | **192** | **50%** |
| Me da igual, si funciona bien | 132 | 34% |
| Sistema público (107 / ministerio / municipio) | 32 | 8% |
| App independiente especializada | **20** | **5%** |
| Empresa de ambulancias / prestador | 8 | 2% |

**Hallazgo decisivo para el modelo de negocio:** la app independiente casi no genera confianza. El canal natural es la **obra social / prepaga**. Esto valida el pivote a **SaaS bandera blanca**.

---

## 7. Muestra primaria (n = 224)

Filtro: cobertura OS/prepaga + CABA/GBA/MdP + smartphone.

| Indicador | Valor |
|---|---|
| Edad dominante | **46–60 (124/224)** |
| Dolor #1 | Demora (148/224) |
| Primer paso | 107 (96) · por medios (68) · OS/prepaga (56) |
| Respaldo #1 | Prepaga/OS (**108/224**) |
| Media utilidad | 3,91 |
| Media intención | **4,13** |

La muestra primaria confirma el mismo patrón que el total, con intención levemente más alta.

---

## 8. Temas de respuestas abiertas

Se repiten, en orden aproximado de frecuencia:

1. **Confianza / respaldo institucional** (obra social, prepaga, “aprobada”, “verificada”)  
2. **Privacidad y seguridad de datos**  
3. **Rapidez / eficacia / que no falle**  
4. **Facilidad de uso** (incl. personas mayores)  
5. Confirmación humana / trazabilidad (“que me llamen de la OS para confirmar”)  
6. Testimonios / prueba de que funciona  

Citas representativas (paraíso):

- *“Que esté respaldada oficialmente por mi prepaga y garantice la total privacidad…”*  
- *“Que la promueva mi obra social.”*  
- *“Que tenga relación con mi obra social… así me quedo más tranquila y en confianza.”*  
- *“Que funcione sin internet… sea rápida de activar y no falle nunca.”*  
- *“Que el de la obra social me llame para corroborar que la ambulancia tomó mi pedido…”*

---

## 9. Conclusiones para el negocio

1. **Hay demanda de utilidad e intención** (≈60% alta intención combinada).  
2. El dolor dominante es **tiempo**, no solo “lugar correcto”.  
3. La confianza se ancla en la **cobertura**, no en una marca app independiente.  
4. Por tanto, el modelo correcto no es freemium B2C, sino **SaaS white-label B2B2C**.  
5. Mensaje de valor unificado:  
   > Activación más rápida de la emergencia, dentro de la red de prestadores de la cobertura, con confirmación y datos listos — embebido en la app que el afiliado ya usa.

### Implicancias de producto (white-label)

| Insight encuesta | Implicancia |
|---|---|
| Quieren que lo ofrezca la OS/prepaga | SDK / módulo white-label en app del financiador |
| Privacidad | Datos bajo gobierno del financiador; messaging de custodia |
| Miedo a activación accidental | Mantener confirmación explícita (deslizar) |
| Demora = dolor #1 | Optimizar tiempo a despacho + feedback de estado |
| Adultos 46–60 | UX simple, tipografía clara, pocos pasos |
| Pocos llaman primero a su cobertura | El módulo debe ser el atajo obvio dentro de *su* app |

---

## 10. Próximos documentos

- [07-buyer-persona-b2b-white-label.md](07-buyer-persona-b2b-white-label.md)  
- [08-usuario-final-actualizado.md](08-usuario-final-actualizado.md)  

---

*Xpedit Group · Análisis de encuesta · octubre 2026*
