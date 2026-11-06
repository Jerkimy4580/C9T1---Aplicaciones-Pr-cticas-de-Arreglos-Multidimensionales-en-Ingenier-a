"""
=============================================================================
Problema 2: Simulación de Fluido en una Cuadrícula Tridimensional
Descripción: 
    Emplea un arreglo tridimensional (3x3x3) donde cada celda almacena múltiples
    variables físicas (Presión, Temperatura y Velocidad) para simular propagación.
=============================================================================
"""

import numpy as np

print("=" * 60)
print("PROBLEMA 2: SIMULACIÓN DE FLUIDO EN UNA CUADRÍCULA 3D")
print("=" * 60)

# Dimensiones del espacio: 3x3x3 celdas volumétricas, con 4 atributos físicos:
# Índice 0: Presión (kPa), Índice 1: Temperatura (K), Índice 2: Velocidad (m/s)
np.random.seed(42)  # Semilla para reproducibilidad de los datos iniciales
volumen_espacial_fluido = np.zeros((3, 3, 3, 3))

# Inicialización de estados físicos en el volumen
volumen_espacial_fluido[:, :, :, 0] = np.random.uniform(100.0, 105.0, (3, 3, 3)) # Presión
volumen_espacial_fluido[:, :, :, 1] = np.random.uniform(290.0, 310.0, (3, 3, 3)) # Temperatura
volumen_espacial_fluido[:, :, :, 2] = np.random.uniform(0.0, 5.0, (3, 3, 3))     # Velocidad

presion_inicial_centro = volumen_espacial_fluido[1, 1, 1, 0]
print(f"Estado inicial de presión en el nodo central (1,1,1): {presion_inicial_centro:.2f} kPa")

# Copia del volumen para actualizar el estado tras la propagación de ondas
volumen_actualizado = volumen_espacial_fluido.copy()

# Simulación de propagación de onda de presión mediante promedio local con la vecindad
promedio_presion_vecindario = np.mean(volumen_espacial_fluido[:, :, :, 0])
volumen_actualizado[1, 1, 1, 0] = (0.6 * presion_inicial_centro) + (0.4 * promedio_presion_vecindario)

print("\n[Resultados de la Simulación de Fluidos]")
print(f"-> Presión promedio del entorno volumétrico: {promedio_presion_vecindario:.2f} kPa")
print(f"-> Presión propagada y actualizada en el nodo central: {volumen_actualizado[1, 1, 1, 0]:.2f} kPa\n")