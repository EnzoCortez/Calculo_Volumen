import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
altura = np.array([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8])
distancia_al_borde = np.array([0.36, 0.67, 0.87, 1.02, 1.16, 1.28, 1.39, 1.51, 1.60, 1.67, 1.80, 1.85, 1.92, 2.00, 2.06, 2.18, 2.23, 2.26, 2.36, 2.43, 2.07, 1.90, 1.65, 1.43, 1.24, 1.13, 0.91, 0.63, 0.37])

# Función para ajustar el cono (parte superior del tanque)
def funcion_cono(h, m, b):
    return m * h + b

# Ajuste de la función cono a los datos
params_cono, _ = curve_fit(funcion_cono, altura, distancia_al_borde)

# Función para el cono ajustada
def cono(h):
    return params_cono[0] * h + params_cono[1]

# Graficar los datos y el ajuste del cono
plt.scatter(altura, distancia_al_borde, label='Datos')
plt.plot(altura, cono(altura), color='red', label='Ajuste del cono')
plt.xlabel('Altura (m)')
plt.ylabel('Distancia al borde (m)')
plt.title('Ajuste de cono para la parte superior del tanque')
plt.legend()
plt.grid(True)
plt.show()
# Función para ajustar la parte inferior del tanque
def funcion_inferior(h, a, b, c):
    return a * h**2 + b * h + c

# Ajuste de la función inferior a los datos
params_inferior, _ = curve_fit(funcion_inferior, altura, distancia_al_borde)

# Función para la parte inferior del tanque ajustada
def inferior(h):
    return params_inferior[0] * h**2 + params_inferior[1] * h + params_inferior[2]

# Graficar los datos y el ajuste de la parte inferior del tanque
plt.scatter(altura, distancia_al_borde, label='Datos')
plt.plot(altura, inferior(altura), color='blue', label='Ajuste de la parte inferior')
plt.xlabel('Altura (m)')
plt.ylabel('Distancia al borde (m)')
plt.title('Ajuste de la parte inferior del tanque')
plt.legend()
plt.grid(True)
plt.show()
# Calcular el volumen de la parte inferior del tanque utilizando sumatorias
volumen_inferior = 0
for i in range(len(altura) - 1):
    delta_h = altura[i+1] - altura[i]
    promedio_radio = (inferior(altura[i]) + inferior(altura[i+1])) / 2
    volumen_inferior += np.pi * promedio_radio**2 * delta_h

# Calcular el volumen de la parte superior del tanque (cono)
h_maxima = altura[-1]
radio_superior = cono(h_maxima)
volumen_superior = (1/3) * np.pi * radio_superior**2 * h_maxima

# Calcular el volumen total del tanque
volumen_total = volumen_inferior + volumen_superior

print("Volumen total del tanque:", volumen_total, "metros cúbicos")
