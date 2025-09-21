# src/eda.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def summarize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera un resumen estadístico básico del dataset.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada.
        
    Returns:
        pd.DataFrame: Estadísticas descriptivas.
    """
    print("===== Info del DataFrame =====")
    print(df.info())
    
    print("\n===== Estadísticas Descriptivas =====")
    print(df.describe(include='all').T)
    
    print("\n===== Valores Nulos =====")
    print(df.isnull().sum())
    
    return df.describe(include='all').T

def plot_distributions(df: pd.DataFrame, numeric_cols: list = None):
    """
    Crea histogramas y boxplots para las variables numéricas.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada.
        numeric_cols (list, opcional): Columnas numéricas a graficar. Si es None, se detectan automáticamente.
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    for col in numeric_cols:
        fig, axes = plt.subplots(1, 2, figsize=(12,4))
        sns.histplot(df[col], kde=True, ax=axes[0])
        axes[0].set_title(f'Histograma de {col}')
        
        sns.boxplot(x=df[col], ax=axes[1])
        axes[1].set_title(f'Boxplot de {col}')
        
        plt.tight_layout()
        plt.show()

def plot_correlation(df: pd.DataFrame):
    """
    Genera un heatmap de correlación entre variables numéricas.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada.
    """
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    corr = df[numeric_cols].corr()
    
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Mapa de correlación")
    plt.show()

import plotly.express as px

def plot_categorical_counts(df, cat_cols=None):
    if cat_cols is None:
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    for col in cat_cols:
        # Contar valores y renombrar columnas
        df_count = df[col].value_counts().reset_index()
        df_count.columns = [col, 'count']  # renombramos para Plotly

        fig = px.bar(
            df_count,
            x=col,
            y='count',
            title=f'Conteo de {col}',
            labels={col: col, 'count': 'Count'}
        )
        fig.show()




import pandas as pd
import plotly.express as px

def plot_churn_analysis(df: pd.DataFrame, churn_col: str = 'Churn'):
    """
    Analiza la variable objetivo 'Churn' en relación con otras variables.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada.
        churn_col (str): Nombre de la columna objetivo.
    """
    if churn_col not in df.columns:
        raise ValueError(f"La columna '{churn_col}' no existe en el DataFrame.")
    
    # Distribución de Churn
    fig = px.pie(df, names=churn_col, title='Distribución de Churn')
    fig.show()
    
    # Análisis de Churn vs Variables Numéricas
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if churn_col in numeric_cols:
        numeric_cols.remove(churn_col)
    
    for col in numeric_cols:
        fig = px.box(df, x=churn_col, y=col, title=f'Churn vs {col}')
        fig.show()
    
    # Análisis de Churn vs Variables Categóricas
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if churn_col in cat_cols:
        cat_cols.remove(churn_col)
    
    for col in cat_cols:
        # Preparar conteos para evitar errores de Plotly
        df_count = df.groupby([col, churn_col]).size().reset_index(name='count')
        fig = px.bar(df_count, x=col, y='count', color=churn_col, barmode='group',
                     title=f'Churn vs {col}', labels={col: col, 'count': 'Count'})
        fig.show()
