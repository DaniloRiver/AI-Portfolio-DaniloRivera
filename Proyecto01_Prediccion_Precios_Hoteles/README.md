
# Proyecto 01: Predicción de Precios y Demanda de Hoteles 🏨

## 📌 Descripción
Este proyecto utiliza el dataset **Hotel Booking Demand** disponible en Kaggle, que contiene información sobre **reservas de hoteles** (City Hotel y Resort Hotel) durante varios años.  

El objetivo es aplicar técnicas de **Machine Learning** para:
- Analizar los factores que influyen en la demanda de hoteles.
- Explorar la relación entre variables como ubicación, duración de la estancia, temporada y precios.
- Desarrollar un modelo predictivo para estimar el **precio de una reserva** o la probabilidad de **cancelación**.

---

## 🎯 Objetivos del Proyecto
- Practicar **limpieza y análisis exploratorio de datos (EDA)**.  
- Construir modelos de regresión para predecir precios de reservas.  
- Probar modelos de clasificación para predecir cancelaciones de reservas.  
- Extraer **insights de negocio** para revenue management y estrategias de marketing.  

---

## 📊 Variables del Dataset
Algunas de las variables más relevantes son:

- `hotel` → Tipo de hotel (City Hotel o Resort Hotel).  
- `is_canceled` → Si la reserva fue cancelada (1) o no (0).  
- `lead_time` → Días entre la reserva y la llegada.  
- `arrival_date_year` → Año de llegada.  
- `arrival_date_month` → Mes de llegada.  
- `stays_in_weekend_nights` → Noches reservadas en fin de semana.  
- `stays_in_week_nights` → Noches reservadas entre semana.  
- `adults` / `children` / `babies` → Número de huéspedes.  
- `meal` → Tipo de comida incluida.  
- `country` → País de origen del cliente.  
- `market_segment` → Segmento de mercado (Online, Corporate, etc.).  
- `distribution_channel` → Canal de distribución.  
- `reserved_room_type` → Tipo de habitación reservada.  
- `adr` → Tarifa diaria promedio (Average Daily Rate, precio por noche).  
- `required_car_parking_spaces` → Espacios de estacionamiento solicitados.  
- `total_of_special_requests` → Número de solicitudes especiales.  

---

## 🧠 Algoritmos a Utilizar
- **Regresión Lineal**: Predicción base de precios (`adr`).  
- **Random Forest / Gradient Boosting**: Modelos para relaciones no lineales.  
- **Clasificación**: Predicción de `is_canceled` (reserva cancelada o no).  
- **Clustering (opcional)**: Segmentar clientes en perfiles.  

---

## 🛠️ Tecnologías
- **Python 3.10+**
- Librerías:  
  - `pandas`, `numpy` → Análisis de datos  
  - `matplotlib`, `seaborn` → Visualización  
  - `scikit-learn` → Modelos ML clásicos  
  - `xgboost`, `lightgbm`, `catboost` → Boosting avanzado  
  - `tensorflow/keras` → Modelos neuronales (opcional)  

---

## 📈 Flujo del Proyecto
1. Cargar y explorar el dataset.  
2. Preprocesamiento (limpieza, tratamiento de nulos, codificación de categóricas).  
3. EDA: análisis de precios por hotel, temporada, país, etc.  
4. Modelado predictivo:  
   - Regresión sobre la variable `adr` (precio por noche).  
   - Clasificación de cancelaciones (`is_canceled`).  
5. Evaluación de modelos con métricas:  
   - **Regresión**: MAE, RMSE, R².  
   - **Clasificación**: Accuracy, Precision, Recall, F1.  
6. Conclusiones y recomendaciones.  

---

## 🚀 Resultados Esperados
- Identificación de **patrones de demanda** en hoteles.  
- Predicciones de tarifas diarias (`adr`) con baja desviación.  
- Predicción de cancelaciones con buena precisión.  
- Recomendaciones para mejorar estrategias de **pricing y reservas**.  

---

## 📂 Estructura del Repositorio
📦 Proyecto01_Prediccion_Precios_Hoteles
┣ 📂 data # Dataset crudo y procesado
┣ 📂 notebooks # Jupyter Notebooks con análisis y modelos
┣ 📂 src # Código fuente
┣ 📂 reports # Gráficas y resultados
┣ README.md # Documentación del proyecto
┗ requirements.txt # Dependencias

yaml
Copiar código

---

## 📜 Referencia del Dataset
Dataset utilizado:  
🔗 [Hotel Booking Demand Dataset – Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

---

## 👨‍💻 Autor
Proyecto realizado como práctica de **Data Science aplicado al sector hotelero**.