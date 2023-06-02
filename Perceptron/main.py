#importar librerias
import numpy as np
import mplt

class perceptron:

  def __init__(
    inicio, n
  ):  # Damos valores iniciales a los pesos para las n entradas, se inicializa

    inicio.pesos = np.random.randn(
      n)  # la cantidad de pesos aleatorios depende del número de entradas n

    inicio.n = n  # almaceno el n

  def salidas(inicio, entradas):

    inicio.salidas_r = 1 * (
      inicio.pesos.dot(entradas) > 0
    )  # se realiza el cálculo de la salida según fórmula del punto 1
    # producto escalar de pesos por entradas con umbral en 0
    inicio.entradas = entradas

  def aprendizaje(inicio, alpha, salidas_deseadas):

    for i in range(
        0,
        inicio.n):  # Se calcularán salidas para el rango de entradas de 0 a n

      inicio.pesos[i] = inicio.pesos[i] + alpha * (
        salidas_deseadas - inicio.salidas_r
      ) * inicio.entradas[i]  # Cálculo de pesos según fórmula del punto 2


perceptron_n_entradas = perceptron(5)  # Creando un perceptrón de 5 entradas

perceptron_n_entradas.pesos

perceptron_n_entradas.salidas([1, 0, 1, 1, 1])

perceptron_n_entradas.salidas_r

perceptron_n_entradas.aprendizaje(
  0.6, 0)  # Cambio el peso y la salida para probar aprendizaje

perceptron_n_entradas.pesos

perceptron_AND_3ent_1sal = perceptron(3)

tabla_AND = np.array([[0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1]])

n = 4

alpha = 0.5

historico_pesos = [perceptron_AND_3ent_1sal.pesos]

repes = 100

for j in range(0, repes):

  for i in range(0, n):

    perceptron_AND_3ent_1sal.salidas(tabla_AND[i, 0:3])

    perceptron_AND_3ent_1sal.aprendizaje(alpha, tabla_AND[i, 3])

    historico_pesos = np.concatenate(
      (historico_pesos, [perceptron_AND_3ent_1sal.pesos]), axis=0)

mplt.plot(historico_pesos[:, 0], 'k')
mplt.plot(historico_pesos[:, 1], 'r')
mplt.plot(historico_pesos[:, 2], 'b')
mplt.show()
