import tensorflow as tf #librería utilizada para la creación de modelos de aprendizaje automático
# import tensorflow_datasets as tfds #nos da acceso a los datasets preparados para el uso con tensorflow
import matplotlib.pyplot as plt #librería que nos permite visualizar imagenes
import math #para usar ecuaciones matematicas
import numpy as np #librería para poder trabajar con matrices
import cv2 as cv #nos facilita el tratar con imagenes
from medmnist import PneumoniaMNIST, INFO #librería que nos permite acceder a un dataset de imagenes de rayos x
from modelo import *
from interfazInicio import interfazInicio
import os


os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

#cargar modelo, de esta manera no se debe de hacer siempre
try:
    # modelo = tf.keras.models.load_model("modelo_pneumonia.keras")
    modelo = tf.keras.models.load_model("modelo_pneumonia.keras", compile=False)
    modelo.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=['accuracy']
    )
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")

# Función para preprocesar la imagen
def preprocesar_imagen(ruta_imagen):
    imagen = cv.imread(ruta_imagen, cv.IMREAD_GRAYSCALE)  # Cargar en escala de grises
    imagen = cv.resize(imagen, (28, 28))  # Redimensionar a 28x28
    imagen = imagen / 255.0  # Normalizar a valores entre 0 y 1
    imagen = np.expand_dims(imagen, axis=-1)  # Añadir dimensión de canal
    imagen = np.expand_dims(imagen, axis=0)  # Añadir dimensión de batch
    return imagen

# Función para hacer la predicción
def predecir_neumonia(ruta_imagen):
    imagen_procesada = preprocesar_imagen(ruta_imagen) #preprocesamos las imagenes para ingresarlas al modelo
    prediccion = modelo.predict(imagen_procesada) #usamos el modelo entrenado para clasificar las imagenes
    clase = np.argmax(prediccion)  # 0: Normal, 1: Neumonía
    resultado = "Neumonía" if clase == 1 else "Normal"

    #* obtener porcentaje de confianza
    porcentajePrediccion = 100 * np.max(prediccion)
    porcentajePrediccionStr = f"{porcentajePrediccion:.2f}%"

    return resultado, porcentajePrediccionStr

# Ruta de la imagen a analizar
def analizarImg(ruta_imagen):
    resultado, porcentajePrediccionStr = predecir_neumonia(ruta_imagen) #analizamos la imagen para clasificarla
    print(f"Resultado del análisis: {resultado}")#mostramos el resultado

    #leemos la imagen
    imagen = cv.imread(ruta_imagen, cv.IMREAD_GRAYSCALE)

    # Mostrar la imagen con Matplotlib
    plt.imshow(imagen, cmap='gray')  # Mostrar en escala de grises
    plt.axis("off")  # Ocultar ejes
    plt.subplots_adjust(bottom=0.2)
    plt.figtext(0.5, 0.01, f"Resultado del análisis: {porcentajePrediccionStr} de {resultado}", 
        ha="center", fontsize=12, bbox={"facecolor": "white", "alpha": 0.7, "pad": 5})
    plt.show()

    return resultado, porcentajePrediccionStr


if __name__ == "__main__": #evita el llamado desde la interfaz principal
    interfazInicio()