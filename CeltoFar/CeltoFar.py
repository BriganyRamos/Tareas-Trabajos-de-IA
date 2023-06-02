import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
faheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa1 = tf.keras.layers.Dense(units = 3, input_shape = [1])
capa2 = tf.keras.layers.Dense(units = 3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([capa1,capa2,salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print('El entrenamiento a iniciado...')
historial = modelo.fit(celsius, faheit, epochs=900)
print('Entrenamiento finalizado...')


plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

resultado = modelo.predict([100.0])
print("El resultado es: " + str(resultado))
