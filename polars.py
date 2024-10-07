import polars as pl

# Lectura del archivo network_traffic.csv e impresión de sus primeras filas
df = pl.read_csv('data\\network_traffic.csv')
print(df.head())

# Resumen de los datos del .csv
print(df.describe())
print(df.dtypes)

# Calculamos el número de valores únicos en la columna source_ip
unique_ips = df.select(pl.col("source_ip").n_unique()).item()
print(f"Número de IPs únicas: {unique_ips}")

# Calculamos el número de valores nulos en la columna destination_ip
null_destinations = df.select(pl.col("destination_ip").is_null().sum()).item()
print(f"Número de destinos nulos: {null_destinations}")

# Filtramos los datos por protocolo
tcp_traffic = df.filter(pl.col('protocol') == 'TCP')
print(tcp_traffic)

# Agrupamos por IP y sumamos los bytes enviados
grouped_data = df.group_by('source_ip').agg(
    [pl.sum('bytes_sent').alias('total_bytes_sent')])
print(grouped_data)

#  Calculamos el percentil 99 para encontrar posibles anomalías y filtramos los valores atípicos
threshold = df.select(pl.quantile("bytes_sent", 0.99)).item()
anomalous_traffic = df.filter(pl.col("bytes_sent") > threshold)

print(f"IPs con tráfico inusual: {anomalous_traffic}")
