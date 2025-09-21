# 📊 Segmentación de Clientes Bancarios

## 📌 Contexto de Negocio
En la banca moderna, comprender a los clientes es clave para diseñar **estrategias de retención, cross-selling y fidelización**.  
Este proyecto busca **segmentar clientes bancarios** en grupos homogéneos según sus características, para ofrecerles productos financieros personalizados.

---

## 🎯 Objetivos
- Analizar patrones de comportamiento de los clientes.
- Identificar segmentos claros (ej: ahorradores, inversionistas, deudores).
- Construir un **dashboard interactivo** que permita explorar la segmentación.
- Proporcionar **recomendaciones accionables** al área de marketing.

---

## 🗂️ Dataset
- **Fuente**: [Bank Marketing Dataset - UCI](https://archive.ics.uci.edu/ml/datasets/bank+marketing)  
- **Descripción**: Información de campañas de marketing de una entidad bancaria, con variables como:  
  - Edad, estado civil, educación  
  - Balance promedio en cuenta  
  - Número de productos contratados  
  - Historial de contacto con el banco  

---

## 🛠️ Tecnologías Utilizadas
- **Python** → pandas, numpy, scikit-learn, matplotlib, seaborn  
- **Machine Learning** → K-Means Clustering, PCA  
- **Business Intelligence** → Power BI (dashboard de segmentos)  
- **Versionado** → Git + GitHub  

---

## 📊 Metodología
1. **Exploración y limpieza de datos**  
   - Eliminación de valores nulos y duplicados  
   - Normalización de variables numéricas  

2. **Análisis exploratorio (EDA)**  
   - Distribución de edad, ingresos y productos  
   - Correlaciones  

3. **Modelado de Segmentación**  
   - Selección del número óptimo de clusters (método del codo, silhouette score)  
   - Aplicación de K-Means  
   - Reducción de dimensionalidad con PCA  

4. **Visualización en BI**  
   - Dashboard con KPIs por segmento  
   - Filtros por edad, balance y productos  

---

# 📂 Diccionario de Variables – Bank Additional Dataset

## 📌 Contexto
El dataset **Bank Marketing (bank-additional)** proviene de una campaña de marketing de una entidad bancaria portuguesa, donde se intentaba predecir si los clientes contratarían un **depósito a plazo fijo**.

Es un dataset muy usado en proyectos de **data analysis, data analytics y machine learning** en banca, ya que combina información **demográfica, financiera, de contacto y macroeconómica**.

---

## 🗂️ Descripción de Variables

| Variable          | Tipo        | Descripción                                                                 |
|-------------------|------------|-----------------------------------------------------------------------------|
| `age`             | Numérica   | Edad del cliente (años).                                                    |
| `job`             | Categórica | Tipo de trabajo (ej: admin, technician, services, management, unemployed). |
| `marital`         | Categórica | Estado civil (ej: married, single, divorced).                               |
| `education`       | Categórica | Nivel educativo (ej: basic.4y, high.school, university.degree).             |
| `default`         | Categórica | ¿Tiene crédito en default? (yes, no, unknown).                              |
| `housing`         | Categórica | ¿Tiene préstamo hipotecario? (yes, no, unknown).                             |
| `loan`            | Categórica | ¿Tiene préstamo personal? (yes, no, unknown).                                |
| `contact`         | Categórica | Medio de contacto (cellular, telephone).                                    |
| `month`           | Categórica | Último mes de contacto (ej: may, jun, jul...).                              |
| `day_of_week`     | Categórica | Día de la semana del contacto (mon, tue, wed, thu, fri).                     |
| `duration`        | Numérica   | Duración del último contacto en segundos. ⚠️ Alta influencia en la variable objetivo. |
| `campaign`        | Numérica   | Número de contactos realizados en esta campaña con el cliente.              |
| `pdays`           | Numérica   | Días desde el último contacto previo a esta campaña (-1 = nunca contactado).|
| `previous`        | Numérica   | Número de contactos anteriores antes de esta campaña.                       |
| `poutcome`        | Categórica | Resultado de la campaña de marketing anterior (success, failure, non-existent). |
| `emp.var.rate`    | Numérica   | Tasa de variación del empleo (indicador macroeconómico trimestral).         |
| `cons.price.idx`  | Numérica   | Índice de precios al consumidor (IPC).                                      |
| `cons.conf.idx`   | Numérica   | Índice de confianza del consumidor.                                         |
| `euribor3m`       | Numérica   | Tasa euríbor a 3 meses.                                                    |
| `nr.employed`     | Numérica   | Número de empleados (indicador macroeconómico trimestral).                  |
| `y`               | Binaria    | Variable objetivo: ¿El cliente contrató un depósito a plazo fijo? (yes/no).|

---

## 🎯 Relevancia para Segmentación Bancaria

- **Perfil sociodemográfico** → `age`, `job`, `marital`, `education`.  
- **Riesgo crediticio** → `default`, `housing`, `loan`.  
- **Interacción con el banco** → `contact`, `month`, `day_of_week`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`.  
- **Contexto económico** → `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed`.  
- **Target (Objetivo)** → `y` (etiqueta para clasificación).  

---

## 🚀 Usos en Análisis y Machine Learning

- **Segmentación de clientes** (clustering: K-Means, PCA, DBSCAN).  
- **Modelado de propensión** (clasificación supervisada: Logistic Regression, Random Forest, XGBoost).  
- **Optimización de campañas** → identificar qué segmentos responden mejor.  
- **Análisis de riesgo crediticio** → relacionar préstamos con propensión a contratar productos.

---

## ⚠️ Nota
- La variable `duration` suele eliminarse en modelos predictivos ya que solo se conoce después del contacto y sesga la variable objetivo.  
- Las variables macroeconómicas (`emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed`) aportan contexto externo útil para enriquecer análisis y segmentación.


## 📈 Resultados
- Se identificaron **4 segmentos principales**:  
  1. **Clientes Jóvenes Digitales** – bajos ingresos, alta interacción digital.  
  2. **Ahorradores Conservadores** – saldo estable, bajo endeudamiento.  
  3. **Clientes Premium** – altos ingresos, múltiples productos contratados.  
  4. **Riesgo de Deserción** – bajo balance, poco contacto con el banco.  

- El dashboard permite a gerencia **tomar decisiones de marketing focalizadas**.  

---

## 📊 Dashboard
👉 Capturas del dashboard en Power BI  

![Dashboard de Segmentación](./dashboard/dashboard_preview.png)  

---

## 🚀 Próximos Pasos
- Integrar datos transaccionales en tiempo real.  
- Conectar con un recomendador de productos financieros.  
- Extender el análisis a múltiples países o sucursales.  

---

## 👨‍💻 Autor
- **Danilo Rivera**  
- Portafolio de Business Intelligence, Business Analytics y Machine Learning  
