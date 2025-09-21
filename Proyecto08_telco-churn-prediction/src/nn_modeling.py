import os
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.utils import save_metrics  # 👈 función para registrar métricas en CSV


def train_neural_network(X_train, y_train, X_test, y_test,
                         save_path="../models/", epochs=20, batch_size=32):
    """
    Entrena una red neuronal artificial simple para predicción de churn,
    guarda el modelo en disco (.h5) y registra métricas de evaluación en un CSV.

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
        Carpeta donde se guardará el modelo
    epochs : int
        Número de épocas de entrenamiento
    batch_size : int
        Tamaño del batch para el entrenamiento

    Retorna:
    --------
    nn : keras.Model
        Red neuronal entrenada
    """

    # 📂 Crear carpeta de modelos si no existe
    os.makedirs(save_path, exist_ok=True)

    # =============================
    # Definición de la red neuronal
    # =============================
    input_dim = X_train.shape[1]  # número de features

    nn = Sequential([
        Dense(32, activation='relu', input_shape=(input_dim,)),  # Capa oculta 1
        Dense(16, activation='relu'),                            # Capa oculta 2
        Dense(1, activation='sigmoid')                           # Capa de salida (binaria)
    ])

    # =============================
    # Compilación del modelo
    # =============================
    nn.compile(optimizer='adam',
               loss='binary_crossentropy',  # pérdida para clasificación binaria
               metrics=['accuracy'])

    # =============================
    # Entrenamiento del modelo
    # =============================
    nn.fit(X_train, y_train,
           epochs=epochs,
           batch_size=batch_size,
           validation_split=0.2,  # usamos 20% del train para validación
           verbose=0)             # ocultar logs

    # =============================
    # Guardar el modelo en disco
    # =============================
    nn.save(os.path.join(save_path, "neural_network.h5"))

    # =============================
    # Evaluación en test y guardado de métricas
    # =============================
    y_pred = (nn.predict(X_test) > 0.5).astype("int32")  # convertir probabilidades a clases
    save_metrics("Neural Network",
                 accuracy_score(y_test, y_pred),
                 precision_score(y_test, y_pred),
                 recall_score(y_test, y_pred),
                 f1_score(y_test, y_pred))

    return nn


def load_neural_network(save_path="../models/"):
    """
    Carga un modelo de red neuronal entrenado desde disco (.h5).
    """
    path = os.path.join(save_path, "neural_network.h5")
    if os.path.exists(path):
        return load_model(path)
    return None
