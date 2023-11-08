import pandas as pd
import matplotlib.pyplot as plt

URL='https://datos.madrid.es/egob/catalogo/300178-10-samur-activaciones.csv'

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(data.head())  # Mostrar las primeras filas para visualizar los datos

datos_nulos = data.isnull().sum()
print(datos_nulos)
data = data.dropna()

duplicados = data[data.duplicated()]
print(duplicados)
data = data.drop_duplicates()

meses = {
    'ENERO': 1, 'FEBRERO': 2, 'MARZO': 3, 'ABRIL': 4, 'MAYO': 5, 'JUNIO': 6,
    'JULIO': 7, 'AGOSTO': 8, 'SEPTIEMBRE': 9, 'OCTUBRE': 10, 'NOVIEMBRE': 11, 'DICIEMBRE': 12
}
data['Mes'] = data['Mes'].map(meses)


data['Hora Solicitud'] = pd.to_datetime(data['Hora Solicitud']).dt.hour * 60 + pd.to_datetime(data['Hora Solicitud']).dt.minute
data['Hora Intervención'] = pd.to_datetime(data['Hora Intervención']).dt.hour * 60 + pd.to_datetime(data['Hora Intervención']).dt.minute


print(data.head())


