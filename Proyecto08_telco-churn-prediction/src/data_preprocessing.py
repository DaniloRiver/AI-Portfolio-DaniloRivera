import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def load_data(path: str) -> pd.DataFrame:
    """
    Carga dataset desde un archivo CSV.
    """
    df = pd.read_csv(path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpieza básica del dataset:
    - Convertir columnas numéricas que estén como objeto a float.
    - Manejar valores nulos.
    """
    # Convertir TotalCharges a float (puede venir como string)
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Llenar nulos con medianas o ceros según corresponda
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col].fillna(df[col].median(), inplace=True)
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna('Unknown', inplace=True)
    
    return df

def encode_features(df: pd.DataFrame, target_col: str = 'Churn', training: bool = True) -> pd.DataFrame:
    """
    Codifica variables categóricas a numéricas.
    Si training=True, codifica también la columna target.
    """
    df_encoded = df.copy()
    le = LabelEncoder()
    
    for col in df_encoded.select_dtypes(include=['object', 'category']).columns:
        if training or col != target_col:
            df_encoded[col] = le.fit_transform(df_encoded[col])
    
    # Codificar target solo si estamos entrenando y existe en df
    if training and target_col in df_encoded.columns:
        if df_encoded[target_col].dtype == 'object':
            df_encoded[target_col] = le.fit_transform(df_encoded[target_col])
    
    return df_encoded



def scale_features(df: pd.DataFrame, feature_cols: list) -> pd.DataFrame:
    """
    Escala las variables numéricas.
    """
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[feature_cols] = scaler.fit_transform(df_scaled[feature_cols])
    return df_scaled

def split_data(df: pd.DataFrame, target_col: str = 'Churn', test_size: float = 0.2, random_state: int = 42):
    """
    Divide el dataset en entrenamiento y prueba.
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    return X_train, X_test, y_train, y_test
