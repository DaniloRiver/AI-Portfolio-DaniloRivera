import gradio as gr
import joblib
import numpy as np
import tensorflow as tf

# Cargar modelos
rf_model = joblib.load("models/random_forest.pkl")
xgb_model = joblib.load("models/xgboost.pkl")
lr_model = joblib.load("models/logistic_regression.pkl")
nn_model = tf.keras.models.load_model("models/neural_network.h5")

def predict(model_name, features):
    features = np.array(features.split(","), dtype=float).reshape(1, -1)

    if model_name == "Random Forest":
        return rf_model.predict(features)[0]
    elif model_name == "XGBoost":
        return xgb_model.predict(features)[0]
    elif model_name == "Logistic Regression":
        return lr_model.predict(features)[0]
    elif model_name == "Neural Network":
        return (nn_model.predict(features) > 0.5).astype(int)[0][0]

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Radio(["Random Forest", "XGBoost", "Logistic Regression", "Neural Network"], label="Modelo"),
        gr.Textbox(label="Features separadas por coma")
    ],
    outputs="text",
)

if __name__ == "__main__":
    demo.launch()
