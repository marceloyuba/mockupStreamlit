
import pickle 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import xgboost as xgb

#cargamos el modelo entrenado desde el archivo 
with open('df_modelo_tv.pkl', 'rb') as f:
    df99 = pickle.load(f)

# Extraer solo la hora de las columnas hora_inicio y hora_fin
df99['hora_inicio'] = df99['hora_inicio'].apply(lambda x: x.hour)
df99['hora_fin'] = df99['hora_fin'].apply(lambda x: x.hour)

#df99['total_tiempo'] = pd.to_timedelta(df99['total_tiempo'])  # Convertir a tipo timedelta 
# Convertir el formato de total_tiempo a minutps
#df99['total_tiempo_minutos'] = df99['total_tiempo'].dt.total_seconds() / 60

# Eliminar la columna total_tiempo original
#df99.drop('total_tiempo', axis=1, inplace=True)


# Definir el número de clases
NUM_CLASSES = len(df99['modelos'].unique())

# Separar las características (features) y la variable objetivo (target)
x = df99.drop(['anio', 'total_tiempo','modelos','tipo_color','barrio','tipo','Lluvia','Nieve','Temp_Minima','Temp_Maxima'], axis=1) # características
y = df99['modelos'] # target

# Dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Codificar las etiquetas de clase en números enteros
cod_num = LabelEncoder()
y_train_encoded = cod_num.fit_transform(y_train)

# Crear el clasificador XGBoost
clf = xgb.XGBClassifier(objective='multi:softmax', num_class=NUM_CLASSES, random_state=42)

# Entrenar el modelo
clf.fit(x_train, y_train_encoded)

# Hacer predicciones en el conjunto de prueba
y_pred_encoded = clf.predict(x_test)
y_pred = cod_num.inverse_transform(y_pred_encoded)

# Calcular la precisión del modelo
precision = accuracy_score(y_test, y_pred)

#cargamos el modelo entrenado desde el archivo 
with open('x_train.pkl', 'rb') as f:
    modelo_entrenado = pickle.load(f)

def predecir_vehiculo( mes, dia_inicio, hora_inicio, hora_fin,distancia_viaje, ubicacion_inicio, ubicacion_fin,pax, modelo_entrenado):
    # Crear un array numpy con las características
    datos = np.array([[ mes, dia_inicio, hora_inicio, hora_fin, distancia_viaje, ubicacion_inicio, ubicacion_fin, pax]])
    
    
    # Realizar la predicción usando el modelo
    prediccion = modelo_entrenado.predict(datos)
    
    # Decodificar la etiqueta predicha si es necesario
    tipo_vehiculo = cod_num.inverse_transform(prediccion)
    
    return tipo_vehiculo

mmodelo_entrenado = clf

count = 0
# Ejemplo de uso:
for indice, fila in x_train.iterrows():
    tipo_vehiculo_recomendado = predecir_vehiculo(fila['mes'], fila['dia_inicio'],fila['hora_inicio'], fila['hora_fin'],fila['distancia_viaje'], fila['ubicacion_inicio'], fila['ubicacion_fin'],fila['pax'], modelo_entrenado)
    print(f'Para el viaje {indice + 1}, se recomienda el vehiculo: {tipo_vehiculo_recomendado}')

    count +=1 
    if count == 100:
        break