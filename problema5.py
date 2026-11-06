"""
=============================================================================
Problema 5: Transformación de Coordenadas en un Sistema Cartesiano
Descripción: 
    Representa un conjunto de puntos 2D en una matriz y aplica una transformación 
    lineal (rotación geométrica) mediante multiplicación matricial optimizada.
=============================================================================
"""

import numpy as np

print("=" * 60)
print("PROBLEMA 5: TRANSFORMACIÓN DE COORDENADAS CARTESIANAS")
print("=" * 60)

# Matriz de puntos cartesianos originales en formato Nx2 ([x, y])
puntos_cartesianos_originales = np.array([
    [2.0, 1.0],
    [4.0, 1.0],
    [3.0, 5.0]
])

print("Coordenadas originales de los vértices:\n", puntos_cartesianos_originales)

# Definición de ángulo de rotación (90 grados) en radianes
angulo_rotacion_grados = 90.0
angulo_radianes = np.radians(angulo_rotacion_grados)
cos_angulo, sin_angulo = np.cos(angulo_radianes), np.sin(angulo_radianes)

# Construcción de la matriz de transformación lineal de rotación 2x2
matriz_transformacion_rotacion = np.array([
    [cos_angulo, -sin_angulo],
    [sin_angulo,  cos_angulo]
])

# Aplicación de la transformación lineal mediante producto punto matricial optimizado
puntos_transformados = np.dot(puntos_cartesianos_originales, matriz_transformacion_rotacion.T)

print(f"\nMatriz de Transformación Lineal (Rotación de {angulo_rotacion_grados}°):\n", matriz_transformacion_rotacion)
print("\n[Resultados de la Transformación Geométrica]")
print("Coordenadas de los puntos después de la transformación:\n", np.round(puntos_transformados, 2))
print("-> Transformación aplicada exitosamente conservando la integridad espacial de la estructura.\n")