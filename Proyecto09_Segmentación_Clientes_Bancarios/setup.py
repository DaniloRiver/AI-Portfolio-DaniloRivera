from setuptools import setup, find_packages

setup(
    name="bank_segmentation",
    version="0.1.0",
    author="Danilo Rivera",
    description="Segmentación de clientes bancarios con Python, clustering y KPIs",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "scikit-learn>=1.2.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0"
    ],
    python_requires=">=3.10",
)
