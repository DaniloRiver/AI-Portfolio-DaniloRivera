# KPIs del Proyecto de Segmentación de Clientes Bancarios

Este documento describe los principales KPIs calculados en el proyecto.  
Se busca medir el desempeño de campañas de marketing, la retención de clientes y el potencial de ventas cruzadas.

---

## 1. Conversión de campaña
**Definición:** mide el porcentaje de clientes contactados que aceptaron el producto.  
**Fórmula:**  
Conversion Rate = (Clientes con y = "yes") / (Total clientes contactados) * 100

---

## 2. Retención de clientes
**Definición:** mide la proporción de clientes que permanecen activos en cada cluster.  
**Fórmula:**  
Retention Rate = (Clientes con y = "yes" en cluster) / (Total clientes en cluster) * 100

---

## 3. Cross-selling index
**Definición:** promedio de productos contratados por cliente dentro de cada cluster.  
**Fórmula:**  
Cross-Selling Index = (Total productos en cluster) / (Total clientes en cluster)

---

## 4. Customer Lifetime Value (CLV)
**Definición:** valor estimado de un cliente a lo largo de su relación con el banco.  
**Fórmula aproximada usada en este proyecto:**  
CLV = balance * previous * factor

Donde:  
- balance = saldo o ingreso promedio del cliente  
- previous = número de productos o interacciones previas  
- factor = ajuste definido (ejemplo: 0.1)

---

## 5. Reporte final
Los KPIs se consolidan en un archivo CSV dentro de la carpeta `outputs/reports.csv`, que puede ser cargado a **Power BI** para su visualización.
