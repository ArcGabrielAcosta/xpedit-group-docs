# Diagrama de casos de uso

**Versión:** inicial  
**Fecha:** octubre 2026  
**Base:** documento de alcance, apartado 2.2  

Primera lectura del piloto: quién participa y qué puede hacer dentro del módulo de emergencias. No reemplaza la especificación de cada caso.

![Diagrama de casos de uso de Xpedit](/diagrams/casos-de-uso.svg)

## Actores

| Actor | Rol en esta etapa |
|---|---|
| Afiliado | Activa, confirma, cancela, carga la ficha y sigue el traslado. El familiar a cargo usa el mismo flujo. |
| Prestador | Recibe el pedido en la central que la cobertura ya contrató. No es una flota de Xpedit. |
| Contacto | Recibe el aviso cuando el envío queda confirmado. |
| Financiador | Obra social o prepaga. Consulta activaciones, tiempos, destinos y cancelaciones. |

## Relaciones

- **«incluye»**. Confirmar el envío dispara el paquete cifrado, la derivación por cartilla y el aviso al contacto. Sin el deslizamiento, esos tres no ocurren.
- **«extiende»**. Cancelar, o dejar vencer la ventana, corta una activación que ya se había abierto.

## Fuera de este diagrama

Operar ambulancias, publicar una app de marca Xpedit y sustituir al 107 quedan fuera de la etapa. El panel no reemplaza el call center ni el ERP de la prepaga.
