import pandas as pd
import os

def save_metrics(model_name, accuracy, precision, recall, f1, filepath="outputs/reports/metrics.csv"):
    """
    Guarda las métricas de un modelo en un CSV acumulativo.
    Si el archivo existe, agrega nuevas filas sin borrar las anteriores.
    """
    metrics_df = pd.DataFrame([{
        "model": model_name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }])

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Guardar o anexar
    if os.path.exists(filepath):
        existing_df = pd.read_csv(filepath)
        combined_df = pd.concat([existing_df, metrics_df], ignore_index=True)
        combined_df.to_csv(filepath, index=False)
    else:
        metrics_df.to_csv(filepath, index=False)

def show_metrics(filepath="outputs/reports/metrics.csv"):
    """
    Muestra las métricas guardadas en el CSV.
    """
    if os.path.exists(filepath):
        metrics_df = pd.read_csv(filepath)
        print(metrics_df)
    else:
        print("No se encontraron métricas guardadas.")
