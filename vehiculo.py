import pickle 
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb

def cargar_modelo(ruta_modelo):
    with open(ruta_modelo, 'rb') as f:
        modelo = pickle.load(f)
    return modelo

def predecir_vehiculo(datos, modelo):
    # Realizar la predicción usando el modelo
    prediccion = modelo.predict(datos)
    return prediccion

def main():
    # Cargar el modelo entrenado
    modelo_entrenado = cargar_modelo('xtrain.pkl')

    # Ejemplo de datos de entrada para predecir
    datos_ejemplo = np.array([['mes', 'dia_inicio', 'hora_inicio', 'hora_fin', 'distancia_viaje', 'ubicacion_inicio', 'ubicacion_fin', 'pax']])

    # Realizar la predicción usando la función predefinida
    tipo_vehiculo_predicho = predecir_vehiculo(datos_ejemplo, modelo_entrenado)

    print(f'Se recomienda el vehículo: {tipo_vehiculo_predicho}')

if __name__ == "__main__":
    main()