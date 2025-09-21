import pandas as pd
import csv
import os

def load_data(path, sep=None):
    """
    Carga dataset desde un CSV detectando automáticamente el separador
    y normaliza nombres de columnas.
    """
    # Detectar separador si no se pasa manualmente
    if sep is None:
        with open(path, "r", encoding="utf-8") as f:
            sample = f.readline()
            sniffer = csv.Sniffer()
            sep = sniffer.sniff(sample).delimiter

    # Cargar dataset
    df = pd.read_csv(path, sep=sep)

    # Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace('"', '', regex=False)
    )

    return df


def save_clean_data(df, output_path):
    """
    Guarda el DataFrame limpio en un CSV sin comillas extras y con separador ','.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, sep=",", quoting=csv.QUOTE_MINIMAL)


def clean_and_save(path, output_path, sep=None):
    """
    Carga, limpia y guarda automáticamente la versión limpia del dataset.
    """
    df = load_data(path, sep=sep)
    save_clean_data(df, output_path)
    return df


def clean_data(df, drop_cols=None):
    """Elimina columnas innecesarias y filas duplicadas."""
    if drop_cols:
        df = df.drop(columns=drop_cols, errors='ignore')
    df = df.drop_duplicates()
    return df


def encode_categoricals(df, drop_first=True):
    """Convierte variables categóricas a dummies."""
    cat_cols = df.select_dtypes(include=['object']).columns
    df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=drop_first)
    return df_encoded


def scale_features(df, numeric_cols=None):
    """Escala variables numéricas."""
    from sklearn.preprocessing import StandardScaler

    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df
