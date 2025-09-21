# src/clustering.py
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import joblib
import os

def find_optimal_k(X, k_range=range(2,10)):
    inertia = []
    silhouette_scores = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
        inertia.append(km.inertia_)
        silhouette_scores.append(silhouette_score(X, km.labels_))
    return inertia, silhouette_scores

def run_kmeans(X, n_clusters=4):
    km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    return km, labels

def plot_pca(X, labels, save_path=None):
    pca = PCA(n_components=2, random_state=42)
    pca_result = pca.fit_transform(X)
    plt.figure(figsize=(8,6))
    plt.scatter(pca_result[:,0], pca_result[:,1], c=labels, cmap='tab10', alpha=0.7)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("Clusters PCA")
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()
    return pca

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)
