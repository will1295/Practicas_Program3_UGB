import tensorflow as tf
import numpy as np

dolares = np.array([60,1,10,7,88,24,98,100], dtype=float)
libras = np.array([52.02,0.87,8.77,6.07,76.30,20.81,84.97,86.70],dtype=float)

capa1 = tf.keras.layers.Dense(units=1, input_shape=[1])
capa2 = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([capa1,capa2])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)


entrenamiento = modelo.fit(dolares,libras,epochs=250)
print("Probando mi ia que convierte dolares a libras")
num= float(input("Por favor ingresa una cantidad en dolares: $"))
resultado= modelo.predict([num])
print("Hola humano tu resultado es:", resultado)

