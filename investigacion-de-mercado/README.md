# Investigación de mercado — Xpedit Group

Carpeta de trabajo para **toda la investigación de mercado** del proyecto.

**Modelo de negocio actual:** SaaS de bandera blanca para obras sociales y prepagas (módulo embebible en sus apps). No freemium B2C con app propia.

## Índice

| # | Archivo | Descripción |
|---|---|---|
| 01 | [01-documento-proyecto.md](01-documento-proyecto.md) | Presentación inicial del proyecto |
| 02 | [02-buyer-persona-provisional-v1.md](02-buyer-persona-provisional-v1.md) | Persona afiliado provisional (pre-encuesta) |
| 03 | [03-diseno-encuesta-validacion.md](03-diseno-encuesta-validacion.md) | Diseño de filtros + preguntas |
| 04 | [04-estudio-poblacion-urgencias-v1.md](04-estudio-poblacion-urgencias-v1.md) | Mortalidad, efecto espectador, encaje |
| 05 | [05-estudio-llamados-emergencias-v2.md](05-estudio-llamados-emergencias-v2.md) | Llamados, código rojo, efecto pirámide |
| 06 | [06-analisis-encuesta-validacion.md](06-analisis-encuesta-validacion.md) | Análisis de encuesta (N=384) + KPIs |
| 07 | [07-buyer-persona-b2b-white-label.md](07-buyer-persona-b2b-white-label.md) | **Buyer / cliente** — obra social / prepaga |
| 08 | [08-usuario-final-actualizado.md](08-usuario-final-actualizado.md) | **Usuario final** afiliado (post-encuesta) |
| 09 | [09-scamper.md](09-scamper.md) | SCAMPER sobre la oferta actual |
| 10 | [10-benchmark.md](10-benchmark.md) | Matriz de características frente a la competencia |
| 11 | [11-analisis-competencia-shaman-sge.md](11-analisis-competencia-shaman-sge.md) | Competencia: Shaman SGE / Shaman AID |
| 12 | [12-analisis-competencia-opsi-sipeme.md](12-analisis-competencia-opsi-sipeme.md) | Competencia: Opsi (Sipeme) |
| 13 | [13-analisis-competencia-inthegra.md](13-analisis-competencia-inthegra.md) | Competencia: Inthegra (principal local) |
| 14 | [14-analisis-competencia-aura.md](14-analisis-competencia-aura.md) | Competencia: Aura (Kenia) |
| 15 | [15-analisis-competencia-rescue-co.md](15-analisis-competencia-rescue-co.md) | Competencia: Rescue.co (Kenia) |
| 16 | [16-analisis-competencia-red-health.md](16-analisis-competencia-red-health.md) | Competencia: RED Health (India) |
| 17 | [17-analisis-competencia-rapidsos.md](17-analisis-competencia-rapidsos.md) | Límite del mapa: RapidSOS Health (EE. UU.) |
| 18 | [18-documento-de-alcance.md](18-documento-de-alcance.md) | Documento de alcance (formato de propuesta de proyecto) |
| — | [dashboard-encuesta/](dashboard-encuesta/) | Dashboard: HTML + CSV + JS (KPIs/gráficos en vivo) |

## Fuente de datos de encuesta

CSV de Google Forms (copia de trabajo del dashboard):

[dashboard-encuesta/Encuesta de validación.csv](dashboard-encuesta/Encuesta%20de%20Validación.csv)

## Dashboard

Carpeta `dashboard-encuesta/`:

| Archivo | Rol |
|---|---|
| `dashboard-encuesta.html` | Shell visual |
| `dashboard.js` | Lee el CSV, calcula KPIs/series y pinta Chart.js |
| `Encuesta de validación.csv` | Fuente de datos |
| `server.js` | Servidor estático Node (sin dependencias) |

```bash
cd investigacion-de-mercado/dashboard-encuesta
node server.js
# http://localhost:8080/dashboard-encuesta.html
```

Si abrís el HTML con `file://`, el navegador puede bloquear el `fetch` del CSV: usá el servidor local o el selector de archivo del propio dashboard.
