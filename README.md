# Análisis Exploratorio de Datos (EDA) de Tráfico de Red
Este proyecto es un ejemplo sencillo de cómo realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos de tráfico de red, utilizando Polars y Pandas en Python. Se realiza una comparativa en términos de uso y rendimiento entre ambas bibliotecas.

El análisis se realiza sobre un archivo CSV que contiene 10,000 filas de datos de tráfico de red, incluyendo información sobre las IPs de origen y destino, el protocolo utilizado, la cantidad de bytes enviados y recibidos, y las marcas de tiempo.

### Contenido
El repositorio incluye los siguientes elementos:

- `polars.py`: Script que realiza el análisis utilizando la biblioteca Polars.
- `pandas.py`: Script que realiza el análisis utilizando la biblioteca Pandas.
- `notebook.ipynb`: Notebook Jupyter que muestra una comparación entre Polars y Pandas en términos de facilidad de uso y rendimiento, junto con ejemplos de EDA.
Carpeta `data`: Contiene el archivo `network_traffic.csv` con los datos de tráfico de red.

### Requisitos
Para ejecutar este proyecto necesitarás:

- Python 3.x
- Pandas
- Polars
- Jupyter (opcional, para ejecutar la notebook)

### Cómo usar
```
python polars.py
```
```
python pandas.py
```
```
jupyter notebook notebook.ipynb
```
