# src/kpis.py
import pandas as pd
import os

def calculate_clv(df, balance_col='balance', products_col='previous', factor=0.1):
    """
    Calcula un CLV aproximado para cada cliente.
    Si 'balance_col' no existe en el dataset, usa 'duration' como proxy.

    Args:
        df (pd.DataFrame): DataFrame con datos de clientes
        balance_col (str): columna con saldo o balance
        products_col (str): columna con número de productos
        factor (float): factor para aproximar CLV
    
    Returns:
        pd.DataFrame: DataFrame con nueva columna 'CLV'
    """
    df = df.copy()
    if balance_col not in df.columns:
        print(f"⚠️ Columna '{balance_col}' no encontrada. Usando 'duration' como proxy.")
        balance_col = "duration"

    if products_col not in df.columns:
        print(f"⚠️ Columna '{products_col}' no encontrada. Se crea columna con valor 1.")
        df[products_col] = 1

    df['CLV'] = df[balance_col] * df[products_col] * factor
    return df


def retention_rate(df, cluster_col='cluster', target_col='y_yes'):
    """
    Calcula tasa de retención por cluster.
    
    Args:
        df (pd.DataFrame): DataFrame con clusters
        cluster_col (str): columna que indica cluster
        target_col (str): columna binaria objetivo
    
    Returns:
        pd.DataFrame: cluster y retención promedio
    """
    return df.groupby(cluster_col)[target_col].mean().reset_index(name='retention_rate')


def cross_selling_index(df, cluster_col='cluster', products_col='previous'):
    """
    Calcula promedio de productos contratados por cluster.
    
    Args:
        df (pd.DataFrame): DataFrame con clusters
        cluster_col (str): columna que indica cluster
        products_col (str): columna con número de productos
    
    Returns:
        pd.DataFrame: cluster y promedio de productos
    """
    return df.groupby(cluster_col)[products_col].mean().reset_index(name='cross_selling_index')


def save_kpis(df_kpis, path):
    """
    Guarda un DataFrame de KPIs en CSV.
    
    Args:
        df_kpis (pd.DataFrame): DataFrame a guardar
        path (str): ruta del archivo CSV
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df_kpis.to_csv(path, index=False)
    print(f"✅ KPIs guardados en {path}")
