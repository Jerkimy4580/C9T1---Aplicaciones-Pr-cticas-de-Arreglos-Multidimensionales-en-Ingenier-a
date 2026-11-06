"""
=============================================================================
Problema 3: Análisis de Imágenes Médicas en 3D
Descripción: 
    Modela un volumen de tomografía como un tensor 3D de capas 2D y aplica 
    un algoritmo de suavizado espacial (filtro de promedio) para reducir ruido.
=============================================================================
"""

import numpy as np

print("=" * 60)
print("PROBLEMA 3: ANÁLISIS DE IMÁGENES MÉDICAS EN 3D (SUAVIZADO)")
print("=" * 60)

# Generación de un volumen 3D sintético (5 capas de profundidad, resolución 4x4)
np.random.seed(10)
volumen_medico_original = np.random.randint(60, 180, size=(5, 4, 4)).astype(float)

# Introducción intencional de un artefacto de ruido extremo en la capa central (índice 2)
volumen_medico_original[2, 2, 2] = 255.0

print("Capa 2 del volumen médico original (con ruido de alta frecuencia):\n", volumen_medico_original[2])

# Copia para almacenar el volumen procesado
volumen_medico_suavizado = np.copy(volumen_medico_original)
profundidad_vol, alto_img, ancho_img = volumen_medico_original.shape

# Aplicación del filtro de suavizado (promedio de vecinos 3x3) capa por capa
for z in range(profundidad_vol):
    capa_actual = volumen_medico_original[z]
    capa_filtrada = np.copy(capa_actual)
    
    for i in range(1, alto_img - 1):
        for j in range(1, ancho_img - 1):
            # Extracción del vecindario local de 3x3
            vecindario_local = capa_actual[i-1:i+2, j-1:j+2]
            # Reemplazo por el promedio aritmético local para atenuar el ruido
            capa_filtrada[i, j] = np.mean(vecindario_local)
            
    volumen_medico_suavizado[z] = capa_filtrada
    
print("\n[Resultados del Procesamiento de Imagen Médica]")
print("Capa 2 tras la aplicación exitosa del filtro de suavizado:\n", np.round(volumen_medico_suavizado[2], 2))
print("-> El ruido puntual ha sido atenuado eficientemente manteniendo la estructura anatómica.\n")