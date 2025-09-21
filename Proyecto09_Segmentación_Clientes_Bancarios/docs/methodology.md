# 🧭 Metodología de Análisis

Este documento describe el proceso seguido para analizar el dataset **Bank Marketing** y generar KPIs y reportes.

---

## 1. Recolección de datos
- Dataset: `bank-additional-full.csv`
- Fuente: UCI Machine Learning Repository
- Tamaño: ~41,000 registros, 20+ variables.

---

## 2. Limpieza y preprocesamiento
- Eliminación de valores desconocidos (`unknown`) o imputación según contexto.
- Conversión de variables categóricas a formato numérico cuando sea necesario.
- Normalización de variables continuas (ej. `duration`, `age`, `euribor3m`).
- Validación de consistencia entre variables de campañas (`campaign`, `previous`, `pdays`).

---

## 3. Definición de KPIs
- Se definieron KPIs centrados en **conversión, eficiencia y costo-beneficio**.
- Cada KPI fue documentado en `kpis.md`.

---

## 4. Generación de reportes
- Scripts en `src/kpi.py` calculan automáticamente los indicadores.
- Resultados exportados a:  
