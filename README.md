# Tarea_argenis
Ultima tarea Metodos cuantitativos
README - Planificador de Fuerza Laboral con Programación Dinámica
Descripción
Este programa implementa una solución basada en Programación Dinámica y Programación Orientada a Objetos (POO) para optimizar el tamaño de la fuerza laboral semana a semana, minimizando los costos totales asociados con contrataciones y mantenimiento de trabajadores excedentes.

Requisitos
Python 3.x

Instalación
No se requiere instalación especial. Solo asegúrese de tener Python 3 instalado en su sistema.

Uso
Clone el repositorio o copie el código en un archivo llamado workforce_planner.py

Ejecute el programa con: python workforce_planner.py

Personalización de parámetros
Puede modificar los siguientes parámetros en el código:# Datos del problema (demanda semanal de trabajadores)
demands = [5, 7, 8, 4, 6]

# Parámetros de costos (opcional)
planner = WorkforcePlanner(
    demands,
    hire_fixed_cost=400,  # Costo fijo por contratación
    hire_var_cost=200,    # Costo por trabajador contratado
    excess_cost=300       # Costo por trabajador excedente por semana
)
Explicación de la solución
El programa utiliza programación dinámica para encontrar el plan óptimo que minimice los costos totales, considerando:

Costos de contratación:

Costo fijo: $400 por proceso de contratación

Costo variable: $200 por cada nuevo trabajador contratado

Costos de excedentes:

$300 por cada trabajador excedente por semana

Salida del programa
El programa muestra una tabla detallada con:

Número de semana

Demanda de trabajadores

Trabajadores contratados

Costo de contratación

Costo de excedentes

Costo acumulado total
