import os
import pickle
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.utils import save_metrics  # 👈 función para guardar métricas en CSV


def train_traditional_models(X_train, y_train, X_test, y_test, save_path="../models/"):
    """
    Entrena modelos tradicionales (Logistic Regression, Random Forest, XGBoost),
    guarda los modelos entrenados en disco y registra sus métricas en un CSV.

    Parámetros:
    -----------
    X_train : DataFrame
        Variables predictoras de entrenamiento
    y_train : Series
        Variable objetivo de entrenamiento
    X_test : DataFrame
        Variables predictoras de prueba
    y_test : Series
        Variable objetivo de prueba
    save_path : str
        Carpeta donde se guardarán los modelos

    Retorna:
    --------
    models : dict
        Diccionario con los modelos entrenados
    """

    # 📂 Crear la carpeta de modelos si no existe
    os.makedirs(save_path, exist_ok=True)

    # Diccionario para almacenar los modelos entrenados
    models = {}

    # =============================
    # 1. Logistic Regression
    # =============================
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)  # Entrenamos el modelo

    # Guardamos el modelo en formato pickle
    with open(os.path.join(save_path, "logistic_regression.pkl"), "wb") as f:
        pickle.dump(lr, f)
    models['LogisticRegression'] = lr

    # Evaluamos el modelo en el conjunto de prueba
    y_pred = lr.predict(X_test)
    save_metrics("Logistic Regression",  # Nombre del modelo
                 accuracy_score(y_test, y_pred),   # Exactitud
                 precision_score(y_test, y_pred),  # Precisión
                 recall_score(y_test, y_pred),     # Recall
                 f1_score(y_test, y_pred))         # F1 Score

    # =============================
    # 2. Random Forest
    # =============================
    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)

    with open(os.path.join(save_path, "random_forest.pkl"), "wb") as f:
        pickle.dump(rf, f)
    models['RandomForest'] = rf

    y_pred = rf.predict(X_test)
    save_metrics("Random Forest",
                 accuracy_score(y_test, y_pred),
                 precision_score(y_test, y_pred),
                 recall_score(y_test, y_pred),
                 f1_score(y_test, y_pred))

    # =============================
    # 3. XGBoost
    # =============================
    xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    xgb.fit(X_train, y_train)

    with open(os.path.join(save_path, "xgboost.pkl"), "wb") as f:
        pickle.dump(xgb, f)
    models['XGBoost'] = xgb

    y_pred = xgb.predict(X_test)
    save_metrics("XGBoost",
                 accuracy_score(y_test, y_pred),
                 precision_score(y_test, y_pred),
                 recall_score(y_test, y_pred),
                 f1_score(y_test, y_pred))

    # Retornamos todos los modelos entrenados
    return models


def load_traditional_models(save_path="../models/"):
    """
    Carga modelos tradicionales entrenados desde disco.
    """
    models = {}
    for name, filename in [("LogisticRegression", "logistic_regression.pkl"),
                           ("RandomForest", "random_forest.pkl"),
                           ("XGBoost", "xgboost.pkl")]:
        path = os.path.join(save_path, filename)
        if os.path.exists(path):
            with open(path, "rb") as f:
                models[name] = pickle.load(f)
    return models
