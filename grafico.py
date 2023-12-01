import matplotlib.pyplot as plt
import random
import time

class GraficoDinamico:
    def __init__(self, y):
        self.x = list(range(len(y)))
        self.y = y

        # Crear un gráfico de líneas
        plt.ion()  # Modo interactivo
        self.linea, = plt.plot(self.x, y, marker='o', linestyle='-')

        # Etiquetas de los ejes
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')

        # Título del gráfico
        plt.title('Gráfico De Ventas')

        # Mostrar el gráfico
        plt.show()

    def actualizar_grafico(self, nuevos_y):
        # Actualizar los datos
        self.y = nuevos_y

        # Actualizar la línea en el gráfico
        self.linea.set_ydata(nuevos_y)

        # Actualizar la visualización del gráfico
        plt.draw()

    def agregar_punto(self, x_punto, y_punto):
        # Agregar un punto al conjunto de datos
        self.x.append(x_punto)
        self.y.append(y_punto)

        # Actualizar la línea en el gráfico
        self.linea.set_xdata(self.x)
        self.linea.set_ydata(self.y)

        # Actualizar la visualización del gráfico
        plt.draw()

 