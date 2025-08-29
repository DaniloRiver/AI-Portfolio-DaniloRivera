# Proyecto de Segmentación de Clientes con Data Science

## 📌 Descripción
Este proyecto tiene como objetivo aplicar **técnicas de ciencia de datos** para segmentar clientes de una empresa minorista en **Seattle, U.S.**, con el fin de crear campañas de marketing personalizadas.  

Se cuenta con más de **2 años y medio de datos de clientes**, y el reto consiste en **identificar al menos 3 segmentos diferentes de clientes** para impulsar ventas, engagement y crecimiento empresarial.

---

## 🎯 Objetivos del Proyecto
- **Educación**: Comunicar de forma clara la propuesta de valor a los clientes.
- **Engagement**: Comprender y conectar con las necesidades de los clientes.
- **Ventas**: Impulsar el tráfico de productos y servicios.
- **Crecimiento**: Ampliar la base de clientes y llegar a nuevos mercados.

---

## 📊 Dataset
El dataset contiene información histórica de pedidos con las siguientes variables principales:

- `ORDERNUMBER`: Identificador del pedido  
- `QUANTITYORDERED`: Número de ítems comprados  
- `PRICEEACH`: Precio de cada ítem  
- `SALES`: Total de ventas efectuadas  
- `ORDERDATE`: Fecha del pedido  
- `STATUS`: Estado del pedido  
- `QTR_ID`: Trimestre del pedido  
- `MONTH_ID`: Mes del pedido  
- `YEAR_ID`: Año del pedido  
- `PRODUCTLINE`: Categoría del producto  
- `CUSTOMERNAME`: Nombre del cliente  
- `PHONE`: Teléfono del cliente  
- `ADDRESSLINE1 / ADDRESSLINE2`: Dirección de envío  
- `CITY`: Ciudad  
- `STATE`: Estado  
- `POSTALCODE`: Código postal  
- `COUNTRY`: País  
- `TERRITORY`: Territorio  
- `DEALSIZE`: Tamaño del pedido  
- `CONTACTFIRSTNAME / CONTACTLASTNAME`: Contacto del cliente  

---

## 🧠 Algoritmos Utilizados

### 🔹 K-Means Clustering
- Algoritmo no supervisado para agrupar clientes según características similares.  
- Se utilizan distancias euclidianas para asignar clientes a clústers.  
- Determinación del número óptimo de clústers mediante el **Método del Codo (Elbow Method)**.

### 🔹 Autoencoders
- Redes neuronales para **aprendizaje no supervisado** y **reducción de dimensionalidad**.  
- Utilizan un **cuello de botella (capa de codificación)** para aprender representaciones comprimidas de los datos.  

### 🔹 Análisis de Componentes Principales (PCA)
- Reducción de dimensionalidad preservando la mayor varianza posible.  
- Útil para visualizar y analizar correlaciones entre variables.  

---

## 🛠️ Tecnologías
- **Python 3.10+**
- Librerías principales:  
  - `pandas`, `numpy` → Manipulación de datos  
  - `matplotlib`, `seaborn` → Visualización  
  - `scikit-learn` → Modelos de ML (K-Means, PCA)  
  - `tensorflow / keras` → Autoencoders  

---

## 📈 Flujo del Proyecto
1. Cargar y explorar el dataset.  
2. Preprocesamiento: limpieza y normalización de datos.  
3. Análisis exploratorio (EDA).  
4. Aplicar **K-Means** con diferentes valores de K → evaluar con método del codo.  
5. Visualización de clústers con PCA.  
6. Entrenar un **Autoencoder** para identificar representaciones comprimidas.  
7. Generar insights de marketing y proponer campañas para cada segmento.  

---

## 🚀 Resultados Esperados
- Identificación de **3 o más segmentos de clientes**.  
- Creación de campañas dirigidas según hábitos de compra.  
- Incremento en engagement y ventas de la empresa.  

---

## 📂 Estructura del Repositorio
📦 marketing-segmentation
┣ 📂 data # Dataset crudo y procesado
┣ 📂 notebooks # Jupyter Notebooks con análisis y modelos
┣ 📂 src # Código fuente (scripts de limpieza y modelos)
┣ 📂 reports # Gráficas, resultados y documentación
┣ README.md # Documentación del proyecto
┗ requirements.txt # Dependencias del proyecto


---

## 📜 Fuente de Inspiración
- [Needpix - Analytics Image](https://www.needpix.com/photo/896541/analytics-data-analytics-graph-chart-analysis-business-data-statistics-analyzing)  
- [Commons Wikimedia - Autoencoder Structure](https://commons.wikimedia.org/wiki/File:Autoencoder_structure.png)  

---

## 👨‍💻 Autores
Proyecto realizado por un equipo de **DaniloDevs**.
