"""
=============================================================================
Problema 1: Análisis de Fuerzas en una Estructura
Descripción:
    Modela un sistema de fuerzas aplicadas en nodos estructurales (3x3)
    utilizando una matriz bidimensional y calcula el equilibrio estático
    y las reacciones nodales equivalentes.
=============================================================================
"""

import numpy as np

print("=" * 60)
print("PROBLEMA 1: ANÁLISIS DE FUERZAS EN UNA ESTRUCTURA")
print("=" * 60)

# Matriz bidimensional 3x3 que representa las fuerzas aplicadas (en Newtons)
# Filas y columnas representan la distribución espacial en los nodos de la estructura.
matriz_fuerzas_nodos = np.array([
    [ 12.5,  -3.2,   8.1],
    [  5.4,  18.0,  -2.5],
    [ -4.1,   9.6,  22.4]
])

print("Matriz de fuerzas aplicadas en los nodos (N):\n", matriz_fuerzas_nodos)

# Operaciones vectorizadas para el análisis de equilibrio
# Sumatoria de fuerzas por columna (componentes espaciales del sistema)
fuerza_resultante_por_eje = np.sum(matriz_fuerzas_nodos, axis=0)

# Sumatoria de carga total soportada por cada nodo estructural (filas)
carga_total_por_nodo = np.sum(matriz_fuerzas_nodos, axis=1)

# Cálculo de la fuerza de reacción global requerida para el equilibrio estático (ΣF = 0)
reaccion_estatica_global = -np.sum(matriz_fuerzas_nodos)

print("\n[Resultados del Análisis Estructural]")
print(f"-> Sumatoria de fuerzas por eje (Columnas): {fuerza_resultante_por_eje}")
print(f"-> Carga acumulada por nodo estructural (Filas): {carga_total_por_nodo}")
print(f"-> Reacción estática global necesaria: {reaccion_estatica_global:.2f} N\n")