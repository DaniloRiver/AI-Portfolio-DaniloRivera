# 📊 Telco Customer Churn Prediction

Este proyecto tiene como objetivo **analizar y predecir el abandono de clientes (churn)** en una empresa de telecomunicaciones, aplicando técnicas de **Data Analysis, Data Analytics y Machine Learning**.

El dataset utilizado contiene información demográfica, servicios contratados, facturación y si el cliente abandonó o no la compañía.

---

## 📂 Dataset

Dataset: **Telco Customer Churn** (IBM)  
🔗 [Disponible en Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn)

**Columnas principales:**
- `gender`, `SeniorCitizen`, `Partner`, `Dependents`  
- `tenure`, `PhoneService`, `InternetService`, `Contract`, `PaymentMethod`  
- `MonthlyCharges`, `TotalCharges`  
- `Churn` (variable objetivo: Yes/No)

---

## 🧠 Metodología

1. **Data Analysis (EDA)**  
   - Limpieza de datos (valores nulos, duplicados, outliers).  
   - Análisis exploratorio con gráficos (seaborn, matplotlib).  
   - Identificación de patrones en clientes que abandonan vs. permanecen.  

2. **Data Analytics (KPIs & Visualización)**  
   - Tasa de churn mensual y global.  
   - Comparación de ingresos entre clientes que se van y los que se quedan.  
   - Segmentación de clientes en riesgo.  
   - Dashboard sugerido en Power BI o Tableau.  

3. **Machine Learning**  
   - Preparación de datos (encoding, escalado).  
   - Modelos aplicados:  
     - Regresión Logística (baseline).  
     - Random Forest.  
     - XGBoost.  
   - Evaluación con métricas: Accuracy, Precision, Recall, F1-score, AUC-ROC.  
   - Feature importance para explicar qué factores influyen en el churn.  

---

## ⚙️ Tecnologías utilizadas

- **Python** 🐍  
  - pandas, numpy, matplotlib, seaborn  
  - scikit-learn  
  - XGBoost  
- **Power BI / Tableau** (para visualización de KPIs)  
- **Jupyter Notebook / Google Colab**  

---

## 🚀 Ejecución del proyecto

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tuusuario/telco-churn-prediction.git
   cd telco-churn-prediction

Instalar dependencias:

pip install -r requirements.txt


Descargar el dataset de Kaggle y colocarlo en la carpeta raíz del proyecto.

Ejecutar el notebook:

jupyter notebook Telco_Churn_Analysis.ipynb

📊 Resultados esperados

Identificación de los principales factores que explican el abandono de clientes.

Modelos predictivos con métricas comparadas.

Visualizaciones para explicar hallazgos de forma clara y visual.

🔮 Futuras mejoras

Implementar un modelo de red neuronal (Deep Learning).

Desplegar la solución como API REST con FastAPI para predicciones en tiempo real.

Integrar dashboard dinámico en Streamlit.

Optimización con técnicas de Feature Engineering.

✍️ Autor: Danilo


