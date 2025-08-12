Inteligencia Artificial - Ejercicios de Búsqueda y Rutas Óptimas

Este repositorio contiene tres ejercicios enfocados en la implementación de algoritmos de búsqueda y optimización de rutas en diferentes contextos: búsqueda A*, resolución de laberintos con costos de terreno, y comparación entre BFS e IDS en un grafo de estaciones.

Contenido

Ejercicio 1 → Implementación genérica de A* para problemas de búsqueda de rutas.

Ejercicio 2 → Búsqueda en un laberinto con múltiples salidas y costos variables por terreno.

Ejercicio 3 → Comparación de BFS e IDS en un grafo de estaciones.

Ejercicio 1 - Algoritmo A* genérico

Análisis del problema
El objetivo es encontrar la secuencia de acciones que lleva desde un estado inicial hasta un estado objetivo con el menor costo total posible.
El problema se modela con:

Estado inicial y meta.

Acciones disponibles.

Función de resultado.

Función de costo.

Heurística para estimar la distancia a la meta.

Aplicación de A*
A* combina:
f(n) = g(n) + h(n)

g(n): costo real desde el inicio.

h(n): costo estimado hasta la meta.

El nodo con menor f(n) se expande primero.
La búsqueda termina cuando se alcanza la meta, garantizando optimalidad si la heurística es admisible.

Optimalidad

Cola de prioridad para expandir el nodo más prometedor.

Registro de estados visitados para evitar rutas más caras.

Si la heurística no sobreestima, el camino encontrado es el más barato posible.

Ejercicio 2 - Laberinto con múltiples salidas y costos de terreno

Efecto de cambiar la función de costo

Penalizar ciertos terrenos → el algoritmo evita zonas costosas aunque sean más cortas en distancia.

Costos uniformes → se comporta como BFS.

Costos negativos → puede perder optimalidad y generar bucles.

Múltiples salidas

El código ya acepta varias metas en la lista goals.

Se elige la primera salida óptima encontrada.

Propuesta de mejora: explorar todas las salidas y devolver la de menor path_cost.

Laberinto más grande y nuevos obstáculos

El algoritmo sigue funcionando mientras los costos sean positivos.

Limitaciones:

Más tiempo y memoria en mapas grandes.

Heurística Manhattan no considera tipos de terreno.

Limitación detectada

La heurística no contempla costos adicionales del terreno, lo que reduce la eficiencia.

Ejercicio 3 - Comparación BFS vs IDS en un grafo de estaciones

Diseño del grafo

Red de estaciones con costo uniforme en todas las aristas.

Representada como diccionario de adyacencia.

Implementación

Clase Node: estado, padre, acción, profundidad.

Clase Problem: estado inicial, meta, acciones y resultado.

Función reconstruct_path para obtener la ruta encontrada.

Algoritmos

BFS

Explora por niveles.

Encuentra la ruta más corta en pasos.

Mayor consumo de memoria.

IDS

DFS con límite de profundidad creciente.

Óptimo en pasos, pero más lento por repeticiones.

Menor consumo de memoria.

Comparación
Algoritmo | Tiempo | Memoria | Ventaja | Desventaja
BFS | Bajo | Alto | Siempre óptimo en pasos | Alto uso de memoria
IDS | Mayor | Bajo | Bajo consumo de memoria | Repetición de nodos

Conclusiones generales

A* es ideal cuando se dispone de una heurística informada y se busca optimalidad en costo.

Laberintos con múltiples salidas requieren modificaciones para evaluar todas las metas posibles.

BFS es óptimo en pasos, pero consume mucha memoria en grafos grandes.

IDS ahorra memoria, pero sacrifica tiempo por repeticiones.

La elección del algoritmo depende del tipo de problema, tamaño del espacio de búsqueda y recursos disponibles.
