"""
=============================================================================
Problema 4: Manejo de Datos en una Tabla de Sensores
Descripción: 
    Organiza lecturas de temperatura en una matriz bidimensional (5x5) 
    y calcula promedios y desviaciones estándar por sensor y por momento temporal.
=============================================================================
"""

import numpy as np

print("=" * 60)
print("PROBLEMA 4: MANEJO DE DATOS EN UNA TABLA DE SENSORES")
print("=" * 60)

# Matriz 5x5: Filas = Momentos en el tiempo (T1 a T5), Columnas = Sensores (S1 a S5)
np.random.seed(5)
matriz_datos_sensores = np.round(np.random.uniform(18.5, 32.0, size=(5, 5)), 2)

print("Tabla de Datos de Sensores (°C) [Filas: Tiempo | Columnas: Sensores S1-S5]:\n", matriz_datos_sensores)

# Análisis estadístico por columnas (Sensores independientes)
promedios_por_sensor = np.mean(matriz_datos_sensores, axis=0)
desviaciones_por_sensor = np.std(matriz_datos_sensores, axis=0)

# Análisis estadístico por filas (Momentos temporales globales)
promedios_por_tiempo = np.mean(matriz_datos_sensores, axis=1)
desviaciones_por_tiempo = np.std(matriz_datos_sensores, axis=1)

print("\n[Resultados Estadísticos por Sensor (Columnas)]")
print(f"  * Promedios por sensor: {promedios_por_sensor}")
print(f"  * Desviaciones estándar por sensor: {np.round(desviaciones_por_sensor, 2)}")

print("\n[Resultados Estadísticos por Momento Temporal (Filas)]")
print(f"  * Promedios por momento temporal: {promedios_por_tiempo}")
print(f"  * Desviaciones estándar por momento temporal: {np.round(desviaciones_por_tiempo, 2)}\n")