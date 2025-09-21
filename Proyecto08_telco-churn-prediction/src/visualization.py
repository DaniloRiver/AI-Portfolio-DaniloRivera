import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plot_churn_distribution(df: pd.DataFrame, churn_col: str = "Churn"):
    """
    Gráfico de torta de la distribución de la variable objetivo.
    """
    if churn_col not in df.columns:
        raise ValueError(f"La columna '{churn_col}' no existe en el DataFrame.")
    return px.pie(df, names=churn_col, title="Distribución de Churn")


def plot_correlation(df: pd.DataFrame):
    """
    Matriz de correlación para variables numéricas.
    """
    corr = df.corr(numeric_only=True)
    fig = px.imshow(corr, text_auto=True, title="Matriz de Correlación")
    return fig


def plot_distributions(df: pd.DataFrame, numeric_cols=None):
    """
    Histogramas de las variables numéricas.
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    figs = []
    for col in numeric_cols:
        fig = px.histogram(df, x=col, nbins=30, title=f"Distribución de {col}")
        figs.append(fig)
    return figs


def plot_categorical_counts(df: pd.DataFrame, cat_cols=None):
    """
    Barras para variables categóricas.
    """
    if cat_cols is None:
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    figs = []
    for col in cat_cols:
        counts = df[col].value_counts().reset_index()
        counts.columns = [col, "count"]
        fig = px.bar(counts, x=col, y="count", title=f"Conteo de {col}")
        figs.append(fig)
    return figs


def plot_churn_analysis(df: pd.DataFrame, churn_col: str = "Churn"):
    """
    Relación de churn con variables numéricas y categóricas.
    """
    if churn_col not in df.columns:
        raise ValueError(f"La columna '{churn_col}' no existe en el DataFrame.")

    figs = []

    # Distribución de churn
    figs.append(plot_churn_distribution(df, churn_col))

    # Numéricas
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if churn_col in numeric_cols:
        numeric_cols.remove(churn_col)

    for col in numeric_cols:
        fig = px.box(df, x=churn_col, y=col, title=f"{col} vs {churn_col}")
        figs.append(fig)

    # Categóricas
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if churn_col in cat_cols:
        cat_cols.remove(churn_col)

    for col in cat_cols:
        fig = px.bar(df, x=col, color=churn_col, barmode="group",
                     title=f"{col} vs {churn_col}")
        figs.append(fig)

    return figs
