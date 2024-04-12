from sys import stdin, stdout
from math import sqrt
# Función para calcular la distancia euclidiana entre dos puntos
def calcular_distancia(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Lectura de la entrada
N, entrada, salida = map(int, stdin.readline().split())
puntos = []

# Leer las coordenadas de los puntos importantes
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    puntos.append((x, y))

# Inicializar la ruta con la entrada
ruta = [entrada]

# Marcamos la entrada como visitada
visitados = set()
visitados.add(entrada)

# Mientras hayan puntos por visitar
while len(visitados) < N:
    actual = ruta[-1]
    siguiente = None
    min_distancia = float('inf')
    for punto in puntos:
        if punto not in visitados:
            distancia = calcular_distancia(puntos[actual - 1], punto)
            if distancia < min_distancia:
                min_distancia = distancia
                siguiente = punto
    ruta.append(puntos.index(siguiente) + 1)
    visitados.add(siguiente)

# Agregar la salida al final de la ruta
ruta.append(salida)

# Calcular la distancia total de la ruta
distancia_total = sum(calcular_distancia(puntos[ruta[i] - 1], puntos[ruta[i + 1] - 1]) for i in range(N))

# Imprimir la distancia total con 6 dígitos decimales
stdout.write("{:.6f}\n".format(distancia_total))
stdout.flush()