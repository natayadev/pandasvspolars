import pandas as pd

# Lectura del archivo network_traffic.csv e impresión de sus primeras filas
df = pd.read_csv('data\\network_traffic.csv')
print(df.head())

# Resumen de los datos del .csv
print(df.describe())
print(df.dtypes)

# Calculamos el número de valores únicos en la columna source_ip
unique_ips = df['source_ip'].nunique()
print(f"Número de IPs únicas: {unique_ips}")

# Calculamos el número de valores nulos en la columna destination_ip
null_destinations = df['destination_ip'].isnull().sum()
print(f"Número de destinos nulos: {null_destinations}")

# Filtramos los datos por protocolo
tcp_traffic = df[df['protocol'] == 'TCP']
print(tcp_traffic)

# Agrupamos por IP y sumamos los bytes enviados
grouped_data = df.groupby('source_ip')['bytes_sent'].sum().reset_index()
print(grouped_data)

#  Calculamos el percentil 99 para encontrar posibles anomalías y filtramos los valores atípicos
threshold = df["bytes_sent"].quantile(0.99) 
anomalous_traffic = df[df["bytes_sent"] > threshold]

print(f"IPs con tráfico inusual: {anomalous_traffic}")