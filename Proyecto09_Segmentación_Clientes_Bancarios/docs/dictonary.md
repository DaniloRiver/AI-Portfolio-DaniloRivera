# 📖 Diccionario de Datos - Bank Marketing Dataset

Este dataset contiene información de clientes de un banco y los resultados de campañas de marketing telefónico.

---

## Variables de Cliente
- **age**: Edad del cliente (numérica).
- **job**: Tipo de empleo (categórica: "admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown").
- **marital**: Estado civil (categórica: "divorced", "married", "single", "unknown").
- **education**: Nivel educativo (categórica: "basic.4y", "basic.6y", "basic.9y", "high.school", "illiterate", "professional.course", "university.degree", "unknown").
- **default**: ¿Tiene crédito en incumplimiento? (categórica: "yes", "no", "unknown").
- **housing**: ¿Tiene préstamo hipotecario? (categórica: "yes", "no", "unknown").
- **loan**: ¿Tiene préstamo personal? (categórica: "yes", "no", "unknown").

---

## Variables de Contacto
- **contact**: Tipo de comunicación (categórica: "cellular", "telephone").
- **month**: Mes del último contacto (categórica: "jan", "feb", ..., "dec").
- **day_of_week**: Día de la semana del último contacto (categórica: "mon", "tue", "wed", "thu", "fri").
- **duration**: Duración del último contacto, en segundos (numérica). ⚠️ Importante: puede sesgar modelos de predicción.

---

## Variables de Campaña
- **campaign**: Número de contactos realizados durante esta campaña para el cliente (numérica).
- **pdays**: Número de días transcurridos desde el último contacto en una campaña anterior (-1 = nunca contactado).
- **previous**: Número de contactos realizados antes de esta campaña (numérica).
- **poutcome**: Resultado de la campaña de marketing anterior (categórica: "failure", "nonexistent", "success").

---

## Variables Socioeconómicas
- **emp.var.rate**: Tasa de variación del empleo (numérica).
- **cons.price.idx**: Índice de precios al consumidor (numérica).
- **cons.conf.idx**: Índice de confianza del consumidor (numérica).
- **euribor3m**: Tipo de interés Euribor a 3 meses (numérica).
- **nr.employed**: Número de empleados (numérica).

---

## Variable Objetivo
- **y**: Resultado de la campaña actual: ¿El cliente suscribió un depósito a plazo? (binaria: "yes", "no").
