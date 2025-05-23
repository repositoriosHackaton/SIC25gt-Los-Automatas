import tensorflow as tf #librería utilizada para la creación de modelos de aprendizaje automático
# import tensorflow_datasets as tfds #nos da acceso a los datasets preparados para el uso con tensorflow
import matplotlib.pyplot as plt #librería que nos permite visualizar imagenes
import math #para usar ecuaciones matematicas
import numpy as np #librería para poder trabajar con matrices
import cv2 as cv #nos facilita el tratar con imagenes
from medmnist import PneumoniaMNIST, INFO #librería que nos permite acceder a un dataset de imagenes de rayos x

# Cargar cada división del dataset por separado
datos_entrenamiento = PneumoniaMNIST(split='train', transform=None, download=True, as_rgb=False)
datos_pruebas = PneumoniaMNIST(split='test', transform=None, download=True, as_rgb=False)
datos_validacion = PneumoniaMNIST(split='val', transform=None, download=True, as_rgb=False)

# Obtener metadatos del dataset
metadatos = INFO['pneumoniamnist']


#* Convertir medmnist a tf.data.Dataset para poder usarlo con TensorFlow
def convertirATf(dataset):
    imagenes = dataset.imgs
    etiquetas = dataset.labels
    return tf.data.Dataset.from_tensor_slices((imagenes, etiquetas))


datos_entrenamiento = convertirATf(datos_entrenamiento)
datos_pruebas = convertirATf(datos_pruebas)
datos_validacion = convertirATf(datos_validacion)

# Confirmar la cantidad de datos
num_ej_entrenamiento = len(datos_entrenamiento)
num_ej_pruebas = len(datos_pruebas)
num_ej_validacion = len(datos_validacion)

print(f"Datos de entrenamiento: {num_ej_entrenamiento}")
print(f"Datos de prueba: {num_ej_pruebas}")
print(f"Datos de validación: {num_ej_validacion}")

# Obtener nombres de las clases
nombres_clases = ["Normal", "Neumonía"]
print('='*50)
print(f"Nombres de las clases: {nombres_clases}")
print('='*50)


#Normalizar los datos hace que la red aprenda mejor y más rapido
def normalizar(imagenes, etiquetas):
    imagenes = tf.cast(imagenes, tf.float32)#convertimos a tipo float para su uso
    imagenes /= 255 #pasamos de 0-255 a 0-1
    return imagenes, etiquetas

#Normalizar los datos con la funcion que hicimos
datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_pruebas = datos_pruebas.map(normalizar)
datos_validacion = datos_validacion.map(normalizar)

#Agregar a cache (usar memoria en lugar de disco, entrenamiento mas rapido)
datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()

#Probamos que todo funcione correctamente mostrando imagenes del dataset
plt.figure(figsize=(10,10)) #cambiamos el tamaño de las imagenes para mostrar varias

for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):  # Usamos 25 ejemplos
    imagen = imagen.numpy().reshape((28,28))  # Redimensionamos y la convertimos en un array de numpy
    etiqueta = etiqueta.numpy()  # Convertimos el tensor de etiqueta a un array de numpy
    etiqueta = int(etiqueta)  # Convertimos el array de numpy a un valor escalar (entero)
    plt.subplot(5,5,i+1)  # Muestra las imágenes en un cuadro de 5x5
    plt.xticks([])  # Quitamos los ejes para que no se miren
    plt.yticks([])
    plt.grid(False)  # Desactivamos la cuadrícula
    plt.imshow(imagen, cmap=plt.cm.binary)  # Pone la imagen en escala de grises
    plt.xlabel(nombres_clases[etiqueta])  # Muestra las etiquetas de cada imagen
plt.show()  # Mostramos las imágenes

#Crear el modelo
#usamos una red de tipo secuencial
modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)), #flatten pasa a una sola dimension
    #capas ocultas
    tf.keras.layers.Dense(80, activation=tf.nn.relu), #usamos la función de activación de relu
    tf.keras.layers.Dense(35, activation=tf.nn.relu),
    #tenemos dos salidas
    tf.keras.layers.Dense(2, activation='softmax') #Softmax para redes de clasificación, así vemos que la suma en la salida sea siempre 1

])

#Compilar el modelo
modelo.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

#ya que son varios datos usaremos lotes para poder entrenar una gran cantidad de datos

#guardamos el número de datos que tenemos de prueba y de entrenamiento
num_ej_entrenamiento = len(datos_entrenamiento)
num_ej_pruebas = len(datos_pruebas)
num_ej_validacion = len(datos_validacion)

#confirmamos cuantos datos hay
print("="*50)
print(f"Número de ejemplos de entrenamiento: {num_ej_entrenamiento}")
print(f"Número de ejemplos de prueba: {num_ej_pruebas}")
print(f"Número de ejemplos de validación: {num_ej_validacion}")
print("="*50)

lote = 32
#Shuffle y repeat hacen que los datos esten mezclados de manera aleatoria para que la red no se aprenda el orden de las cosas
datos_entrenamiento = datos_entrenamiento.repeat().shuffle(num_ej_entrenamiento).batch(lote)
datos_pruebas = datos_pruebas.batch(lote)
datos_validacion = datos_validacion.batch(lote)

#Entrenar la red
historial = modelo.fit(datos_entrenamiento, epochs=200, steps_per_epoch= math.ceil(num_ej_entrenamiento/lote), validation_data= datos_validacion, validation_steps=math.ceil(num_ej_validacion / lote))

#Ver la funcion de perdida
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

# guardar modelo
modelo.save("modelo_pneumonia.keras", save_format="keras", include_optimizer=False)
