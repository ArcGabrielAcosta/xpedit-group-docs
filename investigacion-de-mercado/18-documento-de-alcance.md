# Xpedit Group — Documento de alcance

**Tipo:** Propuesta de proyecto — trabajo final de carrera  
**Carrera:** Análisis de Sistemas — Seminario de Sistemas — Escuela Da Vinci  
**Versión:** 1.0  
**Fecha:** octubre 2026  
**Proyecto:** Xpedit Group — módulo de emergencias de bandera blanca  
**Integrante registrado en esta investigación:** Gabriel Acosta  
**Actualización:** armado con la investigación de mercado (documentos 01 a 08) y el benchmarking de octubre 2026 (documentos 09 a 17)

---

## Tabla de contenidos

- [Xpedit Group — Documento de alcance](#xpedit-group--documento-de-alcance)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [1 Introducción](#1-introducción)
  - [1.1 Objetivo del documento](#11-objetivo-del-documento)
  - [1.2 Descripción del equipo](#12-descripción-del-equipo)
  - [2 Descripción del proyecto](#2-descripción-del-proyecto)
  - [2.1 Nombre](#21-nombre)
  - [2.2 Alcance](#22-alcance)
    - [Funcionalidades](#funcionalidades)
  - [2.3 Tecnología](#23-tecnología)
  - [2.4 Necesidades a satisfacer / oportunidad a ofrecer](#24-necesidades-a-satisfacer--oportunidad-a-ofrecer)
    - [2.4.1 Diferencial competitivo de Xpedit](#241-diferencial-competitivo-de-xpedit)
    - [2.4.2 Alcance de esta etapa](#242-alcance-de-esta-etapa)
  - [2.5 Beneficios esperados](#25-beneficios-esperados)
  - [2.6 Investigación de mercado](#26-investigación-de-mercado)

---

## 1 Introducción

En Argentina, ante una emergencia médica conviven la línea pública 107/911, las obras sociales y prepagas, y los prestadores privados de ambulancia. El afiliado que ya tiene cobertura suele llamar primero al 107 o ir por sus medios a una guardia. En la encuesta de validación (N = 384), el 42% haría eso con el 107 y el 36% iría por sus medios; solo el 20% llamaría primero a su obra social o prepaga. El problema que más preocupa es que la ayuda tarde (60%). La derivación a un lugar fuera de la cartilla preocupa al 4%.

Ese primer paso es confuso (claridad media 3,01 sobre 5) y el sistema que recibe el llamado está cargado de demanda que no es riesgo de vida. En el relevamiento de guardias privadas, cerca del 2,6% de las consultas califica como emergencia real. El resto satura líneas y centrales. Cuando el caso sí es crítico —síncope, disnea, choque, dolor de pecho, confusión aguda— el afiliado pierde minutos explicando ubicación, cobertura y datos clínicos.

La oferta se ajustó con esa evidencia. La presentación inicial describía una aplicación propia de Xpedit. La encuesta cambió el canal: el 50% confía si la solución la ofrece su cobertura, y el 5% si es una app independiente. Xpedit queda definido como un SaaS de bandera blanca. El afiliado no instala otra aplicación. Activa la emergencia desde la app de su obra social o prepaga, con el teléfono bloqueado, y el módulo envía ficha, GPS y cobertura al prestador de esa red.

La solución de esta etapa tiene tres capas:

- **Mobile:** módulo embebido en la app del financiador. Triple pulsación con la pantalla bloqueada, confirmación y seguimiento.
- **Backend:** API de despacho, reglas de cartilla, custodia de la ficha y entrega del pedido a la central que la cobertura ya opera.
- **Web:** panel de la obra social o prepaga, con activaciones, tiempos, destinos y cancelaciones.

Xpedit no opera ambulancias. El pedido, ya confirmado, entra al despacho del prestador contratado.

## 1.1 Objetivo del documento

Este documento define la solución propuesta para esa fricción: alcance, funcionalidades, límites tecnológicos y lectura de mercado del proyecto que se desarrolla en el Seminario de Sistemas.

Refleja el estado a octubre de 2026, en coherencia con la encuesta, los estudios de urgencias, el SCAMPER, la matriz de características y las fichas de competencia (documentos 04 a 17 de esta carpeta). Xpedit figura aquí como oferta diseñada, ya que todavía no es un producto en el mercado.

## 1.2 Descripción del equipo

**Integrante:** Gabriel Acosta

Experiencia, conocimientos y necesidades de capacitación del equipo no están descriptos en la investigación de mercado. Esta sección conserva el lugar del formulario para completar esas fichas con los integrantes del trabajo final.

---

## 2 Descripción del proyecto

## 2.1 Nombre

Xpedit Group — módulo de emergencias de bandera blanca para obras sociales y prepagas.

Eslogan de referencia: **Donde corresponde, cuando importa.**

## 2.2 Alcance

El proyecto consiste en un módulo de activación de emergencias que la obra social o la prepaga incorpora en su propia app, y en el backend que entrega ese pedido a la red de prestadores que ella ya contrató.

El afiliado confirma la alerta con un gesto. Viajan la ficha cargada de antemano, la cobertura y la ubicación. La marca visible es la de la cobertura. Un panel le deja a la organización ver qué se activó, en cuánto tiempo y hacia dónde.

La primera entrega comercial es un piloto: una región o un segmento, antes de un despliegue nacional.

### Funcionalidades

| Nombre de la funcionalidad | Descripción de la funcionalidad | Tipificación (ABM, reporte, lógica de negocio) | Aplica a Web, Mobile o ambas |
|---|---|---|---|
| Módulo en la app del financiador | El gesto y la ficha viven en la app de la obra social o prepaga. Xpedit puede figurar como proveedor discreto; la marca de la pantalla es la de la cobertura | Lógica de negocio | Mobile y Backend |
| Activación con pantalla bloqueada | Tres pulsaciones del botón de bloqueo abren la ventana sin tener que buscar la app ni desbloquear el teléfono para empezar | Lógica de negocio | Mobile |
| Confirmación, tiempo de cierre y cancelación | Solo el deslizamiento envía la alerta. Una pulsación adicional cancela. Sin acción, la ventana se cierra a los 10 segundos y no sale ningún aviso | Lógica de negocio | Mobile |
| Atajo en la home | Además del teléfono bloqueado, la emergencia queda accesible desde la home de la app de la cobertura | Lógica de negocio | Mobile |
| Ficha de emergencia | En un momento de calma, el afiliado carga cobertura, alergias, grupo sanguíneo y contacto de emergencia | ABM | Mobile y Backend |
| Paquete de activación | Tras la confirmación se envía un paquete cifrado con ficha, cobertura, contacto y GPS | Lógica de negocio | Mobile y Backend |
| Aviso al contacto | La confirmación notifica al contacto de emergencia designado en la ficha | Lógica de negocio | Mobile y Backend |
| Derivación según cartilla | El destino es un prestador con convenio vigente de esa cobertura, no una flota genérica | Lógica de negocio | Backend |
| Entrega al despacho existente | El pedido entra a la central y a la red que la cobertura ya contrató. Xpedit no despacha móviles propios | Lógica de negocio | Backend |
| Seguimiento | El afiliado ve que el pedido fue tomado, qué prestador fue notificado y el estado del traslado | Lógica de negocio | Mobile y Backend |
| Encuadre de gravedad | El flujo está pensado para el código rojo (síncope, disnea, dolor de pecho, trauma grave y cuadros equivalentes). La confirmación y el encuadre del módulo evitan usarlo como canal de fiebre, tos o malestar menor | Lógica de negocio | Mobile y Backend |
| Panel de la cobertura | Activaciones, tiempos, destinos y cancelaciones para prestaciones, digital y la red de prestadores | Reporte | Web y Backend |
| Gobierno de datos | La custodia sigue la política del financiador. Al prestador viaja el mínimo clínico y de cobertura necesario para salir | Lógica de negocio | Backend |

El mismo flujo sirve cuando quien necesita la ayuda es un familiar a cargo: no es otro producto. La auditoría fina de prestadores y la puerta de medicina laboral quedan como extensión de este módulo, descritas en el apartado 2.4.2.

## 2.3 Tecnología

La investigación fija las capas y las integraciones. No cierra lenguaje, framework ni motor de base de datos: copiar un stack de otro proyecto dejaría esta sección como una decisión que el repositorio todavía no tomó.

| Componente | Definición en esta etapa |
|---|---|
| Mobile | Módulo embebido en la app del financiador (SDK nativo, WebView controlado o equivalente acordado con su equipo). Gesto de pantalla bloqueada, confirmación y seguimiento. Destino: la app que el afiliado ya tiene en Android o iOS |
| Web | Panel de métricas para la obra social o prepaga |
| Backend | API de despacho, motor de reglas de cartilla, persistencia de la ficha y registro de estados |
| Lenguaje y frameworks | A definir en la especificación técnica del trabajo final |
| Base de datos | A definir. Debe sostener ficha, activaciones, estados y métricas del piloto |
| Sistema operativo | Android e iOS como destino del gesto, dentro de la app anfitriona. Servidor para el backend |
| Autenticación | La sesión es la de la app del financiador. El afiliado no crea una cuenta Xpedit |
| Otras APIs | Ubicación del dispositivo; entrega del pedido a la central o al prestador ya contratado; notificación al contacto de emergencia |
| Datos | Paquete cifrado. Custodia alineada al financiador |

El gesto de pantalla bloqueada está en el alcance funcional. La forma concreta de ofrecerlo depende de lo que Android, iOS y la app anfitriona permitan. Esa restricción se resuelve en el diseño técnico, no se da por resuelta en este documento.

## 2.4 Necesidades a satisfacer / oportunidad a ofrecer

Hoy el afiliado depende de una llamada, de un número que no tiene a mano o de ir por sus medios. En ese momento tiene que explicar dónde está, qué cobertura tiene y qué datos clínicos importan. La obra social o la prepaga pierde el primer minuto: el caso se va al 107 o a una guardia, y la central que sí es de su red se entera tarde o no se entera.

La oportunidad es venderle a ese financiador la activación que sus afiliados ya dijeron que usarían si la ofrece su cobertura: más rápida, dentro de la red correcta, con los datos listos y con una confirmación que corta la falsa alarma.

El SCAMPER de octubre 2026 afila esa oferta en cuatro movimientos: sustituir la segunda app y la marca propia por el gesto dentro de la app de la cobertura; combinar ese gesto con la central y la cartilla que el financiador ya tiene; adaptar el gesto de pantalla bloqueada y la integración por API sin heredar una flota; eliminar la decisión, el relato de la ubicación y el aviso que sale sin confirmación.

### 2.4.1 Diferencial competitivo de Xpedit

1. **Activación con el teléfono bloqueado, dentro de la app de la cobertura.**  
   El afiliado no instala ni reconoce una segunda marca en el momento de la emergencia. Inthegra ya ubica un botón en la app de una prepaga, y hay que entrar a la app para usarlo. Shaman AID y Opsi cubren GPS, datos y triage en una app propia del prestador. El gesto de Xpedit ocurre antes de esa búsqueda.  
   Funcionalidades relacionadas: módulo en la app del financiador, activación con pantalla bloqueada, atajo en la home.

2. **Confirmación explícita.**  
   Aura, en Kenia, documenta la triple pulsación y la integración con el seguro. No documenta un segundo gesto que impida el envío. En Xpedit, sin deslizamiento no sale la alerta, y la ventana se cierra sola.  
   Funcionalidad relacionada: confirmación, tiempo de cierre y cancelación.

3. **Ficha y GPS en el mismo paquete, con la marca del financiador.**  
   Alergias, grupo, cobertura y contacto se cargan en calma. La ubicación viaja con el pedido. La custodia queda bajo la obra social o prepaga, que es quien la encuesta señala como respaldo de confianza (50%, frente al 5% de una app independiente).  
   Funcionalidades relacionadas: ficha de emergencia, paquete de activación, gobierno de datos.

4. **Derivación por cartilla, sin flota propia.**  
   Rescue.co y RED Health acercan el botón de emergencia y operan ambulancias. En Argentina esa flota ya tiene dueño (prestadores privados o la propia prepaga). Xpedit termina cuando el pedido confirmado entra al despacho contratado, elegido según el convenio vigente.  
   Funcionalidades relacionadas: derivación según cartilla, entrega al despacho existente.

5. **La central que ya existe sigue siendo la central.**  
   Inthegra opera el call center además del software. Shaman y Opsi despachan la red de quien los contrata. Xpedit no pide reemplazar el ERP ni el conmutador: alimenta ese ecosistema con un pedido que ya trae ubicación, ficha y cobertura.  
   Funcionalidad relacionada: entrega al despacho existente.

6. **El módulo es para el vértice crítico.**  
   El dolor que la encuesta prioriza es la demora, y el volumen que satura las líneas es la demanda no crítica. El flujo se ofrece para el código rojo y muestra el estado del pedido, en lugar de convertirse en un atajo para cualquier malestar.  
   Funcionalidades relacionadas: encuadre de gravedad, seguimiento, panel de la cobertura.

### 2.4.2 Alcance de esta etapa

Esta primera etapa entrega el módulo de activación, la ficha, la derivación por cartilla, la entrega a un despacho ya contratado y el panel del piloto.

Queda fuera de esta etapa:

- Operar ambulancias o armar una flota.
- Sustituir al 107/911 cuando el caso es de riesgo vital y esa es la vía que corresponde.
- Usar el módulo como canal de medicina domiciliaria o de consultas menores (fiebre, tos, malestar general).
- Reemplazar el call center, el ERP o la suite de gestión de la prepaga.
- Publicar una app de marca Xpedit para que el afiliado la descargue por su cuenta.
- Construir un módulo de telemedicina para desviar el código verde. El encuadre de gravedad evita ese uso; no incluye la consulta médica a distancia.
- Facturación fiscal del servicio médico. El modelo de esta etapa es la licencia del SaaS hacia el financiador.

Quedan como extensión del mismo módulo, no como otro producto: la auditoría de prestadores a partir de tiempos y destinos, la activación pensada para medicina laboral y empresas, y una línea comercial distinta para el familiar a cargo. El familiar puede usar el flujo de esta etapa si la ficha ya lo prevé; no se diseña un producto separado para ese rol.

## 2.5 Beneficios esperados

**Situación actual**

- El primer reflejo es el 107 o ir por los propios medios, aunque exista cobertura.
- Hay que explicar ubicación, datos clínicos y cartilla durante la crisis.
- La claridad del primer paso es media y está polarizada: parte de los afiliados está segura y parte no sabe qué hacer.
- Las líneas y las guardias se saturan con demanda que no es riesgo de vida.
- Una app nueva de un tercero genera poca confianza. Privacidad, miedo a activar por error y preferencia por la propia cobertura son los frenos que la encuesta deja a la vista.
- La obra social o la prepaga tiene poca trazabilidad de ese primer minuto.

**Situación post implementación**

- La emergencia se activa desde la app que el afiliado ya tiene, con la marca de su cobertura.
- Un gesto y una confirmación reemplazan la decisión de a qué número llamar.
- La ficha, la cobertura y el GPS salen juntos, cifrados, hacia el prestador de la cartilla.
- Sin confirmación no hay aviso. La ventana se cierra sola.
- El afiliado ve que el pedido fue tomado y qué prestador responde.
- El contacto de emergencia designado recibe el aviso.
- La cobertura mide activaciones, tiempos, destinos y cancelaciones en el piloto.
- El 107 sigue disponible para el caso en que esa sea la vía correcta.

## 2.6 Investigación de mercado

El análisis de octubre 2026 cruza la encuesta de afiliados con siete ofertas. Los criterios cuantitativos, definidos en el benchmark, son ocho: pantalla bloqueada, confirmación explícita, GPS en la activación, datos precargados, triage, módulo embebido en la app del financiador, derivación según cobertura y ausencia de flota propia. Sobre ese cruce, ninguna oferta documentada reúne las ocho. Xpedit ocupa ese espacio como diseño, no como producto ya vendido.

La tabla siguiente traduce ese cruce al formato de comparación del formulario: qué hace hoy cada oferta, qué hace la propuesta y por qué la diferencia importa.

| Nombre de la aplicación del mercado | Funcionalidad de la aplicación presente en el mercado | Funcionalidad de la aplicación propuesta | Justificación de las diferencias |
|---|---|---|---|
| Inthegra | Suite de gestión para prepagas y obras sociales, con botón de emergencias dentro de la app de Sancor Salud y call center propio. También llega al prestador (Grupo EMI). No documenta pantalla bloqueada, confirmación, GPS del afiliado en el gesto ni ficha precargada | Módulo chico de activación sobre la app y la central que el financiador ya tiene: pantalla bloqueada, confirmación, ficha y entrega del pedido a esa red | Inthegra ya está en el lugar comercial que Xpedit busca. El cambio de su ERP es una decisión pesada. La diferencia de esta etapa es el gesto con el teléfono bloqueado y la confirmación, sin pedir que abandonen Oracle ni la central |
| Shaman SGE (Shaman AID) | App propia del prestador, configurable como bandera blanca. GPS, datos del afiliado y triage. Cartera relevada: Fenix Salud, Samak, +vida y PAMI. Despacha la red de quien lo contrata | El mismo paquete de datos y ubicación, disparado desde la app de la cobertura, con confirmación, y entregado a ese despacho si la red ya usa Shaman | Shaman cubre la operación del prestador. El afiliado suma una segunda app. Xpedit no disputa ese CAD: mueve el gesto a la aplicación que el afiliado ya abre |
| Opsi (Sipeme) | App de afiliados con botón de pánico, GPS, datos y triage, asociada al despacho GEOPSI. Cartera de obras sociales e instituciones (OSDEPYM, IOMA, DASUTEN, ANAR, OSMEBA, OSPCRA, entre otras) | Activación en la app de la cobertura, con confirmación y sin una marca intermedia entre el afiliado y su obra social | Opsi demuestra que el cliente existe y que hoy lo resuelve con una app más. La conversación no es incorporar un botón: es mudar ese gesto a la app de la cobertura |
| Aura | Integración de emergencia en el seguro de Kenia: white-label, API o componentes. Triple pulsación del botón de bloqueo, despacho y seguimiento. Sin confirmación, ficha clínica ni triage por códigos documentados | El mismo tipo de gesto, más confirmación, ficha precargada y derivación a la cartilla argentina, dentro de la app del financiador | Aura prueba que un financiador puede comprar el gesto. No comparte mercado ni red de prestadores. Se toma como referencia de diseño, no como rival de una licitación local |
| Rescue.co (Flare) | Botón de emergencia en su app y API para incrustarlo en la del seguro. GPS, datos cargados al asociarse, despacho y coordinación del destino. Opera flota (ambulancias terrestres, rescate aéreo y en ruta) en África oriental | La forma de integración: el SOS dentro de la app del seguro, con ficha y GPS, entregado a una flota que ya existe en Argentina | El paquete de datos y seguimiento es el que un financiador espera ver. La flota es el centro del negocio de Rescue.co y queda fuera del proyecto |
| RED Health | Botón SOS en una app propia, despacho con triage y flota en India. Venden el servicio a aseguradoras y, a la vez, operan las ambulancias. El producto empresarial visible es RED Assist; el despacho, HeartbeatX | Activación desde el teléfono bloqueado, en la app del financiador, con el caso entregado a una flota ya contratada | RED Health muestra que una empresa paga por un botón asociado a una red que responde. El seguro no es dueño del gesto dentro de su aplicación, y el modelo de flota propia no se traslada a la cartilla argentina |
| RapidSOS Health | API para que la aseguradora, en Estados Unidos, se entere cuando el afiliado entra al 911 o a una guardia, y para enriquecer ese llamado con datos de salud y ubicación. Puede orientar a un centro de la red. No despacha una ambulancia privada ni pone un botón en la app de la cobertura | Activación de la red de la cobertura cuando el caso corresponde a esa red. El 107 permanece como canal cuando el riesgo vital pide la vía pública | RapidSOS marca el límite del mapa: comparte al financiador como cliente y no comparte el servicio. Sirve para recordar que Xpedit no sustituye la línea pública |
| Xpedit Group (nosotros) | Oferta diseñada, todavía no comercializada. En el benchmark reúne las ocho características evaluadas: pantalla bloqueada, confirmación, GPS, ficha, encuadre de gravedad, módulo en la app del financiador, derivación por cobertura y ausencia de flota | Activación confirmada desde el teléfono bloqueado, dentro de la app de la obra social o prepaga, con ficha y GPS, derivada al prestador de la cartilla y visible para la cobertura en un panel | La posición queda en el cruce que la matriz de octubre 2026 deja vacío. El respaldo de demanda es la encuesta: 70% califica la idea con 4 o más, 60% combina utilidad e intención altas, y la confianza se ancla en la cobertura |

---

*Xpedit Group · Documento de alcance v1.0 · octubre 2026*  
*Eslogan de referencia: Donde corresponde, cuando importa.*
