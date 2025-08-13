Informe 1

Contenido

Ejercicio 1 

Ejercicio 2 

Ejercicio 3

**Ejercicio 1**

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


¿Por qué se considera que la ruta encontrada es óptima?


Cola de prioridad para expandir el nodo más prometedor.

Registro de estados visitados para evitar rutas más caras.

Si la heurística no sobreestima, el camino encontrado es el más barato posible.


**Ejercicio 2**


¿Cómo cambia el comportamiento del algoritmo si cambiamos la función de costo?


Penalizar ciertos terrenos → el algoritmo evita zonas costosas aunque sean más cortas en distancia.

Costos uniformes → se comporta como BFS.

Costos negativos → puede perder optimalidad y generar bucles.


Qué sucede si hay múltiples salidas en el laberinto? ¿Cómo podrías modificar el algoritmo para manejar esto? Plantea una
propuesta.


El código ya acepta varias metas en la lista goals.

Se elige la primera salida óptima encontrada.

Propuesta de mejora: explorar todas las salidas y devolver la de menor path_cost.

Laberinto más grande y nuevos obstáculos

El algoritmo sigue funcionando mientras los costos sean positivos.


Modifica el laberinto por uno más grande y con otro tipo de obstáculo además de paredes. ¿Qué limitación encuentras en el
algoritmo? 


Más tiempo y memoria en mapas grandes.

Heurística Manhattan no considera tipos de terreno.

Limitación detectada

La heurística no contempla costos adicionales del terreno, lo que reduce la eficiencia.


**Ejercicio 3** 

Realice el diseño del grafo considerando un costo de igual valor
entre estaciones.

A -- B -- D -- G
| |
C E -- H
|
I -- J
C -- F -- J


Red de estaciones con costo uniforme en todas las aristas.

Representada como diccionario de adyacencia.


Implementación: Haz las definiciones pertinentes para la clase Node y Problem así como también la definición de actions.


Clase Node: estado, padre, acción, profundidad.

Clase Problem: estado inicial, meta, acciones y resultado.

Función reconstruct_path para obtener la ruta encontrada.


Algoritmos: Implementa dos versiones del algoritmo de búsqueda:


BFS

Explora por niveles.

Encuentra la ruta más corta en pasos.

Mayor consumo de memoria.

IDS

DFS con límite de profundidad creciente.

Óptimo en pasos, pero más lento por repeticiones.

Menor consumo de memoria.

Comparación: Ejecuta ambos algoritmos para encontrar la ruta más corta entre las estaciones A y J. Compara los resultados obtenidos en
términos de tiempo de ejecución y memoria.


Explica las diferencias encontradas entre ambos algoritmos.

BFS:
Tiempo: bajo, ya que explora cada nodo una sola vez.
Memoria: mayor consumo debido a almacenar muchos nodos en la frontera.
Ventaja: siempre retorna la solución más corta en pasos.

IDS:
Tiempo: mayor, por repeticiones de exploración.
Memoria: menor que BFS, ya que la profundidad límite controla el espacio usado.
Ventaja: consumo de memoria reducido comparado con BFS.


Diferencias clave
BFS:
Expande por niveles.
Óptimo en pasos si el grafo no pondera costos.
Alto consumo de memoria en grafos grandes.

IDS:
Óptimo en pasos, pero más lento debido a repeticiones.
Bajo consumo de memoria.
Adecuado cuando no sabemos la profundidad de la meta y la memoria es limitada.
