import pandas as pd
import matplotlib.pyplot as plt

URL = "activaciones_samur_2023.csv"

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(data.head())  # Mostrar las primeras filas para visualizar los datos



